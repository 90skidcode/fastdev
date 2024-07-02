from datetime import datetime

def tagEntity(item) -> dict:
	return{
		"id":str(item["_id"]),
		"tag_id":item["tag_id"],
		"tag_name":item["tag_name"],
		"status":item["status"],
		"created_at":item["created_at"]
		}

def tagsEntity(entity) -> list:
	return[tagEntity(item) for item in entity]


def attEntity(item) -> dict:
	return{
		"id":str(item["_id"]),
		"att_id":item["att_id"],
		"att_name":item["att_name"],
		"status":item["status"],
		"created_at":item["created_at"]
		}

def attsEntity(entity) -> list:
	return[attEntity(item) for item in entity]