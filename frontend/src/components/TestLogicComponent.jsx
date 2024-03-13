import axios from "axios"
import taskJsonData from "../data/taskOneVarOne"
import style from "./TestLogicComponent.module.css"
import { Button } from "primereact/button"

export default function TestLogicComponent() {
  const jsonObject = JSON.stringify(taskJsonData)
  const blob = new Blob([jsonObject], { type: "application/json" })

  const formData = new FormData()
  formData.append("file_bytes", blob, "filename.json")

  axios
    .post("http://localhost:8000/part_2_task_1", formData, {
      headers: {
        "Content-Type": "multipart/form-data",
      },
      timeout: 10000,
    })
    .then((response) => {
      console.log(response.data)
    })
    .catch((error) => {
      if (error.response) {
        // Запрос был сделан и сервер ответил кодом состояния
        // который выходит из диапазона 2xx
        console.log(error.response.data)
        console.log(error.response.status)
        console.log(error.response.headers)
      } else if (error.request) {
        // Запрос был сделан, но ответ не был получен
        console.log(error.request)
      } else {
        // Что-то пошло не так при настройке запроса
        console.log("Error", error.message)
      }
    })
  const taskHandlerOne = (event) => {
    console.log(event.target.id)
  }
  return (
    <div className={style.content}>
      <div className={style.variants}>
        <h2>Задача 1</h2>
        <Button
          className={style.button}
          label="Вариант 1"
          key={"task-1-1"}
          onClick={(event) => taskHandlerOne(event)}
          id="11"
        />
        <Button
          className={style.button}
          label="Вариант 2"
          key={"task-1-2"}
          id="12"
        />
        <Button
          className={style.button}
          label="Вариант 3"
          key={"task-1-3"}
          id="13"
        />
        <Button
          className={style.button}
          label="Вариант 4"
          key={"task-1-4"}
          id="14"
        />
        <Button
          className={style.button}
          label="Вариант 5"
          key={"task-1-5"}
          id="15"
        />
      </div>
    </div>
  )
}
