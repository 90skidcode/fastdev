from pydantic import BaseModel

class Tags(BaseModel):
	tag_name:str
	status:str
	created_at:str


class Attributes(BaseModel):
	att_name:str
	status:str
	created_at:str