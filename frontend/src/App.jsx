import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Landing from './pages/Landing'
import Auth from './pages/Auth'
import './App.css'

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Landing />} />
        <Route path="/login" element={<Auth initialMode="login" />} />
        <Route path="/register" element={<Auth initialMode="register" />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App