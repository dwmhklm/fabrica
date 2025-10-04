from flask import Flask as f

app = f(__name__)

@app.route("/")
def home():
   return 'Hello World'

@app.route("/contato")
def cadastro():
   return 'Telefone: 11 98765-4321'

if __name__ == "__main__":
    app.run(debug=True)
    home()
