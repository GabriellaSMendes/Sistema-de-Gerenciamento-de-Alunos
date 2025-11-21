import { useEffect, useState } from "react";
import api from "../api";

export default function Notas() {
  const [alunos, setAlunos] = useState([]);
  const [disciplinas, setDisciplinas] = useState([]);
  const [turmas, setTurmas] = useState([]);

  const [id_aluno, setIdAluno] = useState("");
  const [id_disciplina, setIdDisciplina] = useState("");
  const [id_turma, setIdTurma] = useState("");
  const [avaliacao, setAvaliacao] = useState("");
  const [nota, setNota] = useState("");

  const [mensagem, setMensagem] = useState("");

  // Buscar alunos, disciplinas e turmas
  useEffect(() => {
    api.get("/usuarios?tipo=ALUNO").then(res => setAlunos(res.data));
    api.get("/disciplinas").then(res => setDisciplinas(res.data));
    api.get("/turmas").then(res => setTurmas(res.data));
  }, []);

  function salvarNota(e) {
    e.preventDefault();

    api.post("/notas", {
      id_aluno,
      id_disciplina,
      id_turma,
      avaliacao,
      nota: parseFloat(nota)
    }).then(() => {
      setMensagem("Nota lançada com sucesso!");
      setIdAluno("");
      setIdDisciplina("");
      setIdTurma("");
      setAvaliacao("");
      setNota("");
    }).catch(() => {
      setMensagem("Erro ao lançar nota.");
    });
  }

  return (
    <div className="form-container">
      <h2>Lançar Nota</h2>

      <form onSubmit={salvarNota}>
        <label>Aluno</label>
        <select value={id_aluno} onChange={e => setIdAluno(e.target.value)} required>
          <option value="">Selecione...</option>
          {alunos.map(a => (
            <option key={a[0]} value={a[0]}>
              {a[1]}
            </option>
          ))}
        </select>

        <label>Disciplina</label>
        <select value={id_disciplina} onChange={e => setIdDisciplina(e.target.value)} required>
          <option value="">Selecione...</option>
          {disciplinas.map(d => (
            <option key={d[0]} value={d[0]}>
              {d[1]}
            </option>
          ))}
        </select>

        <label>Turma</label>
        <select value={id_turma} onChange={e => setIdTurma(e.target.value)} required>
          <option value="">Selecione...</option>
          {turmas.map(t => (
            <option key={t[0]} value={t[0]}>
              {t[1]}
            </option>
          ))}
        </select>

        <label>Avaliação</label>
        <input value={avaliacao} onChange={e => setAvaliacao(e.target.value)} placeholder="Ex: P1" required />

        <label>Nota</label>
        <input type="number" step="0.01" min="0" max="10" value={nota} onChange={e => setNota(e.target.value)} required />

        <button type="submit">Salvar</button>
      </form>

      {mensagem && <p className="msg">{mensagem}</p>}
    </div>
  );
}
