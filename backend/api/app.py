from flask import Flask, jsonify, request
from backend.services.usuario_service import UsuarioService
from backend.services.disciplina_service import DisciplinaService
from backend.services.turma_service import TurmaService
from backend.services.notas_service import NotasService
from backend.services.media_service import MediaService

app = Flask(__name__)

# instâncias das services
usuario_service = UsuarioService()
disciplina_service = DisciplinaService()
turma_service = TurmaService()
notas_service = NotasService()
media_service = MediaService()

# rota inicial
@app.route("/")
def home():
    return jsonify({"message": "API do Sistema de Gestão de Notas de Alunos está rodando!"})

#rota GET 
@app.route("/usuarios", methods=["GET"])
def listar_usuarios():
    usuarios = usuario_service.repo.listarUsuario()
    return jsonify(usuarios)

#rota POST (criar usuário)
@app.route("/usuarios", methods=["POST"])
def criar_usuario():
    data = request.get_json()
    usuario_service.criarUsuario(
        nome=data.get("nome"),
        email=data.get("email"),
        senha=data.get("senha"),
        tipo=data.get("tipo"),
        matricula=data.get("matricula")
    )
    return jsonify({"message": "Usuário criado com sucesso!"})

if __name__ == "__main__":
    app.run(debug=True)