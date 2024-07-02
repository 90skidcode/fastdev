from fastapi import APIRouter
from models.category import Category
from config.db import conn
from schemas.category import categoryEntity,categorysEntity
from datetime import datetime
from bson.objectid import ObjectId

category = APIRouter()

@category.get("/category", tags=["Category"])
async def find_all():
    return categorysEntity(conn.ecomdb.category.find({"status":1}))

@category.get("/category/{id}", tags=["Category"])
async def find_category(id):
    return categorysEntity(conn.ecomdb.category.find({"_id": ObjectId(id),"status":1}))


@category.post("/category", tags=["Category"])
async def create_category(category: Category):
    try:
        cat_val = dict(category)
        incr_val = conn.ecomdb.category.count_documents({})
        if incr_val != 0:
            incr_new_val = 101 + incr_val
            incr_id = "CAT" + str(incr_new_val)
        else:
            incr_id = "CAT101"

        cat_val['category_no'] = incr_id
        conn.ecomdb.category.insert_one(cat_val)
        return {"Success"}
    except:
        return {"Error"}

@category.put("/category/{id}", tags=["Category"])
async def update_category(id,category: Category):
	conn.ecomdb.category.update_one({"_id": ObjectId(id)}, {"$set": dict(category)})
	return categorysEntity(conn.ecomdb.category.find({"_id": ObjectId(id)}))

@category.delete("/category/{id}", tags=["Category"])
async def delete_category(id):
	conn.ecomdb.category.update_one({"_id": ObjectId(id)}, {"$set": {"status":0}})
	return categorysEntity(conn.ecomdb.category.find({"_id": ObjectId(id)}))