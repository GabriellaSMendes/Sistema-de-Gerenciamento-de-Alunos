import { useState } from "react";
import api from "../api";

export default function Relatorio() {
  const [idAluno, setIdAluno] = useState("");
  const [resultado, setResultado] = useState(null);
  const [mensagem, setMensagem] = useState("");

  function buscarRelatorio(e) {
    e.preventDefault();

    api.get(`/relatorio/${idAluno}`)
      .then(res => {
        setResultado(res.data);
        setMensagem("");
      })
      .catch(() => {
        setResultado(null);
        setMensagem("Aluno não encontrado ou sem notas.");
      });
  }

  return (
    <div className="form-container">
      <h2>Consultar Boletim</h2>

      <form onSubmit={buscarRelatorio}>
        <label>ID do Aluno</label>
        <input
          type="number"
          value={idAluno}
          onChange={e => setIdAluno(e.target.value)}
          placeholder="Digite o ID"
          required
        />
        <button type="submit">Buscar</button>
      </form>

      {mensagem && <p className="msg">{mensagem}</p>}

      {resultado && (
        <div className="box-resultado">
          <h3>Resultado</h3>
          <p><strong>Média:</strong> {resultado.media}</p>
          <p><strong>Situação:</strong> {resultado.situacao}</p>
        </div>
      )}
    </div>
  );
}
