from fastapi import APIRouter, File, UploadFile
from controllers.productController import productCheck, productallCheck, productCatCheck, productAttCheck
from models.products import Product, ProductCat
from schemas.products import productEntity, productsEntity, productlookupEntity, productjoinEntity
from config.db import conn
from fastapi.responses import JSONResponse, FileResponse
from typing import List
from datetime import datetime
from bson.objectid import ObjectId

products = APIRouter()

@products.get('/product/{productCode}', tags=["Product"])
async def find_product(productCode):
	prod_val = productCheck(productCode)
	return productjoinEntity(prod_val)

@products.post('/productCategory', tags=["Product"])
async def find_product_category(productCategory:ProductCat):
	cat_val = dict(productCategory)
	cat_id = cat_val['category_id']
	prod_val = productCatCheck(cat_id)
	return productjoinEntity(prod_val)

@products.get("/productcat", tags=["Product"])
async def find_all_products():
	return productjoinEntity(productallCheck())

@products.get("/product", tags=["Product"])
async def find_all_prod():
	return productAttCheck()

@products.get("/visibleproducts", tags=["Product"])
async def find_visible_products():
	return productsEntity(conn.ecomdb.product.find({"status":"1","visible":"V"}))

@products.post("/tagwiseproducts/{tags}", tags=["Product"])
async def find_tag_products(tags):
	tags_value = tags.split(',')
	return productsEntity(conn.ecomdb.product.find({"status":"1","visible":"V","tags":{"$in":tags_value}}))

@products.put("/product/{productCode}/{v_status}", tags=["Product"])
async def update_visible(productCode,v_status):
	conn.ecomdb.product.update_one({"product_code": productCode}, {"$set": {"visible": v_status}})
	return productsEntity(conn.ecomdb.product.find({"product_code": productCode}))

@products.put("/product/{productCode}", tags=["Product"])
async def update_product(productCode,product:Product):
	conn.ecomdb.product.update_one({"product_code": productCode}, {"$set": dict(product)})
	return productsEntity(conn.ecomdb.product.find({"product_code": productCode}))

@products.get("/productimg/{img}", tags=["Product"])
async def find_productImg(img):
	return FileResponse("images/products/"+img)

@products.post("/upload", tags=["Product"])
async def upload(files: List[UploadFile] = File(...)):
	for file in files:
		contents = await file.read()
		save_file("images/products/"+file.filename, contents)

	return {"Uploaded Filenames": [file.filename for file in files]}

def save_file(filename, data):
    with open(filename, 'wb') as f:
        f.write(data)


@products.post('/product', tags=["Product"])
async def create_product(product:Product):
	try:
		prod_val = dict(product)
		incr_val = conn.ecomdb.product.count_documents({})
		if incr_val != 0:
			incr_new_val = 1001 + incr_val
			incr_id = "PROD" + str(incr_new_val)
		else:
			incr_id = "PROD1001"

		prod_val['product_code'] = incr_id
		conn.ecomdb.product.insert_one(prod_val)
		return {"message:success"}
	except:
		return {"Error in Insert"}

@products.delete("/product/{productCode}", tags=["Product"])
async def delete_product(productCode):
	conn.ecomdb.product.update_one({"product_code": productCode}, {"$set": {"status":"0"}})
	return productsEntity(conn.ecomdb.product.find({"product_code": productCode}))