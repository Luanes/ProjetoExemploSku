# coding: utf-8

from flask import Flask, request, url_for, render_template
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
from db import ocorrencias, bairro_logradouro, logradouros, bairros, ocorrencias, tp_emergencia
import cadastros
import mapUtil

app = Flask("wtf")
GoogleMaps(app)

# por enquanto vamos usar um template html hardcoded
# mas calma! em breve falaremos  sobre os templates com Jinja2
base_html = u"""
  <html>
  <head>
      <title>{title}</title>
  </head>
  <body>
     {body}
  </body>
  </html>
"""

@app.route("/ocorrencias/cadastrao", methods=["GET", "POST"])
def cadastrao():
	cadastros.cadastrar_bairro()
	cadastros.visualizar_bairros()
	cadastros.cadastrar_logradouros()
	cadastros.visualizar_logradouros()
	cadastros.cadastrar_relacionamento()
	cadastros.visualizar_relacionamento()
	cadastros.cadastrar_tp_emergencia()
	cadastros.visualizar_tp_emergencia()
	#cadastros.cadastrar_ocorrencia()
	cadastros.cadastrar_ocorrencias()
	cadastros.visualizar_ocorrencia()
	
@app.route("/ocorrencias/cadastro", methods=["GET", "POST"])
def cadastro():
	
    if request.method == "POST":
        dados_do_formulario = request.form.to_dict()
	print(dados_do_formulario)
        nova_ocorrencia = ocorrencias.insert(dados_do_formulario)
        return u"""
            <h1>Ocorrencia id %s inserida com sucesso!</h1>
            <a href="%s"> Inserir nova Ocorrencia </a>
        """ % (nova_ocorrencia, url_for('cadastro'))
    else:  # GET
        formulario = u"""
           <form method="post" action="/ocorrencias/cadastro">
               <label>bairro:<br />
                    <input type="text" name="bairro" id="bairro" />
               </label>
               <br />
               <label>GeolocalizacaoX:<br />
                    <input type="number" step="0.0000001" name="GeolocalizacaoX" id="GeolocalizacaoX" />
               </label>
			   <br />
			   <label>GeolocalizacaoY:<br />
                    <input type="number" step="0.0000001" name="GeolocalizacaoY" id="GeolocalizacaoY" />
               </label>
               <input type="submit" value="Postar" />
           </form>
        """
        return base_html.format(title=u"Inserir nova ocorrencia", body=formulario)

@app.route("/ocorrencias")
def index():
	logradouros = mapUtil.geraListaNomes(list(cadastros.get_todos_logradouros()),'nome_logradouro')
	bairros = mapUtil.geraListaNomes(list(cadastros.get_todos_bairros()),'nome_bairro')
	return render_template("tela_inicial.html", bairros=bairros, logradouros = logradouros)
	
@app.route("/ocorrencias/vizualizacoes")
def visu():
	logradouros = cadastros.get_list_id_logradouros_relacao_bairro_logradouro(cadastros.get_id_bairro('ABRAAO'))
	for x in range(len(logradouros)):
		print logradouros[x]['id']

@app.route("/ocorrencias/bairros/<bairro_escolhido>")
def ocorrenciasBairros(bairro_escolhido):
	#Pega a lista de relacoes bairro_logradouro a partir de um bairro escolhido
	lista_relacao_bairro_logradouro_do_bairro_escolhido = cadastros.get_relacao_bairro(bairro_escolhido)
	
	#Pega a lista de logradouros daquele bairro
	lista_nome_logradouros_do_bairro = mapUtil.geraListaDeLogradouros(lista_relacao_bairro_logradouro_do_bairro_escolhido)
	
	#Pega ocorrencias que aconteceram naquele bairro, utilizando a lista de relacao bairro_logradouro com o bairro escolhido
	lista_ocorrencia = cadastros.get_ocorrencias(lista_relacao_bairro_logradouro_do_bairro_escolhido)
	
	#Pega o bairro escolhido, sera usado como centro do mapa na hora de carregar o mapa
	bairro = cadastros.get_bairro(bairro_escolhido)

	#Carrega os marcadores no mapa a partir da relacao bairro_logradouro, visto que essa sera a geolocalizacao da ocorrencia
	markers_on_map = mapUtil.criar_marcadores(lista_ocorrencia)
	#ocorrencia = ocorrencias.find_one(id=ocorrencia_id)
	print(len(markers_on_map))
	mymap = Map(
		style= "height:800px;width:1400px;margin:0;",
		zoom = 16,
        identifier="view-side",
        lat=bairro['latitude'],
        lng=bairro['longitude'],
        markers = markers_on_map
    )
	#O uso das {{}} no template.html identifica os campos que serao carregados através do render_template. No caso, serao as colunas adjacentes do banco.
	return render_template("ocorrencias_por_bairro.html", bairro=bairro_escolhido, nome_logradouro_do_bairro = lista_nome_logradouros_do_bairro, mymap=mymap)

@app.route("/ocorrencias/logradouros/<logradouro_escolhido>")
def ocorrenciasLogradouros(logradouro_escolhido):
	#Pega a lista de relacoes bairro_logradouro a partir de um bairro escolhido
	relacao_bairro_logradouro_do_logradouro_escolhido = cadastros.get_relacao_logradouro(logradouro_escolhido)
	
	#Pega o logradouro escolhido, usado para colocar os marcadores
	logradouro_selecionado = cadastros.get_logradouro(logradouro_escolhido)

	#Pega ocorrencias que aconteceram naquele bairro, utilizando a lista de relacao bairro_logradouro com o bairro escolhido
	lista_ocorrencia = cadastros.get_ocorrencias(relacao_bairro_logradouro_do_logradouro_escolhido)

	#Pega o bairro escolhido, sera usado como centro do mapa na hora de carregar o mapa
	bairro = cadastros.get_bairro_id(relacao_bairro_logradouro_do_logradouro_escolhido[0]['id_bairro'])
	print(lista_ocorrencia)

	#Carrega os marcadores no mapa a partir da relacao bairro_logradouro, visto que essa sera a geolocalizacao da ocorrencia
	markers_on_map = mapUtil.criar_marcadores(lista_ocorrencia)
	#ocorrencia = ocorrencias.find_one(id=ocorrencia_id)
	mymap = Map(
		style= "height:800px;width:1400px;margin:0;",
		zoom = 16,
        identifier="view-side",
        lat=bairro['latitude'],
        lng=bairro['longitude'],
        markers = markers_on_map
    )
	#O uso das {{}} no template.html identifica os campos que serao carregados através do render_template. No caso, serao as colunas adjacentes do banco.
	return render_template("ocorrencias_por_logradouro.html", nome_logradouro = logradouro_selecionado['nome_logradouro'], data_ocorrencia = lista_ocorrencia[0]['data_ocorrencia'],horario_ocorrencia = lista_ocorrencia[0]['horario_ocorrencia'],evaporacao_piche = lista_ocorrencia[0]['evaporacao_piche'],insolacao = lista_ocorrencia[0]['insolacao'],temp_minima = lista_ocorrencia[0]['temp_minima'],precipitacao = lista_ocorrencia[0]['precipitacao'],velocidade_vento_media = lista_ocorrencia[0]['velocidade_vento_media'],umidade_relativa_media = lista_ocorrencia[0]['umidade_relativa_media'],tp_emergencia = lista_ocorrencia[0]['id_tp_emergencia'],temp_comp_media = lista_ocorrencia[0]['temp_comp_media'],  mymap=mymap)

if __name__ == "__main__":
    #app.run(debug=True, use_reloader=True)
    # caso tenha problemas com multithreading na hora de inserir o registro no db use	#return base_html.format(title=ocorrencia['bairro'], body=ocorrencia_html)
    app.run(debug=False, use_reloader=False)