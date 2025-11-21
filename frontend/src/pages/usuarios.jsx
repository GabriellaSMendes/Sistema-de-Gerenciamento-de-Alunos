import { useState } from "react";
import api from "../api"
import "../styles/form.css"
import "../styles/global.css"

export default function Usurios() {
  const [form, setForm] = useState({
    nome: "",
    matricula: "",
    email: "",
    senha: "",
    tipo: "ALUNO"
  });

  const [msg, setMsg] = useState("");

  function handleChange(e) {
    setForm({ ...form, [e.target.name]: e.target.value });
  }

  async function handleSubmit(e) {
    e.preventDefault();
    setMsg("");

    try {
      await api.post("/usuarios/", form, {
        headers: { "Content-Type": "application/json" }
      });
      setMsg("Usuário cadastrado!");

      setForm({
        nome: "",
        matricula: "",
        email: "",
        senha: "",
        tipo: "ALUNO"
      });

    } catch (error) {
      setMsg("Erro ao cadastrar usuário.");
    }
  }

  return (
    <div className="container">
      <h2>Cadastrar Usuário</h2>

      <form onSubmit={handleSubmit}>
        <label>Nome</label>
        <input name="nome" value={form.nome} onChange={handleChange} required />

        <label>Matrícula</label>
        <input name="matricula" value={form.matricula} onChange={handleChange} required />

        <label>Email</label>
        <input type="email" name="email" value={form.email} onChange={handleChange} required />

        <label>Senha</label>
        <input type="password" name="senha" value={form.senha} onChange={handleChange} required />

        <label>Tipo</label>
        <select name="tipo" value={form.tipo} onChange={handleChange}>
          <option value="ALUNO">ALUNO</option>
          <option value="PROFESSOR">PROFESSOR</option>
          <option value="ADMIN">ADMIN</option>
        </select>

        <button className="btn" type="submit">Salvar</button>
      </form>

      {msg && <p className="success">{msg}</p>}
    </div>
  );
}