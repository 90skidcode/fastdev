from datetime import datetime

def categoryEntity(item) -> dict:
	return{
		"id":str(item["_id"]),
		"category_no": item["category_no"],
		"category_name":item["category_name"],
		"category_description":item["category_description"],
		"category_image":item["category_image"],
		"status":item["status"],
		"created_at":item["created_at"]
		}

def categorysEntity(entity) -> list:
	return[categoryEntity(item) for item in entity]