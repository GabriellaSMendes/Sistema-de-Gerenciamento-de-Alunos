from flask import Flask, jsonify
from flask_cors import CORS
from backend.routes.usuario_routes import usuario_routes
from backend.routes.disciplina_routes import disciplina_routes
from backend.routes.turma_routes import turma_routes
from backend.routes.notas_routes import notas_routes
from backend.routes.relatorio_routes import relatorio_routes

app = Flask(__name__)
CORS(app)  # p permitir acesso ao frontend com react

# registra os grupo das rotas
app.register_blueprint(usuario_routes, url_prefix="/usuarios")
app.register_blueprint(disciplina_routes, url_prefix="/disciplinas")
app.register_blueprint(turma_routes, url_prefix="/turmas")
app.register_blueprint(notas_routes, url_prefix="/notas")
app.register_blueprint(relatorio_routes, url_prefix="/relatorio")

# rota inicial
@app.route("/")
def home():
    return jsonify({"message": "API do Sistema de Gestão de Notas de Alunos está rodando!"})

if __name__ == "__main__":
    app.run(debug=True)
