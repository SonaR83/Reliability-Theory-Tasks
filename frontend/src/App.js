import { BrowserRouter, Route, Routes } from "react-router-dom"
import "primereact/resources/themes/lara-dark-indigo/theme.css"
import "primereact/resources/primereact.min.css"
import "primeicons/primeicons.css"

import "./App.css"
import PartOne from "./components/PartOne"
import PartTwo from "./components/PartTwo"
import PartThree from "./components/PartThree"
import MainLayout from "./components/layouts/MainLayout"
import MainMenu from "./components/MainMenu"

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<MainLayout />} />
        <Route index element={<MainMenu />} />
        <Route path="part1" element={<PartOne />} />
        <Route path="part2" element={<PartTwo />} />
        <Route path="part3" element={<PartThree />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App
