from fastapi import APIRouter, File, UploadFile
from models.customer import Customer, CustomerLogin, CustomerAddress
from schemas.customer import customerEntity, customersEntity, customersLoginEN, customersAddEntity
from config.db import conn
from config.mobileApi import MobileSMS
from fastapi.responses import JSONResponse, FileResponse
from typing import List
from datetime import datetime
from bson.objectid import ObjectId
import random

customers = APIRouter()

@customers.get("/customer", tags=["Customer"])
async def find_all_customer():
	return customersEntity(conn.ecomdb.customer.find({"status":"1"}))

@customers.get("/customer/{id}", tags=["Customer"])
async def find_customer(id):
	return customersEntity(conn.ecomdb.customer.find({"_id": ObjectId(id),"status":"1"}))

@customers.get("/custLogin", tags=["Login"])
async def send_login_otp(phone_number):
    if len(phone_number) == 10:
        mobileotp = random.randint(1111, 9999)
        check_phone = customersLoginEN(conn.ecomdb.customer_login.find({"customer_phone": phone_number}))
        if len(check_phone) != 0:
            conn.ecomdb.customer_login.delete_one({"customer_phone": phone_number})
            result_sms =MobileSMS('NDQ0ODYzNjY2YzY5NTQ1NTM3NmQ1MTZhNDk0YjZhNTg=', "91"+phone_number+"", "SRIVKT", "Dear Customer, Use OTP "+str(mobileotp)+" to login to your Sri Venkateshwara Classic Account.")
            print("Here", result_sms)
            conn.ecomdb.customer_login.insert_one({"customer_phone": phone_number, "otp": str(mobileotp)})

            return {"status_code": "200", "Message": "OTP Send to mobile"}
        else:
            conn.ecomdb.customer_login.insert_one({"customer_phone": phone_number, "otp": str(mobileotp)})
            result_sms =MobileSMS('NDQ0ODYzNjY2YzY5NTQ1NTM3NmQ1MTZhNDk0YjZhNTg=', "91"+phone_number+"", "SRIVKT", "Dear Customer, Use OTP "+str(mobileotp)+" to login to your Sri Venkateshwara Classic Account.")
            print("Here1", result_sms)
            return {"status_code": "200", "Message": "OTP Send to mobile"}
    else:
        return {"status_code": "201", "Message": "Invalid Phone Number"}


@customers.post("/custLogin", tags=["Login"])
async def check_otp(custLogin:CustomerLogin):
    loginval = customersLoginEN(conn.ecomdb.customer_login.find(dict(custLogin)))
    if len(loginval) != 0:
        for login_phone in loginval:
            customer_phone = login_phone['customer_phone']

        check_cust = customersEntity(conn.ecomdb.customer.find({"customer_phone": customer_phone, "status": "1"}))
        if len(check_cust) == 0:
            customer_val={}
            customer_val['customer_fname']= customer_val['customer_lname']= customer_val['customer_phone']= customer_val['customer_email']= customer_val['customer_joining']= customer_val['customer_joining']= customer_val['customer_img']=''
            incr_val = conn.ecomdb.customer.count_documents({})
            if incr_val != 0:
                incr_new_val = 10001 + incr_val
                incr_id = "CUS" + str(incr_new_val)
            else:
                incr_id = "CUS10001"

            customer_val['customer_no'] = incr_id
            customer_val['customer_phone'] = customer_phone
            customer_val['status'] = "1"
            customer_val['created_at'] = "05-02-2022"
            conn.ecomdb.customer.insert_one(customer_val)
            conn.ecomdb.customer_login.delete_many({"customer_phone": customer_phone})
            return {"status_code": "200", "Message": customersEntity(conn.ecomdb.customer.find({"customer_no": incr_id,"status": "1"}))}
            #return {"Success"}
        else:
            conn.ecomdb.customer_login.delete_many({"customer_phone": customer_phone})
            return {"status_code": "200", "Message":check_cust}
    else:
        return {"status_code": "201","Message":"Invalid OTP"}

@customers.post("/customer", tags=["Customer"])
async def create_user(customer: Customer):
    try:
        customer_val = dict(customer)
        incr_val = conn.ecomdb.customer.count_documents({})
        if incr_val != 0:
            incr_new_val = 10001 + incr_val
            incr_id = "CUS" + str(incr_new_val)
        else:
            incr_id = "CUS10001"

        customer_val['customer_no'] = incr_id
        conn.ecomdb.customer.insert_one(customer_val)
        return {"message:success"}
    except:
        return {"Error in Insert"}

@customers.put("/customer/{id}", tags=["Customer"])
async def update_user(id,customer: Customer):
    conn.ecomdb.customer.update_one({"_id": ObjectId(id)}, {"$set": dict(customer)})
    return customersEntity(conn.ecomdb.customer.find({"_id": ObjectId(id)}))

@customers.delete("/customer/{id}", tags=["Customer"])
async def delete_user(id):
    conn.ecomdb.customer.update_one({"_id": ObjectId(id)}, {"$set": {"status":"0"}})
    return customersEntity(conn.ecomdb.customer.find({"_id": ObjectId(id)}))


'''Delivery Address'''

@customers.get("/customerAddress/{customer_no}", tags=["Delivery Address"])
async def find_delivery_address(customer_no):
    return customersAddEntity(conn.ecomdb.customer_address.find({"customer_no": customer_no,"status":"1"}))

@customers.post("/customerAddress/", tags=["Delivery Address"])
async def create_user(customerAddress: CustomerAddress):
    try:
        conn.ecomdb.customer_address.insert_one(dict(customerAddress))
        return {"message:success"}
    except:
        return {"Error in Insert"}



