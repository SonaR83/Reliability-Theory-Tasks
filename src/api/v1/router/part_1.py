import json

from fastapi import APIRouter, Query, File
from fastapi import status
from fastapi.responses import ORJSONResponse

from tasks.part_1.solution import task1, task2, task3, task4, task5, task6

p1t1 = APIRouter()


@p1t1.post("/task_1", response_class=ORJSONResponse)
async def part_1_task_1(file_bytes: bytes = File(), ) -> ORJSONResponse:
    result = task1(json.loads(file_bytes))

    return ORJSONResponse(content=result, status_code=status.HTTP_200_OK)


@p1t1.post("/task_2", response_class=ORJSONResponse)
async def part_1_task_2(file_bytes: bytes = File(), ) -> ORJSONResponse:
    result = task2(json.loads(file_bytes))

    return ORJSONResponse(content=result, status_code=status.HTTP_200_OK)


@p1t1.post("/task_3", response_class=ORJSONResponse)
async def part_1_task_3(file_bytes: bytes = File(), ) -> ORJSONResponse:
    result = task3(json.loads(file_bytes))

    return ORJSONResponse(content=result, status_code=status.HTTP_200_OK)


@p1t1.post("/task_4", response_class=ORJSONResponse)
async def part_1_task_4(file_bytes: bytes = File(), ) -> ORJSONResponse:
    result = task4(json.loads(file_bytes))

    return ORJSONResponse(content=result, status_code=status.HTTP_200_OK)


@p1t1.post("/task_5", response_class=ORJSONResponse)
async def part_1_task_5(file_bytes: bytes = File(), ) -> ORJSONResponse:
    result = task5(json.loads(file_bytes))

    return ORJSONResponse(content=result, status_code=status.HTTP_200_OK)


@p1t1.post("/task_6", description="Task 6", response_class=ORJSONResponse)
async def part_1_task_6(file_bytes: bytes = File(), ) -> ORJSONResponse:
    result = task6(json.loads(file_bytes))

    return ORJSONResponse(content=result, status_code=status.HTTP_200_OK)
