from fastapi import Query
from pydantic import BaseModel


class SchemaPart1Task2(BaseModel):
    total_details: int = None
    failed_details: int = None
    time_period: int = None


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


class SchemaPart3Task1(BaseModel):
    quantity: list[int]
    lambda_value: list[float]
    check_time_interval: list[int]


class SchemaPart3Task2(BaseModel):
    mtff: list[int]
    reliability_law: str


class SchemaPart3Task3(BaseModel):
    probabilities_of_non_failure: list[float]
    time_interval: int | float
    reliability_law: str


class SchemaPart3Task4(BaseModel):
    probabilities_of_non_failure: float
    quantity: int | float


class SchemaPart3Task6(BaseModel):
    probabilities_of_non_failure: list[float]
    time_interval: int | float
