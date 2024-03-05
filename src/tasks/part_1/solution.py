import numpy as np


def task1(total_details, failed_details, time_period) -> dict:
    reliability_probability = (total_details - failed_details) / total_details
    failure_probability = failed_details / total_details

    return {f"P({time_period})": str(reliability_probability),
            f"Q({time_period})": str(failure_probability)}


def task2(data: dict) -> dict:
    def calc_failure_frequency(faulured_details, initial_details, period):
        print(f'{faulured_details=}, '
              f'{initial_details=},'
              f'{period=}')
        return np.format_float_scientific(
            faulured_details / (initial_details * period), precision=2)

    def calc_failure_rate(faulured_details, avg_worksfine_details, period):
        return np.format_float_scientific(
            faulured_details / (avg_worksfine_details * period), precision=1)

    def calc_average_worksfine_details_on_period(
            on_begin_details: int,
            failed_period: dict):
        # число исправно работяющих изделий к концу крайнего интервала времени
        for failed_periods, count_failed in failed_period.items():
            on_begin_details -= count_failed
            avg_work_fines_details_in_period.append(on_begin_details)

        # среднее число исправно работающих изделий за весь период времени
        return np.average(avg_work_fines_details_in_period)

    # начальное число деталей на начало испытаний
    initial_details: int = data.get("total_details", 0)

    # начальные временные интервалы, в которых подсчитано число отказов
    initial_failed_periods: dict = data.get("failed_periods")

    # интервал времени, в котором надо посчитать отказ
    desired_periods: dict = data.get("desired_period")

    # среднее число исправно работающих деталей за весь период
    avg_work_fines_details_in_period = []

    # среднее число работающих деталей
    avg_work_fines = calc_average_worksfine_details_on_period(
        on_begin_details=initial_details,
        failed_period=initial_failed_periods
    )

    # число отказавших деталей за указанный интервал времени
    failured_details = initial_failed_periods.get(
        str(desired_periods.get("end")))

    # расчетный период времени
    delta_t = desired_periods.get("end") - desired_periods.get("start")

    alpha_t = calc_failure_frequency(faulured_details=failured_details,
                                     initial_details=initial_details,
                                     period=delta_t)

    failure_rate = calc_failure_rate(faulured_details=failured_details,
                                     avg_worksfine_details=avg_work_fines,
                                     period=delta_t)

    return {"failure_freq": str(alpha_t),
            "failure_rate": str(failure_rate)}


def task3(data: dict) -> dict:
    initial_details = data.get("initial_details")
    delta_time = data.get("delta_time")
    failures_list = data.get("failures")
    probability_fine = []
    failure_freq = []
    failure_rate = []
    fine_in_period = initial_details

    accum_failure = 0

    for failure in failures_list:
        accum_failure += failure
        probability_fine.append(
            (initial_details - accum_failure) / initial_details)
        failure_freq.append(np.format_float_scientific(
            failure / (initial_details * delta_time), precision=2))
        failure_rate.append(np.format_float_scientific(
            failure /
            (delta_time * (
                np.average([fine_in_period, fine_in_period - failure]))),
            precision=2))
        print(delta_time, fine_in_period, fine_in_period - failure)
        fine_in_period -= failure

    print(accum_failure)
    print(len(failures_list)*delta_time)

    return {"P(t)": f"{probability_fine}",
            "a(t)": f"{failure_freq}",
            "lambda(t)": f"{failure_rate}"}
