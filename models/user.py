from pydantic import BaseModel

class User(BaseModel):
	user_name:str
	user_phone:str
	user_email:str
	login_password: str
	user_address:str
	status:str
	created_at:str


class UserLogin(BaseModel):
	user_id:str
	login_password: str
	