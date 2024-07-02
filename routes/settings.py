from fastapi import APIRouter, File, UploadFile
from models.settings import Setting, Terms, Banners, SocialLinks, Pincode, Aboutimg, Landingimg, Contactus
from schemas.settings import settingsEntity, termsConditionEntity, bannerConditionEntity, contactusConditionEntity, socialConditionEntity, pincodeConditionEntity, abtimgConditionEntity, landimgConditionEntity
from config.db import conn
from bson.objectid import ObjectId
from typing import List
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig

settings = APIRouter()

@settings.get("/settings", tags=["Settings"])
async def find_settings():
	return settingsEntity(conn.ecomdb.settings.find({"status":"1"}))

@settings.get("/terms", tags=["Settings"])
async def find_terms():
	return termsConditionEntity(conn.ecomdb.terms.find({"status":"1"}))

@settings.post('/settings', tags=["Settings"])
async def create_settings(settings:Setting):
	try:
		conn.ecomdb.settings.insert_one(dict(settings))
		return {"message:success"}
	except:
		return {"Error in Insert"}

@settings.post('/terms', tags=["Settings"])
async def create_terms(terms:Terms):
	try:
		conn.ecomdb.terms.insert_one(dict(terms))
		return {"message:success"}
	except:
		return {"Error in Insert"}

@settings.put("/settings/{id}", tags=["Settings"])
async def update_settings(id,settings:Setting):
	conn.ecomdb.settings.update_one({"_id": ObjectId(id)}, {"$set": dict(settings)})
	return settingsEntity(conn.ecomdb.settings.find({"_id": ObjectId(id)}))

@settings.put("/terms/{id}", tags=["Settings"])
async def update_terms(id,terms:Terms):
	conn.ecomdb.terms.update_one({"_id": ObjectId(id)}, {"$set": dict(terms)})
	return termsConditionEntity(conn.ecomdb.terms.find({"_id": ObjectId(id)}))

@settings.get("/siteimg/{img}", tags=["Settings"])
async def find_siteimg(img):
	return FileResponse("images/site/"+img)

@settings.post("/siteUpload", tags=["Settings"])
async def upload(files: List[UploadFile] = File(...)):
	for file in files:
		contents = await file.read()
		save_file("images/site/"+file.filename, contents)

	return {"Uploaded Filenames": [file.filename for file in files]}

def save_file(filename, data):
    with open(filename, 'wb') as f:
        f.write(data)

@settings.get("/banner", tags=["Banner"])
async def find_banner():
	return bannerConditionEntity(conn.ecomdb.banner.find({"status":"1"}))

@settings.get("/banner/{id}", tags=["Banner"])
async def find_banner(id):
	return bannerConditionEntity(conn.ecomdb.banner.find({"_id": ObjectId(id),"status":"1"}))

@settings.post('/banner', tags=["Banner"])
async def create_banner(banner:Banners):
	try:
		conn.ecomdb.banner.insert_one(dict(banner))
		return {"message:success"}
	except:
		return {"Error in Insert"}

@settings.put("/banner/{id}", tags=["Banner"])
async def update_banner(id,banner:Banners):
	conn.ecomdb.banner.update_one({"_id": ObjectId(id)}, {"$set": dict(banner)})
	return bannerConditionEntity(conn.ecomdb.banner.find({"_id": ObjectId(id)}))

@settings.get("/social", tags=["SocialLinks"])
async def find_social():
	return socialConditionEntity(conn.ecomdb.socialLink.find({}))

@settings.get("/social/{id}", tags=["SocialLinks"])
async def find_social_id(id):
	return socialConditionEntity(conn.ecomdb.socialLink.find({"_id": ObjectId(id),"status":"1"}))

@settings.get("/socialinactive", tags=["SocialLinks"])
async def find_inactive_social():
	return socialConditionEntity(conn.ecomdb.socialLink.find({"status":"0"}))

@settings.post('/social', tags=["SocialLinks"])
async def create_social(social:SocialLinks):
	try:
		conn.ecomdb.socialLink.insert_one(dict(social))
		return {"message:success"}
	except:
		return {"Error in Insert"}

@settings.put("/social/{id}", tags=["SocialLinks"])
async def update_social(id,social:SocialLinks):
	conn.ecomdb.socialLink.update_one({"_id": ObjectId(id)}, {"$set": dict(social)})
	return socialConditionEntity(conn.ecomdb.socialLink.find({"_id": ObjectId(id)}))


@settings.post('/contactus', tags=["ContactUS"])
async def create_contactus(contactus:Contactus):
	try:
		conn.ecomdb.contactus.insert_one(dict(contactus))
		template = """
		        <html>
		        <body>
				<p>Hi !!!
		        <br>Thanks for using fastapi mail, keep using it..!!!</p>
				</body>
		        </html>
		        """

		econf = ConnectionConfig(
			MAIL_USERNAME="vijaypsekar91@gmail.com",
			MAIL_PASSWORD="ekbystxkobrwcxlb",
			MAIL_FROM="vijaypsekar91@gmail.com",
			MAIL_PORT=587,
			MAIL_SERVER="smtp.gmail.com",
			MAIL_TLS=True,
			MAIL_SSL=False,
			USE_CREDENTIALS=True,
			VALIDATE_CERTS=True
		)

		message = MessageSchema(
			subject="Fastapi-Mail module",
			recipients=["vijaypsekar91@gmail.com"],  # List of recipients, as many as you can pass
			body=template,
			subtype="html"
		)

		fm = FastMail(econf)
		await fm.send_message(message)
		print("errorMEssAge : ", message)
		return {"message:success"}
	except Exception as e:
		print(e)
		return {"Error in Insert", e}

@settings.get("/contactus", tags=["ContactUS"])
async def find_contactus():
	return contactusConditionEntity(conn.ecomdb.contactus.find({"status":"1"}))


@settings.post('/settingPincode', tags=["Pincode"])
async def create_pincode(settingPincode:Pincode):
	try:
		conn.ecomdb.cashpincode.insert_one(dict(settingPincode))
		return {"message:success"}
	except:
		return {"Error in Insert"}

@settings.get("/settingValidpincode/{pincode}", tags=["Pincode"])
async def find_pincode(pincode):
	return pincodeConditionEntity(conn.ecomdb.cashpincode.find({"valid_pincode": pincode,"status":"1"}))

@settings.get("/settingPincode/{id}", tags=["Pincode"])
async def find_pincode(id):
	return pincodeConditionEntity(conn.ecomdb.cashpincode.find({"_id": ObjectId(id),"status":"1"}))

@settings.get("/settingPincode", tags=["Pincode"])
async def find_all_pincode():
	return pincodeConditionEntity(conn.ecomdb.cashpincode.find({"status":"1"}))

@settings.put("/settingPincode/{id}", tags=["Pincode"])
async def update_pincode(id,settingPincode:Pincode):
	conn.ecomdb.cashpincode.update_one({"_id": ObjectId(id)}, {"$set": dict(settingPincode)})
	return pincodeConditionEntity(conn.ecomdb.cashpincode.find({"_id": ObjectId(id)}))

@settings.post('/aboutimg', tags=["About Img"])
async def create_about_img(aboutimg:Aboutimg):
	try:
		conn.ecomdb.imgAbout.insert_one(dict(aboutimg))
		return {"message:success"}
	except:
		return {"Error in Insert"}


@settings.get("/aboutimg", tags=["About Img"])
async def find_all_abtimg():
	return abtimgConditionEntity(conn.ecomdb.imgAbout.find({}))

@settings.put("/aboutimg/{id}", tags=["About Img"])
async def update_abtimg(id,aboutimg:Aboutimg):
	conn.ecomdb.imgAbout.update_one({"_id": ObjectId(id)}, {"$set": dict(aboutimg)})
	return abtimgConditionEntity(conn.ecomdb.imgAbout.find({"_id": ObjectId(id)}))


@settings.post('/landingimg', tags=["Landing Img"])
async def create_landingimg(landingimg:Landingimg):
	try:
		conn.ecomdb.landingimg.insert_one(dict(Landingimg))
		return {"message:success"}
	except:
		return {"Error in Insert"}

@settings.get("/landingimg", tags=["Landing Img"])
async def find_landingimg():
	return landimgConditionEntity(conn.ecomdb.landingimg.find({}))

@settings.put("/landingimg/{id}", tags=["Landing Img"])
async def update_landimg(id,aboutimg:Landingimg):
	conn.ecomdb.landingimg.update_one({"_id": ObjectId(id)}, {"$set": dict(Landingimg)})
	return landimgConditionEntity(conn.ecomdb.landingimg.find({"_id": ObjectId(id)}))
