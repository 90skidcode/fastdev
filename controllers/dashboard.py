from config.db import conn
from bson.objectid import ObjectId
from datetime import datetime
import dateutil.parser
from schemas.order import ordersEntity


def dashboardController():
    #Customer Card
    customer_count = conn.ecomdb.customer.count_documents({"status":"1"})
    #Order Card
    order_count = conn.ecomdb.order.count_documents({"status": "1"})
    #Category Card
    category_count = conn.ecomdb.category.count_documents({"status": "1"})
    #Product Card
    product_count = conn.ecomdb.product.count_documents({"status": "1"})
    #Branch Card
    branch_count = conn.ecomdb.branch.count_documents({"status": "1"})
    # Franchise Card
    franchise_count = conn.ecomdb.franchise.count_documents({"status": "1"})
    # Revenue Card
    revenue_query = conn.ecomdb.order.find({"status": "1"},{"order_amount":1})
    revenue_list=[]
    for rev_val in revenue_query:
        revenue_list.append(float(rev_val['order_amount']))
    revenue_count =round(sum(revenue_list))


    return {"RevenueCard":revenue_count,"CustomerCard":customer_count,"OrderCard":order_count,"CategoryCard":category_count,"ProductCard":product_count,"BranchCard":branch_count,"FranchiseCard":franchise_count}


def GraphReportController():

    f_d = "2022-05-24T13:24:53.929Z"
    order_count = conn.ecomdb.order.find({"created_at": { "$gte": f_d },"status": "1"},{"created_at":1})

    print(order_count)
    for od in order_count:
        print(od)

def OrderReportController(orderReport):
    OrderReport_dict = dict(orderReport)
    if OrderReport_dict:
        if OrderReport_dict['from_date'] != "" and OrderReport_dict['to_date'] == "":
            order_count = conn.ecomdb.order.find({"created_at": {
                "$gte": OrderReport_dict['from_date']
            }})
        elif OrderReport_dict['from_date'] != "" and OrderReport_dict['to_date'] != "":
                order_count = conn.ecomdb.order.find({"created_at": {
                    "$lte": OrderReport_dict['to_date']
                }})
        elif OrderReport_dict['from_date'] != "" and OrderReport_dict['to_date'] != "":
                order_count = conn.ecomdb.order.find({"created_at": {
                    "$gte": OrderReport_dict['from_date'],
                    "$lte": OrderReport_dict['to_date']
                }})
        else:
            order_count = conn.ecomdb.order.find({"status":"1"})

        return {"status_code":"200","result":ordersEntity(order_count)}
    else:
        return {"status_code": "201", "result": "Invalid Entry"}

    return "done"
