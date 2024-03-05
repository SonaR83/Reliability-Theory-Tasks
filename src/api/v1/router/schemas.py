from fastapi import Query
from pydantic import BaseModel


class SchemaTask2(BaseModel):
    total_details: int = Query()
    failed_details: int = Query()
    time_period: int = Query()


class SchemaTask4(BaseModel):
    quantity: int = Query()
    total_failures: int = Query()
    time_before: int = Query()
    end_time: int = Query()


class SchemaTask5(BaseModel):
    failures: list[int] = Query()
    work_times: list[int] = Query()


class SchemaTask6(BaseModel):
    failures: list[int] = Query()
    failure_time: list[int] = Query()
