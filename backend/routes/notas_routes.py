from flask import Blueprint, jsonify, request
from backend.services.notas_service import NotasService

notas_routes = Blueprint("notas_route", __name__)
service = NotasService()

#listar notas por alino
@notas_routes.route("/<int:id_aluno>", methods=["GET"])
def listar_notas(id_aluno):
    notas = service.repo.buscarNota(id_aluno)
    return jsonify(notas)

#lançar nota p/ aluno
@notas_routes.route("/", methods=["POST"])
def lancar_nota():
    data = request.get_json()
    
    service.lancarNotas(
        id_disciplina=data.get("id_disciplina"),
        aluno_id=data.get("aluno_id"),
        turma_id=data.get("turma_id"),
        avaliacao=data.get("avaliacao"),
        nota=data.get("nota"),
        data_lancamento=data.get("data_lancamento")
    )
    
    return jsonify({"message": "Nota lançada!"})