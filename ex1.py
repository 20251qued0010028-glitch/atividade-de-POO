from flask import flask, jsonify, request

app = Flask(__name__)
filmes_db = []
id = 0

@app.route("/filmes", methods=["POST"])
def criar_filmes():
    global id
    id = id + 1
    dados = request.get_json()
    nome = dados.get("nome")
    ano = dados.get("ano")
    diretor = dados.get("diretor")
    filmes = {"id": id, "nome": nome, "ano": ano, "diretor": diretor}
    filmes_db.append(filmes)
    return jsonify(filmes)

@app.route("/filmes/<int:id>", methods=["PUT"])
def editar_filmes():
    dados = request.get_json()
    nome = dados.get("nome")
    ano = dados.get("ano")
    diretor = dados.get("diretor")
    for filmes in filmes_db:
        if filmes["id"] == id:
           filmes["nome"] == nome
           filmes["diretor"] == diretor
           filmes["ano"] == ano
           return jsonify(filmes), 200
    return jsonify({"erro": "filme nao encontrado"}), 408

@app.route("/filmes/<int:id>", methods=["DELETE"])
def remover_filmes(id):
        for filmes in filmes_db:
            if filmes["id"] == id:
                 