from flask import Flask as f, render_template

path = "C:\\Users\\prog3\\Desktop\\gbn\clone\\fabrica\8-flask\\"

app = f(__name__)

@app.route("/")

def home():
   return render_template("index.html")

@app.route("/cadastro")
def cadastro():
   return render_template("cadastro.html")

if __name__ == "__main__":
    app.run(debug=True)
    home()

   