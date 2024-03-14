import axios from "axios"
import style from "./TestLogicComponent.module.css"
import { Button } from "primereact/button"

export default function TestLogicComponent() {
  const taskHandler = (event, { part, task, variant }) => {
    const request_task = async () => {
      const response_task = await axios.get(
        `http://localhost:8000/request_task/part_${part}_task_${task}_var_${variant}`
      )

      return JSON.parse(response_task.data.content)
    }
    request_task().then((response) => {
      console.log(response)
      const jsonObject = JSON.stringify(response)
      const blob = new Blob([jsonObject], { type: "application/json" })

      const formData = new FormData()
      formData.append("file_bytes", blob, "filename.json")

      axios
        .post(`http://localhost:8000/part_${part}_task_${task}`, formData, {
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
    })
  }
  return (
    <div className={style.content}>
      <div className={style.variants}>
        <h2>Задача 1</h2>
        <Button
          className={style.button}
          label="Вариант 1"
          key={"task-1-1"}
          onClick={(event) =>
            taskHandler(event, { part: 1, task: 1, variant: 1 })
          }
        />

        <Button
          className={style.button}
          label="Вариант 2"
          key={"task-1-2"}
          onClick={(event) =>
            taskHandler(event, { part: 1, task: 1, variant: 2 })
          }
        />
        <Button
          className={style.button}
          label="Вариант 3"
          key={"task-1-3"}
          onClick={(event) =>
            taskHandler(event, { part: 1, task: 1, variant: 3 })
          }
        />
        <Button
          className={style.button}
          label="Вариант 4"
          key={"task-1-4"}
          onClick={(event) =>
            taskHandler(event, { part: 1, task: 1, variant: 4 })
          }
        />
        <Button
          className={style.button}
          label="Вариант 5"
          key={"task-1-5"}
          onClick={(event) =>
            taskHandler(event, { part: 1, task: 1, variant: 5 })
          }
        />
      </div>

      <div className={style.variants}>
        <h2>Задача 2</h2>
        <Button
          className={style.button}
          label="Вариант 1"
          key={"task-2-1"}
          onClick={(event) =>
            taskHandler(event, { part: 1, task: 2, variant: 1 })
          }
        />
        <Button
          className={style.button}
          label="Вариант 2"
          key={"task-2-2"}
          onClick={(event) =>
            taskHandler(event, { part: 1, task: 2, variant: 2 })
          }
        />
        <Button
          className={style.button}
          label="Вариант 3"
          key={"task-2-3"}
          onClick={(event) =>
            taskHandler(event, { part: 1, task: 2, variant: 3 })
          }
        />
        <Button
          className={style.button}
          label="Вариант 4"
          key={"task-2-4"}
          onClick={(event) =>
            taskHandler(event, { part: 1, task: 2, variant: 4 })
          }
        />
        <Button
          className={style.button}
          label="Вариант 5"
          key={"task-2-5"}
          onClick={(event) =>
            taskHandler(event, { part: 1, task: 2, variant: 5 })
          }
        />
      </div>

      <div className={style.variants}>
        <h2>Задача 3</h2>
        <Button
          className={style.button}
          label="Вариант 1"
          key={"task-3-1"}
          onClick={(event) =>
            taskHandler(event, { part: 1, task: 3, variant: 1 })
          }
        />
        <Button
          className={style.button}
          label="Вариант 2"
          key={"task-3-2"}
          onClick={(event) =>
            taskHandler(event, { part: 1, task: 3, variant: 2 })
          }
        />
        <Button
          className={style.button}
          label="Вариант 3"
          key={"task-3-3"}
          onClick={(event) =>
            taskHandler(event, { part: 1, task: 3, variant: 3 })
          }
        />
        <Button
          className={style.button}
          label="Вариант 4"
          key={"task-3-4"}
          onClick={(event) =>
            taskHandler(event, { part: 1, task: 3, variant: 4 })
          }
        />
        <Button
          className={style.button}
          label="Вариант 5"
          key={"task-3-5"}
          onClick={(event) =>
            taskHandler(event, { part: 1, task: 3, variant: 5 })
          }
        />
      </div>

      <div className={style.variants}>
        <h2>Задача 4</h2>
        <Button
          className={style.button}
          label="Вариант 1"
          key={"task-4-1"}
          onClick={(event) =>
            taskHandler(event, { part: 1, task: 4, variant: 1 })
          }
        />
        <Button
          className={style.button}
          label="Вариант 2"
          key={"task-4-2"}
          onClick={(event) =>
            taskHandler(event, { part: 1, task: 4, variant: 2 })
          }
        />
        <Button
          className={style.button}
          label="Вариант 3"
          key={"task-4-3"}
          onClick={(event) =>
            taskHandler(event, { part: 1, task: 4, variant: 3 })
          }
        />
        <Button
          className={style.button}
          label="Вариант 4"
          key={"task-4-4"}
          onClick={(event) =>
            taskHandler(event, { part: 1, task: 4, variant: 4 })
          }
        />
        <Button
          className={style.button}
          label="Вариант 5"
          key={"task-4-5"}
          onClick={(event) =>
            taskHandler(event, { part: 1, task: 4, variant: 5 })
          }
        />
      </div>

      <div className={style.variants}>
        <h2>Задача 5</h2>
        <Button
          className={style.button}
          label="Вариант 1"
          key={"task-5-1"}
          onClick={(event) =>
            taskHandler(event, { part: 1, task: 5, variant: 1 })
          }
        />
        <Button
          className={style.button}
          label="Вариант 2"
          key={"task-5-2"}
          onClick={(event) =>
            taskHandler(event, { part: 1, task: 5, variant: 2 })
          }
        />
        <Button
          className={style.button}
          label="Вариант 3"
          key={"task-5-3"}
          onClick={(event) =>
            taskHandler(event, { part: 1, task: 5, variant: 3 })
          }
        />
        <Button
          className={style.button}
          label="Вариант 4"
          key={"task-5-4"}
          onClick={(event) =>
            taskHandler(event, { part: 1, task: 5, variant: 4 })
          }
        />
        <Button
          className={style.button}
          label="Вариант 5"
          key={"task-5-5"}
          onClick={(event) =>
            taskHandler(event, { part: 1, task: 5, variant: 5 })
          }
        />
      </div>

      <div className={style.variants}>
        <h2>Задача 6</h2>
        <Button
          className={style.button}
          label="Вариант 1"
          key={"task-6-1"}
          onClick={(event) =>
            taskHandler(event, { part: 1, task: 6, variant: 1 })
          }
        />
        <Button
          className={style.button}
          label="Вариант 2"
          key={"task-6-2"}
          onClick={(event) =>
            taskHandler(event, { part: 1, task: 6, variant: 2 })
          }
        />
        <Button
          className={style.button}
          label="Вариант 3"
          key={"task-6-3"}
          onClick={(event) =>
            taskHandler(event, { part: 1, task: 6, variant: 3 })
          }
        />
        <Button
          className={style.button}
          label="Вариант 4"
          key={"task-6-4"}
          onClick={(event) =>
            taskHandler(event, { part: 1, task: 6, variant: 4 })
          }
        />
        <Button
          className={style.button}
          label="Вариант 5"
          key={"task-6-5"}
          onClick={(event) =>
            taskHandler(event, { part: 1, task: 6, variant: 5 })
          }
        />
      </div>
      <div className={style.variants}>
        <h2>Задача 7</h2>
        <Button
          className={style.button}
          label="Вариант 1"
          key={"task-7-1"}
          onClick={(event) =>
            taskHandler(event, { part: 1, task: 7, variant: 1 })
          }
        />
        <Button
          className={style.button}
          label="Вариант 2"
          key={"task-7-2"}
          onClick={(event) =>
            taskHandler(event, { part: 1, task: 7, variant: 2 })
          }
        />
        <Button
          className={style.button}
          label="Вариант 3"
          key={"task-7-3"}
          onClick={(event) =>
            taskHandler(event, { part: 1, task: 7, variant: 3 })
          }
        />
        <Button
          className={style.button}
          label="Вариант 4"
          key={"task-7-4"}
          onClick={(event) =>
            taskHandler(event, { part: 1, task: 7, variant: 4 })
          }
        />
        <Button
          className={style.button}
          label="Вариант 5"
          key={"task-7-5"}
          onClick={(event) =>
            taskHandler(event, { part: 1, task: 7, variant: 5 })
          }
        />
      </div>
      <div className={style.variants}>
        <h2>Задача 8</h2>
        <Button
          className={style.button}
          label="Вариант 1"
          key={"task-8-1"}
          onClick={(event) =>
            taskHandler(event, { part: 1, task: 8, variant: 1 })
          }
        />
        <Button
          className={style.button}
          label="Вариант 2"
          key={"task-8-2"}
          onClick={(event) =>
            taskHandler(event, { part: 1, task: 8, variant: 2 })
          }
        />
        <Button
          className={style.button}
          label="Вариант 3"
          key={"task-8-3"}
          onClick={(event) =>
            taskHandler(event, { part: 1, task: 8, variant: 3 })
          }
        />
        <Button
          className={style.button}
          label="Вариант 4"
          key={"task-8-4"}
          onClick={(event) =>
            taskHandler(event, { part: 1, task: 8, variant: 4 })
          }
        />
        <Button
          className={style.button}
          label="Вариант 5"
          key={"task-8-5"}
          onClick={(event) =>
            taskHandler(event, { part: 1, task: 8, variant: 5 })
          }
        />
      </div>
    </div>
  )
}
