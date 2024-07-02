from config.db import conn
from bson.objectid import ObjectId
from schemas.addtocart import listaddtocartProductEntity, listaddtocartEntity
import datetime

def cartList():
    res = conn.ecomdb.cart.aggregate([
        {
            '$lookup': {
                'from': "product",
                'localField': "product_code",
                'foreignField': "product_code",
                'as': "product_info"
            }
        }
    ])

    return res

def CartFinalQuery(customer_id):
    res = conn.ecomdb.cart.aggregate([
        {
            '$lookup': {
                'from': "product",
                'localField': "product_code",
                'foreignField': "product_code",
                'as': "product_info"
            }
        },
        {
            '$match':{'$and':[{"customer_id":customer_id,"status": "1"}]}
        }
    ])
    return res

def UpdateCartController(atcUpdate):
    actupdate_dict = dict(atcUpdate)
    if actupdate_dict:
        customer_id = actupdate_dict['customer_id']
        product_code = actupdate_dict['product_code']
        attribute_id = actupdate_dict['attribute_id']
        check_cart = listaddtocartEntity(conn.ecomdb.cart.find({"attribute_id":attribute_id,"product_code":product_code,"customer_id":customer_id,"status": "1"}))
        if len(check_cart) ==0:
            insert_cart = {}
            insert_cart['customer_id'] = customer_id
            insert_cart['product_code'] = product_code
            insert_cart['attribute_id'] = attribute_id
            insert_cart['quantity'] = 1
            insert_cart['status'] = "1"
            insert_cart['created_at'] = datetime.datetime.today()
            conn.ecomdb.cart.insert_one(insert_cart)

            return CartFinalQuery(customer_id)
        else:
            if actupdate_dict['quantitystatus'] == 'Inc':
                conn.ecomdb.cart.update_one({"attribute_id":attribute_id,"product_code":product_code,"customer_id":customer_id,"status": "1"}, { '$inc': {"quantity": +1}})
            else:
                conn.ecomdb.cart.update_one({"attribute_id":attribute_id,"product_code":product_code,"customer_id":customer_id,"status": "1"}, {'$inc': {"quantity": -1}})

            return CartFinalQuery(customer_id)
