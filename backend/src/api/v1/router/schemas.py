from fastapi import Query
from pydantic import BaseModel


class SchemaPart1Task2(BaseModel):
    total_details: int = Query()
    failed_details: int = Query()
    time_period: int = Query()


class SchemaPart1Task4(BaseModel):
    quantity: int = Query()
    total_failures: int = Query()
    time_before: int = Query()
    end_time: int = Query()


class SchemaPart1Task5(BaseModel):
    failures: list[int] = Query()
    work_times: list[int] = Query()


class SchemaPart1Task6(BaseModel):
    failures: list[int] = Query()
    failure_time: list[int] = Query()


class SchemaPart1Task7(BaseModel):
    recovery_times: list[int | float]


class SchemaPart1Task8(BaseModel):
    avg_failure_time: int | float
    recovery_time: int | float


class SchemaPart2Task1(BaseModel):
    lambda_value: float
    check_time_intervals: list[int]


class GroupModel(BaseModel):
    failure_weight: float
    recovery_time: list[int]


class GroupsModel(BaseModel):
    group: GroupModel


class SchemaPart2Task2(BaseModel):
    total_failures: int
    groups: list[GroupsModel]
