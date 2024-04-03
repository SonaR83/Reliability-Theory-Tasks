import numpy as np

from api.v1.router.schemas import (SchemaPart3Task1, SchemaPart3Task2,
                                   SchemaPart3Task3, SchemaPart3Task4,
                                   SchemaPart3Task6)


def task1(data: dict) -> dict:
    print("it works")

    task = SchemaPart3Task1(**data)

    lambda_sys = sum(
        [val * task.lambda_value[count] for count, val in
         enumerate(task.quantity)])
    lambda_sys_str = np.format_float_scientific(lambda_sys)
    probabilities = [np.exp(-lambda_sys * time) for time in
                     task.check_time_interval]
    probabilities_str = [
        float(np.format_float_scientific(probabilitiy, precision=2))
        for probabilitiy in probabilities]

    # Mean time between failures
    mbtf = 1 / lambda_sys

    return {"lambda_sys": f"{lambda_sys_str}",
            "probabilities": f"{probabilities_str}",
            "mean time between failures": f"{mbtf}"}


def task2(data: dict) -> dict:
    # mean time to first failure
    task = SchemaPart3Task2(**data)
    lambda_sys = sum([1 / mtff for mtff in task.mtff])
    mtff_sys = 1 / lambda_sys

    return {"lamba_sys": f"{lambda_sys}",
            "mtff_sys": f"{mtff_sys}"}


def task3(data: dict) -> dict:
    task = SchemaPart3Task3(**data)
    probability_syst = np.prod(task.probabilities_of_non_failure)
    lambda_sys = (-1 / task.time_interval) * np.log(probability_syst)

    mtff_syst = (1 / lambda_sys)

    return {"probability_syst": f"{probability_syst}",
            "lambda_sys": f"{np.format_float_scientific(lambda_sys)}",
            "mtff_syst": f"{mtff_syst}"
            }


def task4(data: dict) -> dict:
    task = SchemaPart3Task4(**data)
    probability_syst_1 = pow(task.probabilities_of_non_failure, task.quantity)
    probability_syst_2 = 1 - task.quantity * (
            1 - task.probabilities_of_non_failure)
    print(f"probability_syst_1: {probability_syst_1}")
    print(f"probability_syst_2: {probability_syst_2}")

    return {f"probability_syst_1": f"{probability_syst_1}",
            f"probability_syst_2": f"{probability_syst_2}"}


def task5(data: dict) -> dict:
    task = SchemaPart3Task4(**data)
    probability_elem = 1 - (
                (1 - task.probabilities_of_non_failure) / task.quantity)
    return {"P_elem": f"{probability_elem}"}


def task6(data: dict) -> dict:
    task = SchemaPart3Task6(**data)
    p_sys = 1 - sum(
        [1 - p_elem for p_elem in task.probabilities_of_non_failure])

    lambda_syst = (1 - p_sys) / task.time_interval
    alpha_syst = lambda_syst * (1 - lambda_syst)
    return {"P_sys": f"{p_sys}",
            "lambda_syst": f"{lambda_syst}",
            "alpha_syst": f"{alpha_syst}"
            }
# def task___(data: dict) -> dict:
#     task = SchemaPart3Task3(**data)
#     return {"status": "success"}
