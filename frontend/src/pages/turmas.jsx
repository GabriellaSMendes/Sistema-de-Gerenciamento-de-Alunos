import { useState, useEffect } from "react";
import api from "../api";
import "../styles/form.css";
import "../styles/global.css";

export default function Turmas() {
  const [disciplinas, setDisciplinas] = useState([]);
  const [professores, setProfessores] = useState([]);
  const [msg, setMsg] = useState("");

  const [form, setForm] = useState({
    cod_turma: "",
    id_disciplina: "",
    id_professor: "",
    ano: "",
    semestre: ""
  });

  useEffect(() => {
    async function carregarDados() {
      try {
        const respDisc = await api.get("/disciplinas/");
        setDisciplinas(respDisc.data);

        const respProf = await api.get("/usuarios/");
        const listaProf = respProf.data.filter(u => u[5] === "PROFESSOR");
        setProfessores(listaProf);
      } catch (error) {
        setMsg("Erro ao carregar dados.");
      }
    }
    carregarDados();
  }, []);

  function handleChange(e) {
    setForm({ ...form, [e.target.name]: e.target.value });
  }

  async function handleSubmit(e) {
    e.preventDefault();
    setMsg("");

    try {
      await api.post("/turmas/", form);
      setMsg("Turma cadastrada com sucesso!");
      setForm({ cod_turma: "", id_disciplina: "", id_professor: "", ano: "", semestre: "" });
    } catch (error) {
      setMsg("Erro ao cadastrar turma.");
    }
  }

  return (
    <div className="container">
      <h2>Cadastrar Turma</h2>

      <form onSubmit={handleSubmit}>
        <label>Código da Turma</label>
        <input name="cod_turma" value={form.cod_turma} onChange={handleChange} required />

        <label>Disciplina</label>
        <select name="id_disciplina" value={form.id_disciplina} onChange={handleChange} required>
          <option value="">Selecione...</option>
          {disciplinas.map((d) => (
            <option key={d[0]} value={d[0]}>
              {d[1]} ({d[2]})
            </option>
          ))}
        </select>

        <label>Professor</label>
        <select name="id_professor" value={form.id_professor} onChange={handleChange} required>
          <option value="">Selecione...</option>
          {professores.map((p) => (
            <option key={p[0]} value={p[0]}>
              {p[1]} ({p[2]})
            </option>
          ))}
        </select>

        <label>Ano</label>
        <input type="number" name="ano" value={form.ano} onChange={handleChange} required />

        <label>Semestre</label>
        <select name="semestre" value={form.semestre} onChange={handleChange} required>
          <option value="">Selecione...</option>
          <option value="1">1</option>
          <option value="2">2</option>
        </select>

        <button className="btn" type="submit">Salvar</button>
      </form>

      {msg && <p className="success">{msg}</p>}
    </div>
  );
}
