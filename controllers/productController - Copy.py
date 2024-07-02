from config.db import conn
from schemas.products import productlookupEntity,productjoinEntity
import json
from bson import ObjectId, json_util
from fastapi.responses import JSONResponse

def productCheck(product_code):
    res = conn.ecomdb.product.aggregate([
        {
            '$lookup':{
                'from': "category",
                'localField': "category_id",
                'foreignField': "category_no",
                'as': "category_info"
            }
        },
        {
            '$match': {'$and': [{"product_code": product_code}]}
        }
    ])
    return res

def productallCheck():
    res = conn.ecomdb.product.aggregate([
        {
            '$lookup':{
                'from': "category",
                'localField': "category_id",
                'foreignField': "category_no",
                'as': "category_info"
            }
        }
    ])
    return res


def productCatCheck(category_id):
    res = conn.ecomdb.product.aggregate([
        {
            '$lookup':{
                'from': "category",
                'localField': "category_id",
                'foreignField': "category_no",
                'as': "category_info"
            }
        },
        {
            '$match': {"category_id": {"$in" : category_id }}
        }
    ])
    return res

def productAttCheck():
    res = conn.ecomdb.product.find({"status": "1"})
    for resval in res:
        if isinstance(resval['attribute_id'], list) == True:
            for attributeVal in resval['attribute_id']:
                select_attr= conn.ecomdb.attribute.find_one({"att_id": attributeVal['att_id']},{"att_name":1,"status":1})
                att_name = select_attr['att_name']
                attributeVal['att_value'] = att_name

    return res




