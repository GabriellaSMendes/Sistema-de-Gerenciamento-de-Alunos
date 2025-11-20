from flask import Blueprint, jsonify
from backend.services.media_service import MediaService

relatorio_routes = Blueprint("relatorio_routes", __name__)
service = MediaService()

#calula e retorna media por aluno
@relatorio_routes.route("/<int:id_aluno>", methods=["GET"])
def calcular_media(id_aluno):
    media, situacao = service.calcularMedia(id_aluno)
    return jsonify({
    "media": media,
    "situacao": situacao.value
    })
