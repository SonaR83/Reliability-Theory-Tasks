import numpy as np
import matplotlib.pyplot as plt

from api.v1.router.schemas import (
    SchemaPart1Task2, SchemaPart1Task4, SchemaPart1Task5,
    SchemaPart1Task6, SchemaPart1Task7, SchemaPart1Task8)


def task1(data: dict) -> dict:
    task = SchemaPart1Task2(**data)

    # отношение разности исправных и отказавших деталей к общему числу деталей
    reliability_probability = (
                                      task.total_details - task.failed_details) / task.total_details
    # отношение отказавших деталей к общему числу деталей
    #  или как 1- reliability_probability - так как исправность и отказ
    # являются несовместными событиями
    failure_probability = task.failed_details / task.total_details

    return {f"P({task.time_period})": str(reliability_probability),
            f"Q({task.time_period})": str(failure_probability)}


def task2(data: dict) -> dict:
    # частота отказа
    def calc_failure_frequency(_failure_details, _initial_details, period):

        print(f'{_failure_details=}, '
              f'{_initial_details=},'
              f'{period=}')
        # считается как отношение отказавшизх деталей за период времени
        # к начальному числу деталей за этот же период времени
        return np.format_float_scientific(
            _failure_details / (_initial_details * period), precision=2)

    def calc_failure_rate(failure_details, avg_works_fine_details, period):
        # интенсивность отказа: считается как отношение неисправных деталей
        # к среднему числу исправных деталей за период времени
        return np.format_float_scientific(
            failure_details / (avg_works_fine_details * period), precision=1)

    def calc_average_works_fine_details_on_period(
            on_begin_details: int,
            failed_period: dict):
        # для каждого периода времени считаем
        # число исправно работающих изделий к концу крайнего интервала времени
        # и добавляем в массив чтобы потом по нему посчитать среднее значение
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
    avg_work_fines = calc_average_works_fine_details_on_period(
        on_begin_details=initial_details,
        failed_period=initial_failed_periods
    )
    print(avg_work_fines)

    # число отказавших деталей за указанный интервал времени
    failure_details = initial_failed_periods.get(
        str(desired_periods.get("end")))

    # расчетный период времени
    delta_t = desired_periods.get("end") - desired_periods.get("start")

    # частота отказа
    alpha_t = calc_failure_frequency(_failure_details=failure_details,
                                     _initial_details=initial_details,
                                     period=delta_t)

    failure_rate = calc_failure_rate(failure_details=failure_details,
                                     avg_works_fine_details=avg_work_fines,
                                     period=delta_t)

    return {f"failure_freq({delta_t})": str(alpha_t),
            f"failure_rate({delta_t})": str(failure_rate)}


def task3(data: dict) -> dict:
    initial_details = data.get("initial_details")
    delta_time = data.get("delta_time")
    failures_list = data.get("failures")
    probability_fine = []
    failure_freq = []
    failure_rate = []
    fine_in_period = initial_details
    x_axis = [0, *[count * delta_time for count, _ in
                   enumerate(failures_list, start=1)]]
    accum_failure = 0

    for failure in failures_list:
        # считаем число отказавших деталей в каждый период времени
        accum_failure += failure
        # для каждого интервала времени считаем ВБР
        probability_fine.append(
            (initial_details - accum_failure) / initial_details)
        # для каждого интервала времени считаем частоту отказа
        failure_freq.append(np.format_float_scientific(
            failure / (initial_details * delta_time), precision=2))
        # для каждого интервала времени считаем интенсивность отказа
        failure_rate.append(np.format_float_scientific(
            failure /
            (delta_time * (
                np.average([fine_in_period, fine_in_period - failure]))),
            precision=2))

        fine_in_period -= failure

    alt_x = [*x_axis[1:]]
    # Создаем фигуру и массив подграфиков (осей)
    # 3 графика вертикально, 1 колонка
    fig, axs = plt.subplots(1, 2, figsize=(15, 5))
    axs[0].plot(x_axis, [1, *probability_fine],
                label="Вероятность безотказной работы")
    axs[0].set_ylabel("Probability")
    axs[0].set_title("Вероятность безотказной работы")
    axs[0].legend()

    # Второй под график с двумя графиками: частота отказов 
    # и интенсивность отказов
    axs[1].plot(alt_x, [float(i) * 10000 for i in failure_freq],
                label="Частота отказов")
    axs[1].plot(alt_x, [float(i) * 10000 for i in failure_rate],
                label="Интенсивность отказов")
    axs[1].set_ylabel("Интенсивность отказов")
    axs[1].set_title("Частота и интенсивность отказов")
    axs[1].legend()  # Показываем легенду для различения графиков

    # Автоматически настраиваем отступы между подграфиками
    plt.tight_layout()

    # Показываем фигуру

    plt.show()
    return {"P(t)": f"{probability_fine}",
            "a(t)": f"{failure_freq}",
            "lambda(t)": f"{failure_rate}"}


def task4(data: dict) -> dict:
    task = SchemaPart1Task4(**data)
    delta_time = task.end_time - task.time_before
    return {"T0": delta_time / task.total_failures}


def task5(data: dict) -> dict:
    task = SchemaPart1Task5(**data)
    sum_work = sum(task.work_times)
    sum_failures = sum(task.failures)
    return {"avgT0": sum_work / sum_failures}


def task6(data: dict) -> dict:
    task = SchemaPart1Task6(**data)
    failures = task.failures
    failure_time = task.failure_time
    mttf_components = [t / f if f != 0 else float('inf') for f, t in
                       zip(failures, failure_time)]

    # Calculate harmonic mean of MTTF for the system
    finite_mttf_components = [m for m in mttf_components if m != float('inf')]
    mttf_system = 1 / sum(
        1 / m for m in
        finite_mttf_components) if finite_mttf_components else float(
        'inf')

    # Return the result in the specified format
    return {"avgT0": mttf_system}


def task7(data: dict) -> dict:
    task = SchemaPart1Task7(**data)

    return {"avg recovery time": np.average(task.recovery_times)}


def task8(data: dict) -> dict:
    task = SchemaPart1Task8(**data)

    return {"availability factor": task.avg_failure_time / sum(
        [task.avg_failure_time, task.recovery_time])}
