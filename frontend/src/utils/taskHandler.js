import axios from "axios"

const taskHandlerMain = ({ part, task, variant }, setVisible, setAnswer) => {
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
        setAnswer(JSON.stringify(response.data))
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
    setVisible(true)
  })
}

export default taskHandlerMain
