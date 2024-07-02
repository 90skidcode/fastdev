from config.db import conn
import json
from bson import ObjectId, json_util
from fastapi.responses import JSONResponse
from datetime import datetime
import pytz

def validate_coupon(validate_val):
    current_date = datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%Y-%m-%dT%H:%M:%S%z')
    dict_val = dict(validate_val)
    valid_cc = conn.ecomdb.coupon.find_one({"status":"1","cc":dict_val['cc']})
    results = list(valid_cc)
    if len(results) == 0:
        final_val = {"status_code":"400","message": "Minimum Value"}
    else:
        print("Cursor is Not Empty")
        print("Start Date",valid_cc['sd'])
        user_coupon_check = conn.ecomdb.user_coupon.count_documents({"cc": dict_val['cc'], "customer_no": dict_val['customer_no']})
        print("user_coupon_check",user_coupon_check)
        if user_coupon_check == 0 or int(valid_cc['user_cnt']) > user_coupon_check :
            if valid_cc['min_val'] == '0' or int(valid_cc['min_val']) <= int(dict_val['amt']):
                if valid_cc['sd'] <= current_date and valid_cc['ed'] >= current_date:
                    if valid_cc['limit']=='0' or int(valid_cc['cnt']) <= int(valid_cc['limit']):
                        insert_user_coupon = {}
                        if valid_cc['det_type'] == 'flat':
                            print("Amount",dict_val['amt'])
                            f_val = int(dict_val['amt']) - int(valid_cc['value'])
                            #Insert Usercoupon
                            '''insert_user_coupon['customer_no'] = dict_val['customer_no']
                            insert_user_coupon['cc'] = dict_val['cc']
                            insert_user_coupon['discount_amt'] = int(valid_cc['value'])
                            conn.ecomdb.user_coupon.insert_one(insert_user_coupon)
                            inc_count = int(valid_cc['cnt']) + 1
                            conn.ecomdb.coupon.update_one({"cc": dict_val['cc']},
                                                         {'$set': {"cnt": inc_count}})'''
                            final_val = {"status_code":"200","message":"Success","amount": f_val,"difference":valid_cc['value']}
                        elif  valid_cc['det_type'] == 'percentage':
                            f_val = int(dict_val['amt']) - (int(dict_val['amt']) * int(valid_cc['value']) / 100)
                            diff_val = (int(dict_val['amt']) * int(valid_cc['value']) / 100)
                            '''insert_user_coupon['customer_no'] = dict_val['customer_no']
                            insert_user_coupon['cc'] = dict_val['cc']
                            insert_user_coupon['discount_amt'] = diff_val
                            conn.ecomdb.user_coupon.insert_one(insert_user_coupon)
                            inc_count = int(valid_cc['cnt']) + 1
                            conn.ecomdb.coupon.update_one({"cc": dict_val['cc']},
                                                          {'$set': {"cnt": inc_count}})'''
                            final_val = {"status_code":"200","message":"Success","amount": f_val, "difference":str(diff_val)}
                        else:
                            final_val = {"status_code":"400","message":"Invalid API"}
                    else:
                        final_val = {"status_code":"400","message":"Coupon limit exceeds"}
                else:
                    final_val = {"status_code":"400","message": "Coupon Expired"}
            else:
                final_val = {"status_code":"400","message": "Minimum Value"}
        else:
            final_val = {"status_code":"400","message": "Coupon Already Used"}

    return final_val