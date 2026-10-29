from flask import Flask, jsonify, request

app = Flask(__name__)
musicas_db = []
id = 0

@app.route("/filmes", methods=["POST"])
def criar_musicas():
    global id
    id = id + 1
    dados = request.get_json()
    nome = dados.get("nome")
    artista = dados.get("artista")
    ano = dados.get("ano")
    musicas  = {"id": id, "nome": nome, "ano": ano, "artista": artista}
    musicas_db.append(musicas)
    return jsonify(musicas)


