import React from "react"
import { Card } from "primereact/card"
import { Button } from "primereact/button"
import style from "./MainMenu.module.css"
import { Link } from "react-router-dom"

function MainMenu() {
  const navigateHandler = (path) => {
    console.log(path)
  }
  return (
    <div className={style.mainMenu}>
      <Card
        title="Задания по теории надежности"
        style={{
          padding: "25px",
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
        }}
      >
        <div
          style={{
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
          }}
        >
          <h3>Задачи</h3>
          <div
            style={{
              display: "flex",
              flexDirection: "row",
              alignItems: "center",
            }}
          >
            <Link to="part1">
              <Button
                label="Part 1"
                onClick={() => navigateHandler("part1")}
                style={{
                  width: "60px",
                  height: "30px",
                  borderRadius: "1px",
                  margin: "5px",
                  justifyContent: "center",
                  alignItems: "center",
                }}
              />
            </Link>

            <Link to="part2">
              <Button
                label="Part 2"
                onClick={() => navigateHandler("part2")}
                style={{
                  width: "60px",
                  height: "30px",
                  borderRadius: "1px",
                  margin: "5px",
                  justifyContent: "center",
                  alignItems: "center",
                }}
              />
            </Link>
          </div>
        </div>
      </Card>
    </div>
  )
}

export default MainMenu
