import numpy as np

from api.v1.router.schemas import SchemaPart2Task1, SchemaPart2Task2, \
    GroupsModel, GroupModel


def task1(data: dict) -> dict:
    print("it works")
    task = SchemaPart2Task1(**data)

    lambda_value = float(np.format_float_scientific(task.lambda_value))
    probabilities = [np.round(np.exp(-lambda_value * time), 3) for time in
                     task.check_time_intervals]

    failure_frequencies = [
        np.format_float_scientific(
            lambda_value * np.exp(-lambda_value * time), precision=3)
        for time in task.check_time_intervals]

    return {"probability of failure-free operation": f"{probabilities}",
            "failure frequency": f"{failure_frequencies}",
            "mean time to failure": f"{np.reciprocal(lambda_value)}"}


def task2(data: dict) -> dict:
    task = SchemaPart2Task2(**data)
    results = []
    failure_weights = []
    for task_groups in task.groups:
        groups = GroupsModel(**task_groups.model_dump())
        group = GroupModel(**groups.group.model_dump())

        result = sum(group.recovery_time) / len(
            group.recovery_time) * group.failure_weight
        failure_weights.append(group.failure_weight)
        results.append(result)

    return {"avg system recovery time": f"{sum(results)}",
            f"check_weights": f"{sum(failure_weights)}"}
