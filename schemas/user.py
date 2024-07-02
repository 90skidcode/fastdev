def userEntity(item) -> dict:
	return{
		"id":str(item["_id"]),
		"user_id":item["user_id"],
		"user_name":item["user_name"],
		"user_phone":item["user_phone"],
		"user_email":item["user_email"],
		"user_address":item["user_address"],
		"status": item["status"],
		"created_at": item["created_at"]
		}

def usersEntity(entity) -> list:
	return[userEntity(item) for item in entity]