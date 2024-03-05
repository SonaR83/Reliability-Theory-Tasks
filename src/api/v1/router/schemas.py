from fastapi import Query
from pydantic import BaseModel





class SchemaTask2(BaseModel):
    total_details: int = Query()
    failed_details_in_time_period: list[dict[str, int]]
    time_period: int = Query()
