from flask import Blueprint, jsonify, request
from backend.services.turma_service import TurmaService

turma_routes = Blueprint("turma_routes", __name__)
service = TurmaService()

#listar turmas
@turma_routes.route("/", methods=["GET"])
def listar_turmas():
    turmas = service.repo.listarTurma()
    return jsonify(turmas)

#criar turmas
@turma_routes.route("/", methods=["POST"])
def criar_turma():
    data = request.get_json()
    
    service.criarTurma(
        cod_turma=data.get("cod_turma"),
        id_disciplina=data.get("id_disciplina"),
        id_professor=data.get("id_professor"),
        ano=data.get("ano"),
        semestre=data.get("semestre")
    )

    
    return jsonify({"message": "Turma criada!"})