import { BrowserRouter, Routes, Route } from "react-router-dom";
import Login from "./pages/Login.jsx";
import Signup from "./pages/Signup.jsx";
import Home from "./pages/Home.jsx";
import Vote from "./pages/Vote.jsx";
import Results from "./pages/Results.jsx";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/signup" element={<Signup />} />
        <Route path="/home" element={<Home />} />
        <Route path="/vote/:id" element={<Vote />} />
        <Route path="/results/:id" element={<Results />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;