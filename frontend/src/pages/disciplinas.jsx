import { useState, useEffect } from "react";
import api from "../api";
import "../styles/form.css";
import "../styles/global.css";

export default function Disciplinas() {
  const [professores, setProfessores] = useState([]);
  const [form, setForm] = useState({
    nome: "",
    cod_disciplina: "",
    id_professor: ""
  });
  const [msg, setMsg] = useState("");

  useEffect(() => {
    async function carregarProfessores() {
      try {
        const res = await api.get("/usuarios/");
        const lista = res.data.filter(u => u[5] === "PROFESSOR"); 
        setProfessores(lista);
      } catch (error) {
        setMsg("Erro ao carregar professores.");
      }
    }
    carregarProfessores();
  }, []);

  function handleChange(e) {
    setForm({ ...form, [e.target.name]: e.target.value });
  }

  async function handleSubmit(e) {
    e.preventDefault();
    setMsg("");

    try {
      await api.post("/disciplinas/", form);
      setMsg("Disciplina cadastrada com sucesso!");
      setForm({ nome: "", cod_disciplina: "", id_professor: "" });
    } catch (error) {
      setMsg("Erro ao cadastrar disciplina.");
    }
  }

  return (
    <div className="container">
      <h2>Cadastrar Disciplina</h2>

      <form onSubmit={handleSubmit}>
        <label>Nome da disciplina</label>
        <input name="nome" value={form.nome} onChange={handleChange} required />

        <label>Código da disciplina</label>
        <input name="cod_disciplina" value={form.cod_disciplina} onChange={handleChange} required />

        <label>Professor responsável</label>
        <select name="id_professor" value={form.id_professor} onChange={handleChange} required>
          <option value="">Selecione...</option>
          {professores.map((p) => (
            <option key={p[0]} value={p[0]}>
              {p[1]} ({p[2]})
            </option>
          ))}
        </select>

        <button className="btn" type="submit">Salvar</button>
      </form>

      {msg && <p className="success">{msg}</p>}
    </div>
  );
}
