from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/")
def pg_principal():
    return render_template("principal.html")

@app.route("/sobre")
def pg_sobre():
    return render_template("sobre.html")






app.run(debug=True)

# o debug=True para não precisarmos desligar o servidor, ele altera automaticamente 