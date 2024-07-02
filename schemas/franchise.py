from datetime import datetime

def franchiseEntity(item) -> dict:
	return{
		"id":str(item["_id"]),
		"franchise_no":item["franchise_no"],
		"franchise_name":item["franchise_name"],
		"franchise_address":item["franchise_address"],
		"franchise_phone":item["franchise_phone"],
		"franchise_email":item["franchise_email"],
		"franchise_country":item["franchise_country"],
		"franchise_state":item["franchise_state"],
		"franchise_city":item["franchise_city"],
		"franchise_pincode":item["franchise_pincode"],
		"status":item["status"],
		"created_at":item["created_at"]
		}

def franchisesEntity(entity) -> list:
	return[franchiseEntity(item) for item in entity]