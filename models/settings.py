from pydantic import BaseModel

class Setting(BaseModel):
	site_logo:str
	aboutus:str
	client_email:str
	client_phone:str
	client_address:str
	status:str
	created_at:str


class Terms(BaseModel):
	terms_condition:str
	privacy_policy:str
	status:str
	created_at:str

class Banners(BaseModel):
	banner_image:str
	status:str


class SocialLinks(BaseModel):
	social_media_name:str
	social_img: str
	social_link: str
	status:str

class Contactus(BaseModel):
	contactus_name:str
	contactus_email: str
	contactus_message: str
	status:str

class Pincode(BaseModel):
	valid_pincode:str
	status:str

class Aboutimg(BaseModel):
	aboutImg_1:str
	aboutImg_2:str
	aboutImg_3:str
	aboutImg_4:str
	aboutImg_5:str
	aboutImg_6:str
	aboutImg_7:str

class Landingimg(BaseModel):
	landingImg:str
	status:str