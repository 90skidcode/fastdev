from fastapi import APIRouter
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from models.branch import Branch
from config.db import conn
from schemas.branch import branchEntity, branchsEntity
from datetime import datetime
from bson.objectid import ObjectId

branch = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="qwerty")

@branch.get("/branch", tags=["branch"])
async def find_all(token: str = Depends(oauth2_scheme)):
	return branchsEntity(conn.ecomdb.branch.find({"status":"1"}))

@branch.get("/branch/{id}", tags=["branch"])
async def find_branch(id):
	return branchsEntity(conn.ecomdb.branch.find({"_id": ObjectId(id),"status":"1"}))

@branch.post("/branch", tags=["branch"])
async def create_user(branch: Branch):
	try:
		branch_val = dict(branch)
		incr_val = conn.ecomdb.branch.count_documents({})
		if incr_val != 0:
			incr_new_val = 10001 + incr_val
			incr_id = "BRAN" + str(incr_new_val)
		else:
			incr_id = "BRAN10001"

		branch_val['branch_no'] = incr_id
		conn.ecomdb.branch.insert_one(branch_val)
		return {"message:success"}
	except:
		return {"Error in Insert"}

@branch.put("/branch/{id}", tags=["branch"])
async def update_branch(id,branch: Branch):
	conn.ecomdb.branch.update_one({"_id": ObjectId(id)}, {"$set": dict(branch)})
	return branchsEntity(conn.ecomdb.branch.find({"_id": ObjectId(id)}))

@branch.delete("/branch/{id}", tags=["branch"])
async def delete_branch(id):
	conn.ecomdb.branch.update_one({"_id": ObjectId(id)}, {"$set": {"status":"0"}})
	return branchsEntity(conn.ecomdb.branch.find({"_id": ObjectId(id)}))

