from pydantic import BaseModel

class ReportSearch(BaseModel):
	from_date:str
	to_date:str
