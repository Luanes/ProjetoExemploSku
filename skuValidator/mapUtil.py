# coding: utf-8

import cadastros

prefix = 'http://maps.google.com/mapfiles/ms/icons/'
dicionario_de_icones = { 1 : prefix + 'red-dot.png',2 : prefix + 'green-dot.png',3 : prefix + 'blue-dot.png',4 : prefix + 'yellow-dot.png',5 : prefix + 'msmarker.png',6 : prefix + 'ltblue-dot.png',7 : prefix + 'orange-dot.png',8 : prefix + 'pink-dot.png',9 : prefix + 'purple-dot.png',10 : prefix + 'grn-pushpin.png',11 : prefix + 'ltblu-pushpin.png'}

def criar_marcadores(lista_ocorrencia):
	markers = []
	for x in range(len(lista_ocorrencia)):
		ocorrencia = lista_ocorrencia[x]
		bairro_logradouro_da_ocorrencia = cadastros.get_relacao_bairro_logradouro(ocorrencia['id_bairro_logradouro'])
		new_mark = {
				'icon': dicionario_de_icones[lista_ocorrencia[x]['id_tp_emergencia']],
				'lat': bairro_logradouro_da_ocorrencia['geolocalizacaoX'],
				'lng': bairro_logradouro_da_ocorrencia['geolocalizacaoY'],
				'infobox': "<b>Ocorrencia numero"+ str(x+1) + "</b>"
				}
		markers.append(new_mark)
	return markers

def geraListaDeLogradouros(lista_relacao_bairro_logradouro):
	lista_logradouros_do_bairro = []
	for x in range(len(lista_relacao_bairro_logradouro)):
		logradouro = cadastros.get_logradouro_id(lista_relacao_bairro_logradouro[x]['id_logradouro'])
		lista_logradouros_do_bairro.append(logradouro['nome_logradouro'])
	return lista_logradouros_do_bairro
	
def geraListaDeBairros(bairros):
	lista_bairros = []
	for x in range(len(bairros)):
		lista_bairros.append(bairros['nome_bairros'])
	return lista_logradouros_do_bairro

#revisar
def geraListaDeLogradouros2(logradouros):
	lista_logradouros = []
	for x in range(len(logradouros)):
		lista_logradouros.append(logradouro['nome_logradouro'])
	return lista_logradouros_do_bairro
	
#revisar
def geraListaNomes(listaDeEntrada, stringNomeDoCampo):
	lista = []
	for x in range(len(listaDeEntrada)):
		lista.append(listaDeEntrada[x][stringNomeDoCampo])
	return lista