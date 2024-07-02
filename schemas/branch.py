from datetime import datetime

def branchEntity(item) -> dict:
	return{
		"id":str(item["_id"]),
		"branch_no":item["branch_no"],
		"branch_name":item["branch_name"],
		"branch_address":item["branch_address"],
		"branch_phone":item["branch_phone"],
		"branch_email":item["branch_email"],
		"branch_country":item["branch_country"],
		"branch_state":item["branch_state"],
		"branch_city":item["branch_city"],
		"branch_pincode":item["branch_pincode"],
		"status":item["status"],
		"created_at":item["created_at"]
		}

def branchsEntity(entity) -> list:
	return[branchEntity(item) for item in entity]