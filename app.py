from flask import Flask, render_template, request, redirect
import random


app = Flask(__name__)

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
        return "Você acessou a página restrita"
    else:
        return render_template("login.html", erro = "Acesso negado")


app.run(debug=True)

# o debug=True para não precisarmos desligar o servidor, ele altera automaticamente 