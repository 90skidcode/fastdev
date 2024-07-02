from config.db import conn
from bson.objectid import ObjectId

def orderCheck(order_id):
    res = conn.ecomdb.order.aggregate([
        {
            '$lookup': {
                'from': "customer",
                'localField': "customer_id",
                'foreignField': "customer_no",
                'as': "customer_info"
            }
        },
        {
            '$match':{'$and':[{"order_id":order_id}]}
        }
    ])

    return res

def orderCustomer(customer_id):
    res = conn.ecomdb.order.aggregate([
        {
            '$lookup': {
                'from': "customer",
                'localField': "customer_id",
                'foreignField': "customer_no",
                'as': "customer_info"
            }
        },
        {
            '$match':{'$and':[{"customer_id":customer_id}]}
        }
    ])

    return res