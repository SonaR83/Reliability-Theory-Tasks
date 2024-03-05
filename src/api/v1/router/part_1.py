import json

from fastapi import APIRouter, Query, UploadFile, File
from fastapi.responses import ORJSONResponse
from fastapi.requests import  Request
from fastapi import status

from api.v1.router.schemas import SchemaTask2
from tasks.part_1.solution import task1, task2, task3

p1t1 = APIRouter()


@p1t1.post("/task_1", response_class=ORJSONResponse)
async def p1t1_solution(
        total_details: int = Query(),
        failed_details: int = Query(),
        time_period: int = Query()) -> ORJSONResponse:
    result = task1(total_details, failed_details, time_period)
    return ORJSONResponse(content=result, status_code=status.HTTP_200_OK)


@p1t1.post("/task_2", response_class=ORJSONResponse)
async def p1t2_solution(file_bytes: bytes = File(),) -> ORJSONResponse:
    result = task2(json.loads(file_bytes))

    return ORJSONResponse(content=result, status_code=status.HTTP_200_OK)


@p1t1.post("/task_3", response_class=ORJSONResponse)
async def p1t2_solution(file_bytes: bytes = File(),) -> ORJSONResponse:
    result = task3(json.loads(file_bytes))

    return ORJSONResponse(content=result, status_code=status.HTTP_200_OK)