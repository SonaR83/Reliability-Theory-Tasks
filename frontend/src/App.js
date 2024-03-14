import { BrowserRouter, Route, Routes } from "react-router-dom"
import "primereact/resources/themes/lara-dark-indigo/theme.css"
import "primereact/resources/primereact.min.css"
import "primeicons/primeicons.css"

import "./App.css"
import TestLogicComponent from "./components/TestLogicComponent"
import PartTwo from "./components/PartTwo"
import MainLayout from "./components/layouts/MainLayout"
import MainMenu from "./components/MainMenu"

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<MainLayout />} />
        <Route index element={<MainMenu />} />
        <Route path="part1" element={<TestLogicComponent />} />
        <Route path="part2" element={<PartTwo />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App
