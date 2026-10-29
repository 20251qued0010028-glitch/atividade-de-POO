from flask import Flask, jsonify, request

app = Flask(__name__)
produtos_db = []
id = 0

@app.route("/filmes", methods=["POST"])
def criar_produtos():
    global id
    id = id + 1
    dados = request.get_json()
    nome = dados.get("nome")
    preco = dados.get("preco")
    categoria = dados.get("categoria")
    produtos = {"id": id, "nome": nome, "preco": preco, "categoria": categoria}
    produtos_db.append(produtos)
    return jsonify(produtos)
