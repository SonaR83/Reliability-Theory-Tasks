import requests
import os

file_path = os.path.abspath("tasks/part_2/tasks/task1/task_1_var_1.json")
with open(file_path, "rb") as file:
    # Подготовка файла к отправке; ключ 'file_bytes' должен соответствовать ожиданиям сервера
    files = {'file_bytes': file}

    with requests.session() as session:
        headers = {"accept": "application/json",
                   "Content-Type": "multipart/form-data",
                   }
        response = session.post(url="http://localhost:8000/part_2_task_1",
                                files=files)

    print(response.json())
