from flask import Flask, jsonify, request

app = Flask(__name__)
jogos_db = []
id = 0

@app.route("/filmes", methods=["POST"])
def criar_jogos():
    global id
    id = id + 1
    dados = request.get_json()
    nome = dados.get("nome")
    genero = dados.get("genero")
    ano = dados.get("ano")
    jogos = {"id": id, "nome": nome, "genero": genero, "ano": ano}
    jogos_db.append(jogos)
    return jsonify(jogos)



