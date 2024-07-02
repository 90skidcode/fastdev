from fastapi import APIRouter
from config.db import conn
from datetime import datetime
from bson.objectid import ObjectId
from models.coupon import Coupon, Validate_model
from schemas.coupon import couponsEntity
from controllers.coupon import validate_coupon


coupons = APIRouter()

@coupons.get("/coupons", tags=["coupons"])
async def find_coupons():
	return couponsEntity(conn.ecomdb.coupon.find({"status":"1"}))

#@coupons.get("/coupons/{coupon}", tags=["coupons"])
#async def check_coupons(coupon):
#	if len(coupon) == 0:
#		return {"message:Coupon Empty"}
#	else:
#		return couponsEntity(conn.ecomdb.coupon.find({"cc": coupon,"status":"1"}))

@coupons.get("/coupons/{id}", tags=["coupons"])
async def check_coupons_id(id):
	if len(id) == 0:
		return {"message:Coupon Empty"}
	else:
		return couponsEntity(conn.ecomdb.coupon.find({"_id": ObjectId(id),"status":"1"}))

@coupons.post("/coupons", tags=["coupons"])
async def create_coupons(coupons: Coupon):
	try:
		conn.ecomdb.coupon.insert_one(dict(coupons))
		return {"message:success"}
	except:
		return {"Error in Insert"}


@coupons.put("/coupons/{id}", tags=["coupons"])
async def update_coupons(id,coupons: Coupon):
	conn.ecomdb.coupon.update_one({"_id": ObjectId(id)}, {"$set": dict(coupons)})
	return couponsEntity(conn.ecomdb.coupon.find({"_id": ObjectId(id)}))

@coupons.delete("/coupons/{id}", tags=["coupons"])
async def delete_coupons(id):
	conn.ecomdb.coupon.update_one({"_id": ObjectId(id)}, {"$set": {"status":"0"}})
	return couponsEntity(conn.ecomdb.coupon.find({"_id": ObjectId(id)}))


@coupons.post("/validate_coupons", tags=["coupons"])
async def validate_coupons(validate_coupons:Validate_model):
	return validate_coupon(validate_coupons)
