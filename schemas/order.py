from datetime import datetime
from schemas.customer import customersEntity
from schemas.products import productsEntity

def orderEntity(item) -> dict:
	return{
		"id":str(item["_id"]),
		"order_id":item["order_id"],
		"customer_id":item["customer_id"],
		"product_id":item["product_id"],
		"delivery_address":item["delivery_address"],
		"payment_mode":item["payment_mode"],
		"order_amount":item["order_amount"],
		"delivery_status":item["delivery_status"],
		"order_status":item["order_status"],
		"cc":"" if "cc" not in item else item["cc"],
		"difference":"" if "difference" not in item else item["difference"],
		"online_transaction_id": item["online_transaction_id"],
		"status":item["status"],
		"created_at":item["created_at"]
		}

def ordersEntity(entity) -> list:
	return[orderEntity(item) for item in entity]


def ordercustomerEntity(item) -> dict:
	return{
		"id":str(item["_id"]),
		"order_id":item["order_id"],
		"customer_id":item["customer_id"],
		"product_id":item["product_id"],
		"delivery_address":item["delivery_address"],
		"payment_mode":item["payment_mode"],
		"order_amount":item["order_amount"],
		"delivery_status":item["delivery_status"],
		"order_status":item["order_status"],
		"cc": "" if "cc" not in item else item["cc"],
		"difference": "" if "difference" not in item else item["difference"],
		"online_transaction_id":item["online_transaction_id"],
		"customer_info":customersEntity(item["customer_info"]),
		"status":item["status"],
		"created_at":item["created_at"]
		}

def orderscusJoinEntity(entity) -> list:
	return[ordercustomerEntity(item) for item in entity]
