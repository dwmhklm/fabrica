from main import app
from flask import render_template

@app.route("/")
def home():    
    return render_template("bemvindo.html")

@app.route("/cadastro")
def cadastro():    
    return render_template("cadastro.html")

@app.route("/contato")
def contato():
    return render_template("contato.html")