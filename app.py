from flask import Flask, render_template, request, redirect
import random


app = Flask(__name__)

app.secret_key = "202026"

lista_comentario = []

@app.route("/")
def pg_principal():
    return render_template("principal.html")

@app.route("/sobre", methods=["GET"])
def pg_sobre():
    return render_template("sobre.html")

@app.route("/login", methods=["GET"])
def pg_login():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login_postn():
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")

    if usuario == "Camila" and senha == "1234":
        return redirect("/comentario")

    else:
        return render_template("login.html", erro = "Acesso negado")
    
@app.route("/comentario", methods=["GET"])
def pg_comentario():
    return render_template("comentario.html", lista_comentario = lista_comentario)

@app.route("/add_comentario", methods=["POST"])
def add_comentario():
    comentario = request.form.get("comentario")
    lista_comentario.append(comentario)
    print(lista_comentario)
    return redirect("/comentario")


app.run(debug=True)

# o debug=True para não precisarmos desligar o servidor, ele altera automaticamente 
# get para abrir a página
# post = escrever e enviar para abrir uma página