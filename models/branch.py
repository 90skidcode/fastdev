from pydantic import BaseModel

class Branch(BaseModel):
	branch_name:str
	branch_address:str
	branch_phone:str
	branch_email:str
	branch_country:str
	branch_state:str
	branch_city:str
	branch_pincode:str
	status:int
	created_at:str