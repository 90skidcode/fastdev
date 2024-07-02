from fastapi import APIRouter
from config.db import conn
from datetime import datetime
from bson.objectid import ObjectId
from models.reports import ReportSearch
from controllers.dashboard import dashboardController, OrderReportController, GraphReportController

dashboard = APIRouter()

@dashboard.get("/dashboardCard", tags=["Dashboard"])
async def find_card():
    return dashboardController()


reports = APIRouter()

@reports.post("/orderReport", tags=["Reports"])
async def find_order(orderReport:ReportSearch):
    return OrderReportController(orderReport)


@reports.post("/graphReport", tags=["Reports"])
async def find_graph():
    return GraphReportController()

