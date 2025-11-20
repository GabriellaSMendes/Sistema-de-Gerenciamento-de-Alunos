from flask import Blueprint, jsonify, request
from backend.services.disciplina_service import DisciplinaService

disciplina_routes = Blueprint("disciplina_routes", __name__)
service = DisciplinaService()

#listar disciplinas
@disciplina_routes.route("/", methods=["GET"])
def listar_disciplinas():
    disciplinas = service.repo.listarDisciplina()
    return jsonify(disciplinas)

#criar disciplina
@disciplina_routes.route("/", methods=["POST"])
def criar_disciplina():
    data = request.get_json()
    
    service.criarDisciplina(
        id=None,
        nome=data.get("nome"),
        cod_disciplina=data.get("cod_disciplina"),
        id_professor=data.get("id_professor")
    )
    
    return jsonify({"message": "Disciplina criada!"})
    