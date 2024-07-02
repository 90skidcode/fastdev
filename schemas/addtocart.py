from schemas.products import productsEntity

def addtocartEntity(item) -> dict:
	return{
		"id":str(item["_id"]),
		"customer_id": item["customer_id"],
		"product_code":item["product_code"],
		"quantity":item["quantity"],
		"attribute_id":"" if "attribute_id" not in item else item["attribute_id"],
		"status":item["status"],
		"created_at":item["created_at"],
		}

def listaddtocartEntity(entity) -> list:
	return[addtocartEntity(item) for item in entity]


def addtocartProductEntity(item) -> dict:
	return{
		"id":str(item["_id"]),
		"customer_id": item["customer_id"],
		"product_code":item["product_code"],
		"quantity":item["quantity"],
		"status":item["status"],
		"attribute_id": "" if "attribute_id" not in item else item["attribute_id"],
		"product_info": productsEntity(item["product_info"]),
		"created_at":item["created_at"],
		"created_at": item["created_at"],
		}

def listaddtocartProductEntity(entity) -> list:
	return[addtocartProductEntity(item) for item in entity]

def whishlistEntity(item) -> dict:
	return{
		"id":str(item["_id"]),
		"customer_id": item["customer_id"],
		"product_code":item["product_code"],
		"status":item["status"],
		"created_at":item["created_at"],
		}

def listwhishlistEntity(entity) -> list:
	return[whishlistEntity(item) for item in entity]