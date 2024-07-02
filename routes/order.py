from fastapi import APIRouter
from models.order import Order, Updatestatus
from config.db import conn
from schemas.order import orderEntity, ordersEntity ,orderscusJoinEntity, ordercustomerEntity
from schemas.customer import customersEntity
from controllers.order import orderCheck, orderCustomer
from datetime import datetime
from bson.objectid import ObjectId
from config.mobileApi import MobileSMS

order = APIRouter()

@order.get("/order", tags=["Orders"])
async def find_all():
    return ordersEntity(conn.ecomdb.order.find({"status":"1"}))

@order.get("/order/{order_id}", tags=["Orders"])
async def find_order(order_id):
   return orderscusJoinEntity(orderCheck(order_id))

@order.get("/orderCustomer/{customer_id}", tags=["Orders"])
async def find_order_customer(customer_id):
	return orderscusJoinEntity(orderCustomer(customer_id))

@order.post("/order", tags=["Orders"])
async def create_order(order: Order):
	try:
		order_val = dict(order)
		incr_val = conn.ecomdb.order.count_documents({})
		if incr_val != 0:
			incr_new_val = 10001 + incr_val
			incr_id = "ORD" + str(incr_new_val)
		else:
			incr_id = "ORD10001"

		order_val['order_id'] = incr_id
		conn.ecomdb.order.insert_one(order_val)
		customer_id = order_val['customer_id']
		conn.ecomdb.cart.update_many({"customer_id": customer_id, "status": "1"},
									{'$set': {"status": "2"}})
		#print("here1")
		#exit(0)
		#CC
		if order_val['cc']:
			valid_cc = conn.ecomdb.coupon.find_one({"status": "1", "cc": order_val['cc']})
			insert_user_coupon['customer_no'] = order_val['customer_no']
			insert_user_coupon['cc'] = order_val['cc']
			insert_user_coupon['discount_amt'] = int(order_val['difference'])
			conn.ecomdb.user_coupon.insert_one(insert_user_coupon)

			inc_count = int(valid_cc['cnt']) + 1
			conn.ecomdb.coupon.update_one({"cc": order_val['cc']},
										  {'$set': {"cnt": inc_count}})
		print("here2")
		#SMS
		#order_sms = conn.ecomdb.customer.find_one({"customer_id": customer_id})
		#result_sms = MobileSMS('NDQ0ODYzNjY2YzY5NTQ1NTM3NmQ1MTZhNDk0YjZhNTg=', "91" + order_sms['customer_phone'] + "", "SRIVKT",
		#					   "Dear Customer, Your order " + str(incr_id) + "will be delivered soon. Keep ordering from Sri Venkateshwara Classic.")
		print("here3")
		#print("Here", result_sms)
		return {"message:success"}
	except Exception as e:
		return {"Error in Insert", e}

@order.delete("/order/{id}", tags=["Orders"])
async def delete_order(id):
	conn.ecomdb.order.update_one({"_id": ObjectId(id)}, {"$set": {"status":"0"}})
	return ordersEntity(conn.ecomdb.order.find({"_id": ObjectId(id)}))

'''@order.put("/order/{order_id}/{order_status}", tags=["Orders"])
async def order_status(order_id,order_status):
	conn.ecomdb.order.update_one({"order_id": order_id}, {"$set": {"order_status":order_status}})
	return ordersEntity(conn.ecomdb.order.find({"order_id": order_id}))'''

@order.put("/order/{order_id}", tags=["Orders"])
async def order_status(order_id,order:Updatestatus):
	conn.ecomdb.order.update_one({"order_id": order_id}, {"$set": dict(order)})
	return ordersEntity(conn.ecomdb.order.find({"order_id": order_id}))
