from flask import flask, jsonify, request
app = flask(__name__)
alunos_db = []
id = 0
@app.route("/filmes", methods=["POST"])
def criar_alunos():
    global id
    id = id + 1
    dados = request.get_json()
    nome = dados.get("nome")
    idade = dados.get("idade")
    curso = dados.get("curso")
    alunos = {"id": id, "nome": nome, "idade": idade, "curso": curso}
    alunos_db.append(alunos)
    return jsonify(alunos)