from pydantic import BaseModel

class Addtocart(BaseModel):
	customer_id:str
	product_code:str
	quantity:int
	attribute_id:str
	status:str
	created_at:str

class Whishlist(BaseModel):
	customer_id:str
	product_code:str
	status:str
	created_at:str

class Updatecart(BaseModel):
	customer_id:str
	product_code:str
	quantitystatus:str
	attribute_id: str