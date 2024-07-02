from pydantic import BaseModel

class Product(BaseModel):
	product_name:str
	product_img:str
	category_id:str
	product_description:str
	product_quantity:str
	attribute_id:list
	tags:list
	visible:str
	sku:str
	status:str
	created_at:str


class ProductCat(BaseModel):
	category_id:list