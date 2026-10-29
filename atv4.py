from flask import Flask, jsonify, request

app = Flask(__name__)
funcionarios_db = []
id = 0

@app.route("/filmes", methods=["POST"])
def criar_funcionario():
    global id
    id = id + 1
    dados = request.get_json()
    nome = dados.get("nome")
    cargo = dados.get("cargo")
    salario = dados.get("salario")
    funcionarios = {"id": id, "nome": nome, "cargo": cargo, "salario": salario}
    funcionarios_db.append(funcionarios)
    return jsonify(funcionarios)
