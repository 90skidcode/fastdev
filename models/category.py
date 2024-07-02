from pydantic import BaseModel

class Category(BaseModel):
	category_name:str
	category_description:str
	category_image: str
	status:int
	created_at:str