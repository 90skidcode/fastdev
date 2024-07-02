from fastapi import APIRouter
from schemas.addtocart import listaddtocartEntity, listwhishlistEntity, listaddtocartProductEntity
from controllers.cartController import cartList, UpdateCartController, CartFinalQuery
from models.addtocart import Addtocart, Whishlist, Updatecart
from bson.objectid import ObjectId
from config.db import conn

atc = APIRouter()

@atc.get("/atc", tags=["Cart"])
async def find_all_atc():
    listval = listaddtocartProductEntity(cartList())
    #listval = listaddtocartEntity(conn.ecomdb.cart.find({"status":"1"}))
    if len(listval) == 0:
        return {"Empty"}
    else:
         return listaddtocartProductEntity(cartList())

@atc.post("/atcUpdate", tags=["Cart"])
async def update_atc(atcUpdate:Updatecart):
    return listaddtocartProductEntity(UpdateCartController(atcUpdate))


@atc.get("/wish", tags=["Wish"])
async def find_all_wish():
    whishval = listwhishlistEntity(conn.ecomdb.wish.find({"status":"1"}))
    if len(whishval) == 0:
        return {"Empty"}
    else:
         return listwhishlistEntity(conn.ecomdb.wish.find({"status":"1"}))

@atc.get("/atc/{id}", tags=["Cart"])
async def find_atc(id):
    #listval = listaddtocartEntity(conn.ecomdb.cart.find({"customer_id": id,"status":"1"}))
    return  listaddtocartProductEntity(CartFinalQuery(id))


@atc.get("/wish/{id}", tags=["Wish"])
async def find_wish(id):
    whishval = listwhishlistEntity(conn.ecomdb.wish.find({"customer_id": id,"status":"1"}))
    if len(whishval) == 0:
        return {"Empty"}
    else:
         return listwhishlistEntity(conn.ecomdb.wish.find({"customer_id": id,"status":"1"}))

@atc.post("/atc", tags=["Cart"])
async def create_cart(cart: Addtocart):
    try:
        conn.ecomdb.cart.insert_one(dict(cart))
        return {"Success"}
    except:
        return {"Error"}

@atc.post("/wish", tags=["Wish"])
async def create_wish(wish: Whishlist):
    try:
        conn.ecomdb.wish.insert_one(dict(wish))
        return {"Success"}
    except:
        return {"Error"}

@atc.put("/atc/{id}", tags=["Cart"])
async def update_cart(id,cart: Addtocart):
    conn.ecomdb.cart.update_one({"_id": ObjectId(id)}, {"$set": dict(cart)})
    return listaddtocartEntity(conn.ecomdb.cart.find({"_id": ObjectId(id)}))

@atc.put("/wish/{id}", tags=["Wish"])
async def update_wish(id,wish: Whishlist):
    conn.ecomdb.wish.update_one({"_id": ObjectId(id)}, {"$set": dict(wish)})
    return listwhishlistEntity(conn.ecomdb.wish.find({"_id": ObjectId(id)}))

@atc.delete("/atc/{id}", tags=["Cart"])
async def delete_cart(id):
    conn.ecomdb.cart.update_one({"_id": ObjectId(id)}, {"$set": {"status":"0"}})
    return listaddtocartEntity(conn.ecomdb.cart.find({"_id": ObjectId(id)}))

@atc.delete("/wish/{id}", tags=["Wish"])
async def delete_wish(id):
    conn.ecomdb.wish.update_one({"_id": ObjectId(id)}, {"$set": {"status":"0"}})
    return listwhishlistEntity(conn.ecomdb.wish.find({"_id": ObjectId(id)}))
