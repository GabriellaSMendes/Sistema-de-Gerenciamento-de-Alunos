import { Link } from "react-router-dom";
import "../styles/global.css"

export default function Home (){
    return(
        <div className="container">
            <h2>Dashboard</h2>

            <Link to="/usuarios"><button className="btn">Cadastrar Usuários</button></Link>
            <Link to="/disciplinas"><button className="btn">Cadastrar disciplinas</button></Link>
            <Link to="/turmas"><button className="btn">Cadastrar turma</button></Link>
            <Link to="/notas"><button className="btn">Lançar Nota</button></Link>
            <Link to="/relatorio"><button className="btn">Consultar boletim</button></Link>

        </div>
    );
}