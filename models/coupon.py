from pydantic import BaseModel

class Coupon(BaseModel):
    cc:str
    sd:str
    ed:str
    det_type:str
    description: str
    value:str
    cnt:str
    user_cnt:str
    min_val:str
    limit:str
    status:str
    created_at:str

class Validate_model(BaseModel):
    cc:str
    amt:str
    customer_no:str

