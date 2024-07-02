from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.user import user
from routes.products import products
from routes.branch import branch
from routes.franchise import franchise
from routes.category import category
from routes.customer import customers
from routes.order import order
from routes.settings import settings
from routes.addtocart import atc
from routes.dashboard import dashboard, reports
from routes.tags import tags
from routes.coupon import coupons

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
    "https://srivenkateswaraadmin.netlify.app",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user)
app.include_router(products)
app.include_router(branch)
app.include_router(franchise)
app.include_router(category)
app.include_router(customers)
app.include_router(order)
app.include_router(settings)
app.include_router(atc)
app.include_router(dashboard)
app.include_router(reports)
app.include_router(tags)
app.include_router(coupons)