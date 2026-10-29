from flask import Flask, jsonify, request

app = Flask(__name__)
cidade_db = []
id = 0

@app.route("/filmes", methods=["POST"])
def criar_cidades():
    global id
    id = id + 1
    dados = request.get_json()
    nome = dados.get("nome")
    endereco = dados.get("endereco")
    numero = dados.get("numero")
    cidades = {"id": id, "nome": nome, "endereco": endereco, "numero": numero}
    cidade_db.append(cidades)
    return jsonify(cidades)
