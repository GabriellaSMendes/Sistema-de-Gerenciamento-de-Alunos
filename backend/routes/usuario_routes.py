from flask import Blueprint, jsonify, request
from backend.services.usuario_service import UsuarioService

usuario_routes = Blueprint("usuario_routes", __name__)
service = UsuarioService()

# listar usuarios
@usuario_routes.route("/", methods=["GET"])
def listar_usuario():
    usuarios = service.repo.listarUsuario()
    return jsonify(usuarios)

#criar usuarios
@usuario_routes.route("/", methods=["POST"])
def criar_usuario():
    data = request.get_json()
    
    service.criarUsuario(
        nome=data.get("nome"),
        email=data.get("email"),
        senha=data.get("senha"),
        tipo=data.get("tipo"),
        matricula=data.get("matricula")
    )
    
    return jsonify({"message": "Usuário criado!"})