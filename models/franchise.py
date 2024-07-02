from pydantic import BaseModel

class Franchise(BaseModel):
	franchise_name:str
	franchise_address:str
	franchise_phone:str
	franchise_email:str
	franchise_country:str
	franchise_state:str
	franchise_city:str
	franchise_pincode:str
	status:str
	created_at:str