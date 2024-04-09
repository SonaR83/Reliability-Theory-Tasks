import numpy as np

from api.v1.router.schemas import (SchemaPart3Task1, SchemaPart3Task2,
                                   SchemaPart3Task3, SchemaPart3Task4,
                                   SchemaPart3Task6, SchemaPart3Task8,
                                   ProbabilityLaw)


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


def task7(data: dict) -> dict:
    # task = SchemaPart3Task3(**data)
    elements = data.get("elements", [])
    time_interval = data.get("time_interval")

    failure_rates = [elem.get('failure_rate', 0) * elem.get('quantity', 0)
                     for elem in elements]
    failure_rate_sys = sum(failure_rates)
    probability_elem = np.exp(-failure_rate_sys * time_interval)

    return {"failure rate system":
                f"{np.format_float_scientific(failure_rate_sys)}",
            "probability": f"{probability_elem}",
            "average time to first failure": f"{1 / sum(failure_rates)}"}


def task8(data: dict) -> dict:
    # task = SchemaPart3Task8(**data)
    groups = data.get("groups", [])
    validated_data = [SchemaPart3Task8(**part)
                      for part in groups]
    probabilities = []
    for val_data in validated_data:
        match val_data.law:
            case ProbabilityLaw.EXPONENTIAL:
                time_interval = data.get("time_interval")
                probability = np.exp(-val_data.failure_rate * time_interval)

                probabilities.append(probability)

            case ProbabilityLaw.RELAY:
                time_interval = data.get("time_interval")
                probability = np.exp(
                    -(time_interval ** 2) / (2 * val_data.theta ** 2))

                probabilities.append(probability)

            case ProbabilityLaw.WEIBULL:
                time_interval = data.get("time_interval")
                multiplier_1 = val_data.failure_rate * (
                        time_interval ** val_data.k)

                probability = np.exp(-multiplier_1)

                probabilities.append(probability)

    print(probabilities)
    p_sys = np.prod(probabilities)

    return {"probability sys": f"{p_sys}"}

# def task___(data: dict) -> dict:
#     task = SchemaPart3Task3(**data)
#     return {"status": "success"}
