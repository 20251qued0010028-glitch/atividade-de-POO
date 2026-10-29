from flask import Flask, jsonify, request

app = Flask(__name__)
curso_db = []
id = 0

@app.route("/filmes", methods=["POST"])
def criar_curso():
    global id
    id = id + 1
    dados = request.get_json()
    nome = dados.get("nome")
    instituicao = dados.get("instituicao")
    duracao = dados.get("duracao")
    cursos = {"id": id, "nome": nome, "instituicao": instituicao, "duracao": duracao}
    curso_db.append(cursos)
    return jsonify(cursos)
