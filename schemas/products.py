from config.db import conn
from datetime import datetime
from schemas.category import categorysEntity, categoryEntity

def productEntity(item) -> dict:
	return{
		"id":str(item["_id"]),
		"product_code": item["product_code"],
		"product_name":item["product_name"],
		"product_img": "" if "product_img" not in item else item["product_img"],
		"category_id":item["category_id"],
		"product_description":item["product_description"],
		"product_quantity": item["product_quantity"],
		"attribute_id": "" if "attribute_id" not in item else productattvalCheck(item["attribute_id"]),
		"tags": "" if "tags" not in item else item["tags"],
		"visible": item["visible"],
		"sku": item["sku"],
		"status":item["status"],
		"created_at":item["created_at"],
		}

def productlookupEntity(item) -> dict:
	return{
		"id":str(item["_id"]),
		"product_code": item["product_code"],
		"product_name":item["product_name"],
		"product_img": "" if "product_img" not in item else item["product_img"],
		"category_id":item["category_id"],
		"product_description":item["product_description"],
		"product_quantity": item["product_quantity"],
		"attribute_id": "" if "attribute_id" not in item else productattvalCheck(item["attribute_id"]),
		"tags": "" if "tags" not in item else item["tags"],
		"visible": item["visible"],
		"sku": item["sku"],
		"status":item["status"],
		"created_at":item["created_at"],
		"category_info": categorysEntity(item["category_info"])
		}

def productsEntity(entity) -> list:
	return[productEntity(item) for item in entity]

def productjoinEntity(entity) -> list:
	return[productlookupEntity(item) for item in entity]



def productattvalCheck(resval):
	if isinstance(resval, list) == True:
		for attributeVal in resval:
			select_attr = conn.ecomdb.attribute.find_one({"att_id": attributeVal['att_id']},
														 {"att_name": 1, "status": 1})
			att_name = select_attr['att_name']
			attributeVal['att_value'] = att_name


	return resval
