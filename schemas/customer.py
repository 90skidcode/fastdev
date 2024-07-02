def customerEntity(item) -> dict:
	return{
		"id":str(item["_id"]),
		"customer_no": item["customer_no"],
		"customer_fname": item["customer_fname"],
		"customer_lname": item["customer_lname"],
		"customer_phone": item["customer_phone"],
		"customer_email": item["customer_email"],
		"customer_joining": item["customer_joining"],
		"customer_img": item["customer_img"],
		"status":item["status"],
		"created_at":item["created_at"]
		}

def customersEntity(entity) -> list:
	return[customerEntity(item) for item in entity]

def customerLoginEntity(item) -> dict:
	return{
		"id":str(item["_id"]),
		"customer_phone": item["customer_phone"],
		"otp": item["otp"]
		}

def customersLoginEN(entity) -> list:
	return[customerLoginEntity(item) for item in entity]


def customerAddressEntity(item) -> dict:
	return{
		"id":str(item["_id"]),
		"customer_no": item["customer_no"],
		"customer_addr_name": item["customer_addr_name"],
		"customer_addr_phone": item["customer_addr_phone"],
		"customer_addr_email": item["customer_addr_email"],
		"customer_addr_locality": item["customer_addr_locality"],
		"customer_addr_address": item["customer_addr_address"],
		"customer_addr_city": item["customer_addr_city"],
		"customer_addr_state": item["customer_addr_state"],
		"customer_addr_pincode": item["customer_addr_pincode"],
		"customer_addr_landmark": item["customer_addr_landmark"],
		"customer_addr_altphone": item["customer_addr_altphone"],
		"customer_addr_type": item["customer_addr_type"],
		"status":item["status"],
		"created_at":item["created_at"]
		}

def customersAddEntity(entity) -> list:
	return[customerAddressEntity(item) for item in entity]