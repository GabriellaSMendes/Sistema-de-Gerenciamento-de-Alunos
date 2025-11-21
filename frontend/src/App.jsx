import { BrowserRouter, Routes, Route } from "react-router-dom";
import Header from "./components/Header";
import Home from "./pages/home";
import Usuarios from "./pages/usuarios";
import Disciplinas from "./pages/disciplinas";
import Turmas from "./pages/turmas";
import Notas from "./pages/notas";
import Relatorio from "./pages/relatorio";
import "./styles/global.css";

export default function App() {
  return (
    <BrowserRouter>
      <Header />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/usuarios" element={<Usuarios />} />
        <Route path="/disciplinas" element={<Disciplinas />} />
        <Route path="/turmas" element={<Turmas />} />
        <Route path="/notas" element={<Notas />} />
        <Route path="/relatorio" element={<Relatorio />} />
      </Routes>
    </BrowserRouter>
  );
}