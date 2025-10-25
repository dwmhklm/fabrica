from flask import Flask as f, request, render_template


app = f(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    resultado = None


    if request.method == "POST":

        try: 

            v1 = float(request.form.get("valor1", 0))
            v2 = float(request.form.get("valor2", 0))
            operacao = (request.form.get("operacao"))


            if operacao == "adicao":
                resultado = v1 + v2
            elif operacao == "subtracao":
                resultado = v1 - v2
            elif operacao == "multiplicacao":
                resultado = v1 * v2
            elif operacao == "divisao":
                if v2 == 0:
                    resultado = "Não é possível dividir por zero."
                else:
                    resultado = v1 / v2
            else:
                print("Operação inválida")
        except ValueError:
            resultado = "Digite apenas números"

    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)