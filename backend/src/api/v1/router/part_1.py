import json

import orjson
from fastapi import APIRouter, File
from fastapi import status
from fastapi.responses import ORJSONResponse

from tasks.part_1.solution_part_1 import task1, task2, task3, task4, task5, \
    task6, \
    task7, task8

part_1 = APIRouter()


@part_1.post("/part_1_task_1", response_class=ORJSONResponse)
async def part_1_task_1(file_bytes: bytes = File(), ) -> ORJSONResponse:
    result = task1(json.loads(file_bytes))

    return ORJSONResponse(content=result, status_code=status.HTTP_200_OK)


@part_1.post("/part_1_task_2", response_class=ORJSONResponse)
async def part_1_task_2(file_bytes: bytes = File(), ) -> ORJSONResponse:

    result = task2(json.loads(file_bytes))

    return ORJSONResponse(content=result, status_code=status.HTTP_200_OK)


@part_1.post("/part_1_task_3", response_class=ORJSONResponse)
async def part_1_task_3(file_bytes: bytes = File(), ) -> ORJSONResponse:
    result = task3(json.loads(file_bytes))

    return ORJSONResponse(content=result, status_code=status.HTTP_200_OK)


@part_1.post("/part_1_task_4", response_class=ORJSONResponse)
async def part_1_task_4(file_bytes: bytes = File(), ) -> ORJSONResponse:
    result = task4(json.loads(file_bytes))

    return ORJSONResponse(content=result, status_code=status.HTTP_200_OK)


@part_1.post("/part_1_task_5", response_class=ORJSONResponse)
async def part_1_task_5(file_bytes: bytes = File(), ) -> ORJSONResponse:
    result = task5(json.loads(file_bytes))

    return ORJSONResponse(content=result, status_code=status.HTTP_200_OK)


@part_1.post("/part_1_task_6", description="Task 6",
             response_class=ORJSONResponse)
async def part_1_task_6(file_bytes: bytes = File(), ) -> ORJSONResponse:
    result = task6(json.loads(file_bytes))

    return ORJSONResponse(content=result, status_code=status.HTTP_200_OK)


@part_1.post("/part_1_task_7", description="Task 7",
             response_class=ORJSONResponse)
async def part_1_task_6(file_bytes: bytes = File(), ) -> ORJSONResponse:
    result = task7(json.loads(file_bytes))

    return ORJSONResponse(content=result, status_code=status.HTTP_200_OK)


@part_1.post("/part_1_task_8", description="Task 8",
             response_class=ORJSONResponse)
async def part_1_task_6(file_bytes: bytes = File(), ) -> ORJSONResponse:
    result = task8(json.loads(file_bytes))

    return ORJSONResponse(content=result, status_code=status.HTTP_200_OK)
