from fastapi import APIRouter
from config.db import conn
from datetime import datetime
from bson.objectid import ObjectId
from models.tags import Tags, Attributes
from schemas.tags import tagsEntity, attsEntity

tags = APIRouter()

@tags.get("/tags", tags=["tags"])
async def find_all():
	return tagsEntity(conn.ecomdb.tag.find({"status":"1"}))

@tags.get("/tags/{id}", tags=["tags"])
async def find_tag(id):
	return tagsEntity(conn.ecomdb.tag.find({"_id": ObjectId(id),"status":"1"}))

@tags.post("/tags", tags=["tags"])
async def create_tags(tags: Tags):
	try:
		tag_val = dict(tags)
		incr_val = conn.ecomdb.tag.count_documents({})
		if incr_val != 0:
			incr_new_val = 10001 + incr_val
			incr_id = "TAG" + str(incr_new_val)
		else:
			incr_id = "TAG10001"

		tag_val['tag_id'] = incr_id
		conn.ecomdb.tag.insert_one(tag_val)
		return {"message:success"}
	except:
		return {"Error in Insert"}

@tags.put("/tags/{id}", tags=["tags"])
async def update_tag(id,tags: Tags):
	conn.ecomdb.tag.update_one({"_id": ObjectId(id)}, {"$set": dict(tags)})
	return tagsEntity(conn.ecomdb.tag.find({"_id": ObjectId(id)}))

@tags.get("/attribute", tags=["Attribute"])
async def find_all():
	return attsEntity(conn.ecomdb.attribute.find({"status":"1"}))

@tags.get("/attribute/{att_id}", tags=["Attribute"])
async def find_all(att_id):
	return attsEntity(conn.ecomdb.attribute.find({"att_id":att_id,"status":"1"}))

@tags.post("/attribute", tags=["Attribute"])
async def create_attribute(attribute: Attributes):
	try:
		attribute_val = dict(attribute)
		incr_val = conn.ecomdb.attribute.count_documents({})
		if incr_val != 0:
			incr_new_val = 101 + incr_val
			incr_id = "ATT" + str(incr_new_val)
		else:
			incr_id = "ATT101"

		attribute_val['att_id'] = incr_id
		conn.ecomdb.attribute.insert_one(attribute_val)
		return {"message:success"}
	except:
		return {"Error in Insert"}


@tags.put("/attribute/{att_id}", tags=["Attribute"])
async def update_tag(att_id,attribute: Attributes):
	conn.ecomdb.attribute.update_one({"att_id": att_id}, {"$set": dict(attribute)})
	return attsEntity(conn.ecomdb.attribute.find({"att_id": att_id}))