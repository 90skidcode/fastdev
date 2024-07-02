from pydantic import BaseModel

class Order(BaseModel):
    customer_id: str
    product_id: str
    delivery_address: str
    payment_mode: str
    order_amount: str
    delivery_status: str
    order_status: str
    cc: str
    difference: str
    online_transaction_id: str
    status: str
    created_at: str


class Updatestatus(BaseModel):
    delivery_status: str
    order_status: str
