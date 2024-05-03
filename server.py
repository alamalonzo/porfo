from flask import Flask, render_template, send_from_directory, request, redirect
from time import time, ctime
import csv

app = Flask(__name__)

@app.route("/")
def home_1():
    return render_template("index.html")

#haciendolo dinamico con <>
@app.route("/<string:page_name>")
def page_name(page_name):
    return render_template(page_name)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico')


#para agregar la hora y fecha
# def tiempo(func):
#     def colocar_hora():
#         t = time()
#         hora = ctime(t)
#         func()
#         return colocar_hora


#recibo un dict de request.form.to_dict() y eso lo divido en diferentes variable que
#luego escribe en mi txt con comas para poder usarlo en excel si asi lo quiero.
def escribir(data):
     with open("database.txt", mode="a") as file:
            email = data["email"]
            tema = data["subject"]
            texto = data["message"]
            t = time()
            hora = ctime(t)
            file.write(f"\n{email}, {tema}, {texto}, {hora} ")

#para escribir en un csv import csv:
def escribir_csv(data):
    with open("database.csv",newline="", mode="a") as database2:
        email = data["email"]
        tema = data["subject"]
        texto = data["message"]
        t = time()
        hora = ctime(t)
        #el delimitador casi siempre sera la ","
        iniciacion = csv.writer(database2, delimiter=",", quotechar=" ", quoting= csv.QUOTE_MINIMAL)
        iniciacion.writerow([email, tema, texto, hora])

#para imprimir en python la informacion del contacto.
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
        escribir_csv(data)
        #luego de importar FAlsk redirect podemos redireccionar a una pagina x
        return redirect("/gracias.html")
    else:
        return "algo anda mal, intenta denuevo."


if __name__ == "__main__":
    app.run(debug=True)

