import json

from fastapi import APIRouter, File
from fastapi import status
from fastapi.responses import ORJSONResponse

from tasks.part_2.solution_part_2 import task1, task2

part_2 = APIRouter()


@part_2.post("/part_2_task_1", response_class=ORJSONResponse)
async def part_2_task_1(file_bytes: bytes = File(), ) -> ORJSONResponse:
    result = task1(json.loads(file_bytes))

    return ORJSONResponse(content=result, status_code=status.HTTP_200_OK)


@part_2.post("/part_2_task_2", response_class=ORJSONResponse)
async def part_2_task_2(file_bytes: bytes = File(), ) -> ORJSONResponse:
    result = task2(json.loads(file_bytes))

    return ORJSONResponse(content=result, status_code=status.HTTP_200_OK)
