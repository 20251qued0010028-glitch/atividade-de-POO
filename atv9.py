from flask import Flask, jsonify, request

app = Flask(__name__)
restaurante_db = []
id = 0

@app.route("/filmes", methods=["POST"])
def criar_restaurante():
    global id
    id = id + 1
    dados = request.get_json()
    nome = dados.get("nome")
    tipo = dados.get("tipo")
    cidade = dados.get("cidade")
    restaurante = {"id": id, "nome": nome, "tipo": tipo, "cidade": cidade}
    restaurante_db.append(restaurante)
    return jsonify(restaurante)


