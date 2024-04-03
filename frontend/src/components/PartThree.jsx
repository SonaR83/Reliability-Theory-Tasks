import { useState } from "react"
import style from "./TestLogicComponent.module.css"
import { Dialog } from "primereact/dialog"

import genericButton from "./buttons/button"

export default function PartThree() {
  const [answer, setAnswer] = useState(null)
  const [visible, setVisible] = useState(false)
  console.log(Array.from({ length: 5 }, (x, i) => i))
  return (
    <div className={style.content}>
      <div className={style.variants}>
        <h2>Задача 1</h2>
        <Dialog
          header="Ответ"
          visible={visible}
          style={{ width: "50vw", fontSize: "25px" }}
          onHide={() => setVisible(false)}
        >
          <p className="m-0">{answer}</p>
        </Dialog>

        {genericButton(style.button, setVisible, setAnswer, 3, 1, 1)}
        {genericButton(style.button, setVisible, setAnswer, 3, 1, 2)}
        {genericButton(style.button, setVisible, setAnswer, 3, 1, 3)}
        {genericButton(style.button, setVisible, setAnswer, 3, 1, 4)}
        {genericButton(style.button, setVisible, setAnswer, 3, 1, 5)}
      </div>

      <div className={style.variants}>
        <h2>Задача 2</h2>
        {genericButton(style.button, setVisible, setAnswer, 3, 2, 1)}
        {genericButton(style.button, setVisible, setAnswer, 3, 2, 2)}
        {genericButton(style.button, setVisible, setAnswer, 3, 2, 3)}
        {genericButton(style.button, setVisible, setAnswer, 3, 2, 4)}
        {genericButton(style.button, setVisible, setAnswer, 3, 2, 5)}
      </div>

      <div className={style.variants}>
        <h2>Задача 3</h2>
        {genericButton(style.button, setVisible, setAnswer, 3, 3, 1)}
        {genericButton(style.button, setVisible, setAnswer, 3, 3, 2)}
        {genericButton(style.button, setVisible, setAnswer, 3, 3, 3)}
        {genericButton(style.button, setVisible, setAnswer, 3, 3, 4)}
        {genericButton(style.button, setVisible, setAnswer, 3, 3, 5)}
      </div>

      <div className={style.variants}>
        <h2>Задача 4</h2>
        {genericButton(style.button, setVisible, setAnswer, 3, 4, 1)}
        {genericButton(style.button, setVisible, setAnswer, 3, 4, 2)}
        {genericButton(style.button, setVisible, setAnswer, 3, 4, 3)}
        {genericButton(style.button, setVisible, setAnswer, 3, 4, 4)}
        {genericButton(style.button, setVisible, setAnswer, 3, 4, 5)}
      </div>

      <div className={style.variants}>
        <h2>Задача 5</h2>
        {genericButton(style.button, setVisible, setAnswer, 3, 5, 1)}
        {genericButton(style.button, setVisible, setAnswer, 3, 5, 2)}
        {genericButton(style.button, setVisible, setAnswer, 3, 5, 3)}
        {genericButton(style.button, setVisible, setAnswer, 3, 5, 4)}
        {genericButton(style.button, setVisible, setAnswer, 3, 5, 5)}
      </div>

      <div className={style.variants}>
        <h2>Задача 6</h2>
        {genericButton(style.button, setVisible, setAnswer, 3, 6, 1)}
        {genericButton(style.button, setVisible, setAnswer, 3, 6, 2)}
        {genericButton(style.button, setVisible, setAnswer, 3, 6, 3)}
        {genericButton(style.button, setVisible, setAnswer, 3, 6, 4)}
        {genericButton(style.button, setVisible, setAnswer, 3, 6, 5)}
      </div>
    </div>
  )
}
