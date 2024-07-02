def settingEntity(item) -> dict:
	return{
		"id":str(item["_id"]),
		"site_logo":item["site_logo"],
		"aboutus":item["aboutus"],
		"client_email": item["client_email"],
		"client_phone": item["client_phone"],
		"client_address": item["client_address"],
		"status":item["status"],
		"created_at":item["created_at"],
		}

def settingsEntity(entity) -> list:
	return[settingEntity(item) for item in entity]


def termsEntity(item) -> dict:
	return{
		"id":str(item["_id"]),
		"terms_condition": item["terms_condition"],
		"privacy_policy":item["privacy_policy"],
		"status":item["status"],
		"created_at":item["created_at"],
		}

def termsConditionEntity(entity) -> list:
	return[termsEntity(item) for item in entity]


def bannerEntity(item) -> dict:
	return{
		"id":str(item["_id"]),
		"banner_image":item["banner_image"],
		"status":item["status"],
		}

def bannerConditionEntity(entity) -> list:
	return[bannerEntity(item) for item in entity]


def socialEntity(item) -> dict:
	return{
		"id":str(item["_id"]),
		"social_media_name":item["social_media_name"],
		"social_img":item["social_img"],
		"social_link":item["social_link"],
		"status":item["status"],
		}

def socialConditionEntity(entity) -> list:
	return[socialEntity(item) for item in entity]


def contactusEntity(item) -> dict:
	return{
		"id":str(item["_id"]),
		"social_media_name":item["social_media_name"],
		"social_img":item["social_img"],
		"social_link":item["social_link"],
		"status":item["status"],
		}

def contactusConditionEntity(entity) -> list:
	return[contactusEntity(item) for item in entity]

def pincodeEntity(item) -> dict:
	return{
		"id":str(item["_id"]),
		"valid_pincode":item["valid_pincode"],
		"status":item["status"],
		}

def pincodeConditionEntity(entity) -> list:
	return[pincodeEntity(item) for item in entity]

def abtimgEntity(item) -> dict:
	return{
		"id":str(item["_id"]),
		"aboutImg_1":item["aboutImg_1"],
		"aboutImg_2":item["aboutImg_2"],
		"aboutImg_3":item["aboutImg_3"],
		"aboutImg_4":item["aboutImg_4"],
		"aboutImg_5":item["aboutImg_5"],
		"aboutImg_6":item["aboutImg_6"],
		"aboutImg_7":item["aboutImg_7"],
		}

def abtimgConditionEntity(entity) -> list:
	return[abtimgEntity(item) for item in entity]

def landimgEntity(item) -> dict:
	return{
		"id":str(item["_id"]),
		"landingImg":item["landingImg"],
		"status":item["status"],
		}

def landimgConditionEntity(entity) -> list:
	return[landimgEntity(item) for item in entity]

