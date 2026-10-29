from flask import Flask, jsonify, request

app = Flask(__name__)
carros_db = []
id = 0

@app.route("/filmes", methods=["POST"])
def criar_carros():
    global id
    id = id + 1
    dados = request.get_json()
    modelo = dados.get("modelo")
    marca = dados.get("marca")
    ano = dados.get("ano")
    carro = {"id": id, "modelo": modelo, "marca": marca, "ano": ano}
    carros_db.append(carro)
    return jsonify(carro)


