from flask import Flask, jsonify, request

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
