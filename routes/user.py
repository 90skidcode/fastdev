from fastapi import APIRouter
from models.user import User, UserLogin
from config.db import conn
from schemas.user import userEntity, usersEntity
from datetime import datetime
from bson.objectid import ObjectId

user = APIRouter()

@user.get("/user", tags=["users"])
async def find_all():
	return usersEntity(conn.ecomdb.user.find({"status":"1"}))

@user.get("/user/{id}", tags=["users"])
async def find_user(id):
	return usersEntity(conn.ecomdb.user.find({"_id": ObjectId(id),"status":"1"}))


@user.post("/userLogin", tags=["Login"])
async def find_user(userLogin:UserLogin):
	Loginval =  usersEntity(conn.ecomdb.user.find(dict(userLogin)))
	if len(Loginval) == 0:
		return {"status_code":"201","Message":"Invalid Login"}
	else:
		return {"status_code":"200","Message":Loginval}

@user.post("/user", tags=["users"])
async def create_user(user: User):
	try:
		user_val = dict(user)
		incr_val = conn.ecomdb.user.count_documents({})
		if incr_val != 0:
			incr_new_val = 101 + incr_val
			incr_id = "VKT" + str(incr_new_val)
		else:
			incr_id = "VKT101"

		user_val['user_id'] = incr_id
		conn.ecomdb.user.insert_one(user_val)
		return {"message:success"}
	except:
		return {"Error in Insert"}

@user.put("/user/{id}", tags=["users"])
async def update_user(id,user: User):
	conn.ecomdb.user.update_one({"_id": ObjectId(id)}, {"$set": dict(user)})
	return usersEntity(conn.ecomdb.user.find({"_id": ObjectId(id)}))

@user.delete("/user/{id}", tags=["users"])
async def delete_user(id):
	conn.ecomdb.user.update_one({"_id": ObjectId(id)}, {"$set": {"status":"0"}})
	return usersEntity(conn.ecomdb.user.find({"_id": ObjectId(id)}))