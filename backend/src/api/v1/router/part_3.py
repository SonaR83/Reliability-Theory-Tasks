import json

from fastapi import APIRouter, File
from fastapi import status
from fastapi.responses import ORJSONResponse

from tasks.part_3.solution_part_3 import (task1, task2, task3, task4, task5,
                                          task6, task7, task8)

# from tasks.part_3.solution_part_3 import task1

part_3 = APIRouter()


@part_3.post("/part_3_task_1", response_class=ORJSONResponse)
async def part_3_task_1(file_bytes: bytes = File(), ) -> ORJSONResponse:
    result = task1(json.loads(file_bytes))

    return ORJSONResponse(content=result, status_code=status.HTTP_200_OK)


@part_3.post("/part_3_task_2", response_class=ORJSONResponse)
async def part_3_task_2(file_bytes: bytes = File(), ) -> ORJSONResponse:
    result = task2(json.loads(file_bytes))

    return ORJSONResponse(content=result, status_code=status.HTTP_200_OK)


@part_3.post("/part_3_task_3", response_class=ORJSONResponse)
async def part_3_task_3(file_bytes: bytes = File(), ) -> ORJSONResponse:
    result = task3(json.loads(file_bytes))

    return ORJSONResponse(content=result, status_code=status.HTTP_200_OK)


@part_3.post("/part_3_task_4", response_class=ORJSONResponse)
async def part_3_task_4(file_bytes: bytes = File(), ) -> ORJSONResponse:
    result = task4(json.loads(file_bytes))

    return ORJSONResponse(content=result, status_code=status.HTTP_200_OK)

@part_3.post("/part_3_task_5", response_class=ORJSONResponse)
async def part_3_task_5(file_bytes: bytes = File(), ) -> ORJSONResponse:
    result = task5(json.loads(file_bytes))

    return ORJSONResponse(content=result, status_code=status.HTTP_200_OK)


@part_3.post("/part_3_task_6", response_class=ORJSONResponse)
async def part_3_task_6(file_bytes: bytes = File(), ) -> ORJSONResponse:
    result = task6(json.loads(file_bytes))

    return ORJSONResponse(content=result, status_code=status.HTTP_200_OK)


@part_3.post("/part_3_task_7", response_class=ORJSONResponse)
async def part_3_task_7(file_bytes: bytes = File(), ) -> ORJSONResponse:
    result = task7(json.loads(file_bytes))

    return ORJSONResponse(content=result, status_code=status.HTTP_200_OK)

@part_3.post("/part_3_task_8", response_class=ORJSONResponse)
async def part_3_task_8(file_bytes: bytes = File(), ) -> ORJSONResponse:
    result = task8(json.loads(file_bytes))

    return ORJSONResponse(content=result, status_code=status.HTTP_200_OK)