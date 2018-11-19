# coding: utf-8

from flask import Flask, request, url_for, render_template

app = Flask("wtf")

@app.route("/sku/<sku>", methods=["GET", "POST"])
def cadastro(sku):
	array = []
	arrayTecidos = sku.split('T')
	arrayRevestimento = sku.split('R')
	arrayTecidosFinal = {}
	arrayRevestimento = {}
	for x in range(len(arrayTecidos)-1):
		dict = { 'Tecido' + str(x+1) : arrayTecidos[x+1]
		arrayTecidos.append(dict)
	
	for x in range(len(arrayRevestimento)-1):
		dict = { 'Revestimento' + str(x+1) : arrayRevestimento[x+1]
		arrayRevestimento.append(dict)
	
	
	return render_template("validateSku.html", arrayTecidosFinal = arrayTecidosFinal, arrayRevestimento = arrayRevestimento)

if __name__ == "__main__":
    #app.run(debug=True, use_reloader=True)
    # caso tenha problemas com multithreading na hora de inserir o registro no db use	#return base_html.format(title=ocorrencia['bairro'], body=ocorrencia_html)
    app.run(debug=False, use_reloader=False)