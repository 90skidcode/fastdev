from fastapi import APIRouter
from models.franchise import Franchise
from config.db import conn
from schemas.franchise import franchiseEntity, franchisesEntity
from datetime import datetime
from bson.objectid import ObjectId

franchise = APIRouter()

@franchise.get("/franchise", tags=["franchise"])
async def find_all():
	return franchisesEntity(conn.ecomdb.franchise.find({"status":"1"}))

@franchise.get("/franchise/{id}", tags=["franchise"])
async def find_franchise(id):
	return franchisesEntity(conn.ecomdb.franchise.find({"_id": ObjectId(id),"status":"1"}))
	
@franchise.post("/franchise", tags=["franchise"])
async def create_franchise(franchise: Franchise):
	try:
		franchise_val = dict(franchise)
		incr_val = conn.ecomdb.franchise.count_documents({})
		if incr_val != 0:
			incr_new_val = 101 + incr_val
			incr_id = "FRAN" + str(incr_new_val)
		else:
			incr_id = "FRAN101"

		franchise_val['franchise_no'] = incr_id
		conn.ecomdb.franchise.insert_one(franchise_val)
		return {"Success"}
	except:
		return{"Error in Insert"}

@franchise.put("/franchise/{id}", tags=["franchise"])
async def update_franchise(id,franchise: Franchise):
	conn.ecomdb.franchise.update_one({"_id": ObjectId(id)}, {"$set": dict(franchise)})
	return franchisesEntity(conn.ecomdb.franchise.find({"_id": ObjectId(id)}))

@franchise.delete("/franchise/{id}", tags=["franchise"])
async def delete_franchise(id):
	conn.ecomdb.franchise.update_one({"_id": ObjectId(id)}, {"$set": {"status":"0"}})
	return franchisesEntity(conn.ecomdb.franchise.find({"_id": ObjectId(id)}))