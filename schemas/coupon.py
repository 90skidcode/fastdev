from datetime import datetime

#cc- couponcode, sd-startdate, ed-Enddate, det_type-detuctiontype {flat,percentage}, value- value of discount, cnt- noused
# limit- to used, user_cnt - user limit, min_val - min amount
def couponEntity(item) -> dict:
	return{
		"id":str(item["_id"]),
		"cc":item["cc"],
		"sd":item["sd"],
		"ed":item["ed"],
		"det_type":item["det_type"],
		"value":item["value"],
		"user_cnt":"0" if "user_cnt" not in item else item["user_cnt"],
		"min_val":"0" if "min_val" not in item else item["min_val"],
		"description": "" if "description" not in item else item["description"],
		"cnt":item["cnt"],
		"limit":item["limit"],
		"status":item["status"],
		"created_at":item["created_at"]
		}

def couponsEntity(entity) -> list:
	return[couponEntity(item) for item in entity]