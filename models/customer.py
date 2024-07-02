from pydantic import BaseModel

class Customer(BaseModel):
	customer_fname:str
	customer_lname:str
	customer_phone:str
	customer_email:str
	customer_joining:str
	customer_img:str
	status:str
	created_at:str

class CustomerLogin(BaseModel):
	customer_phone:str
	otp:str

class CustomerAddress(BaseModel):
	customer_no:str
	customer_addr_name: str
	customer_addr_phone:str
	customer_addr_email:str
	customer_addr_locality: str
	customer_addr_address: str
	customer_addr_city: str
	customer_addr_state: str
	customer_addr_pincode: str
	customer_addr_landmark: str
	customer_addr_altphone: str
	customer_addr_type: str
	status:str
	created_at:str