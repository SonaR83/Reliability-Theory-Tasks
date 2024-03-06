import axios from 'axios'
import taskJsonData from '../data/taskOneVarOne'

export default function TestLogicComponent() {
  const jsonObject = JSON.stringify(taskJsonData)
  const blob = new Blob([jsonObject], { type: 'application/json' })

  const formData = new FormData()
  formData.append('file_bytes', blob, 'filename.json')

  axios
    .post('http://localhost:8000/part_2_task_1', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
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
        console.log('Error', error.message)
      }
    })
  return <h1>test component</h1>
}
