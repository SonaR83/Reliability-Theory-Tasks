import { BrowserRouter, Route, Routes } from "react-router-dom"
import "primereact/resources/themes/lara-dark-indigo/theme.css"
import "primereact/resources/primereact.min.css"
import "primeicons/primeicons.css"

import "./App.css"
import TestLogicComponent from "./components/TestLogicComponent"
import MainLayout from "./components/layouts/MainLayout"

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<MainLayout />} />
        <Route index element={<TestLogicComponent />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App
