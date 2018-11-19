# coding: utf-8

from flask import Flask, request, url_for, render_template
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
from db import ocorrencias, bairro_logradouro, logradouros, bairros, ocorrencias, tp_emergencia
import random
import decimal

#Eliminando caracteres sujos
#logradouros_do_abraaoo = ['JOAO MEIRELLES - 663867','23 DE MARCO - 2454','ABRAAO - 4003','BIAS PEIXOTO','BOM JESUS DE IGUAPE','CAMPOLINO ALVES - 526','DA FONTE - 663','DA FONTE I','DANIEL MARCELINO - 677','DOMINGOS LUIZ GONZAGA','DOMINGOS LUIZ GONZAGA - 377208','HERCILIO DE AQUINO - 1034','JOAO ACELINO SENNA - 1186','JOAO MEIRELLES - 1250','JOAQUIM CARNEIRO - 1293','JOAQUIM FERNANDES DE OLIVEIRA','JOAQUIM FERNANDEZ DE OLIVEIRA','JOAQUIM JOSE SANTANA - 1300','JOSE AMARO OURIQUES - 1413','JOSE AMARO OURIQUES - 377822','JOSE JOAQUIM DE SANTANA - 377867','JOSE JOAQUIM SANTANA - 2450','JOSE JOAQUIM SANTANA - 1395','LEONEL DUTRA','LEONEL DUTRA - 1500','LUIZ GONZAGA LAMEGO','MANOEL FELIX CARDOSO','MEDICO  MIGUEL SALLES CAVALCANTI','MIGUEL S CAVALCANTI','NELIO OURIQUES','NOSSA SENHORA APARECIDA - 314','OURIQUES','PADRE OSMAR MULLER - 1842','PATRICIO CALDEIRA DE ANDRADE','PEDRO ANDRADE GARCIA','PROCOPIO FERREIRA','PROFESSOR ROSINHA CAMPOS','PROFESSORA  OTILIA COSTA','PROFESSORA ROSINHA CAMPOS','SILVIO POSSOBON','VIDEIRA','VIDEIRA']
logradouros_do_abraao = ['JOAO-MEIRELLES','23-DE-MARCO','ABRAAO','BIAS-PEIXOTO','BOM-JESUS-DE-IGUAPE','CAMPOLINO-ALVES','DA-FONTE','DA-FONTE-I','DANIEL-MARCELINO','DOMINGOS-LUIZ-GONZAGA','DOMINGOS-LUIZ-GONZAGA','HERCILIO-DE-AQUINO','JOAO-ACELINO-SENNA','JOAO-MEIRELLES','JOAQUIM-CARNEIRO','JOAQUIM-FERNANDES-DE-OLIVEIRA','JOAQUIM-FERNANDEZ-DE-OLIVEIRA','JOAQUIM-JOSE-SANTANA','JOSE-AMARO-OURIQUES','JOSE-AMARO-OURIQUES','JOSE-JOAQUIM-DE-SANTANA','JOSE-JOAQUIM-SANTANA','JOSE-JOAQUIM-SANTANA','LEONEL-DUTRA','LEONEL-DUTRA','LUIZ-GONZAGA-LAMEGO','MANOEL-FELIX-CARDOSO','MEDICO-MIGUEL-SALLES-CAVALCANTI','MIGUEL-S-CAVALCANTI','NELIO-OURIQUES','NOSSA-SENHORA-APARECIDA','OURIQUES','PADRE-OSMAR-MULLER','PATRICIO-CALDEIRA-DE-ANDRADE','PEDRO-ANDRADE-GARCIA','PROCOPIO-FERREIRA','PROFESSOR-ROSINHA-CAMPOS','PROFESSORA-OTILIA-COSTA','PROFESSORA-ROSINHA-CAMPOS','SILVIO-POSSOBON','VIDEIRA']

ocorrencia1 = [{'data_ocorrencia': '2007-05-26', 'horario_ocorrencia' : '11:13:28', 'evaporacao_piche' : 2.2, 'insolacao' : 9.5, 'temp_minima' : 9.5, 'precipitacao':0, 'velocidade_vento_media' : 2.5333, 'umidade_relativa_media': 79.25, 'temp_comp_media' : 15.9
}]

tp_emergencia
def cadastrar_bairro():
	novo_bairro = {'nome_bairro': 'CANTO', 'latitude':-27.583693, 'longitude':-48.588646}
	bairros.insert(novo_bairro)
	novo_bairro = {'nome_bairro': 'ABRAAO', 'latitude':-27.6057259, 'longitude':-48.592358}
	bairros.insert(novo_bairro)

def visualizar_bairros():
	bairro = bairros.find_one(id=1)
	print(bairro['nome_bairro'])
	bairro = bairros.find_one(id=2)
	print(bairro['nome_bairro'])

def cadastrar_logradouros():
	for x in range(len(logradouros_do_abraao)):
		novo_logradouro = {'nome_logradouro': logradouros_do_abraao[x]}
		logradouros.insert(novo_logradouro)
		
def visualizar_logradouros():
	logradouro = logradouros.find_one(id=1)
	print(logradouro['nome_logradouro'])
	logradouro = logradouros.find_one(id=15)
	print(logradouro['nome_logradouro'])
	
def cadastrar_relacionamento():
	for x in range(len(logradouros_do_abraao)):
		# O x comeca em 0 mas o ID do banco de dados comeca em 1
		auxiliarParaIdBancoDeDados = x + 1
		# Variavel auxiliar para gerar localização para testar
		x = float(decimal.Decimal(random.randrange(30, 100))/10000)
		y = float(decimal.Decimal(random.randrange(10, 40))/10000)
		print(x)
		geolocalizacaoX = float(-27.603601) + -1*x
		geolocalizacaoY = float(-48.590801) + -1*y
		print('geolocalizacaoX :')
		print(geolocalizacaoX)
		print('geolocalizacaoY :')
		print(geolocalizacaoY)
		logradouro = logradouros.find_one(id=auxiliarParaIdBancoDeDados)
		print(logradouro['nome_logradouro'])
		bairro = bairros.find_one(id=2)
		novo_relacionamento = {'id_bairro': bairro['id'], 'id_logradouro': logradouro['id'], 'geolocalizacaoX': geolocalizacaoX, 'geolocalizacaoY' : geolocalizacaoY}
		bairro_logradouro.insert(novo_relacionamento)
		
def visualizar_relacionamento():
	relacionamento = bairro_logradouro.find_one(id=1)
	print(relacionamento)
	relacionamento = bairro_logradouro.find_one(id=15)
	print(relacionamento)
	
def get_id_bairro(bairro):
	bairro_selecionado = bairros.find_one(nome_bairro = bairro)
	return bairro_selecionado['id']
	
def get_logradouro(logradouro):
	logradouro_selecionado = logradouros.find_one(nome_logradouro = logradouro)
	return logradouro_selecionado
	
def get_logradouro_id(id_logradouro):
	logradouro_selecionado = logradouros.find_one(id = id_logradouro)
	return logradouro_selecionado

#revisar
def get_todos_logradouros():
	logradouro_selecionado = logradouros.find()
	return logradouro_selecionado
	
#revisar
def get_todos_bairros():
	logradouro_selecionado = bairros.find()
	return logradouro_selecionado
	
#Para testes
def get_list_id_logradouros_relacao_bairro_logradouro(bairro):
	logradouros_selecionados = bairro_logradouro.find(id_bairro = bairro)
	return list(logradouros_selecionados)

def cadastrar_ocorrencia():
	id_bairro = get_id_bairro('ABRAAO')
	logradouro = get_id_logradouro('JOAO_MEIRELLES')
	bairro_logradouro_selecionado = bairro_logradouro.find_one(id_bairro = id_bairro, id_logradouro = logradouro['id'])
	ocorrencia1[0]['id_bairro_logradouro'] = bairro_logradouro_selecionado['id']
	nova_ocorrencia = ocorrencia1[0]
	ocorrencias.insert(nova_ocorrencia)
	
def cadastrar_ocorrencias():
	id_bairro_logradouros = list(bairro_logradouro.find(id_bairro = get_id_bairro('ABRAAO')))
	for x in range(len(id_bairro_logradouros)):
			nova_ocorrencia = ocorrencia1[0]
			nova_ocorrencia['id_bairro_logradouro'] = id_bairro_logradouros[x]['id']
			nova_ocorrencia['id_tp_emergencia'] = random.randint(1,11)
			id = ocorrencias.insert(nova_ocorrencia)
			print(ocorrencias.find_one(id = id))
	
def visualizar_ocorrencia():
	print(ocorrencias.find_one(id =1))
	
def get_ocorrencias(bairro_logradouros):
	lista_bairro_logradouros = bairro_logradouros
	lista_ocorrencias = []
	for x in range(len(lista_bairro_logradouros)):
		lista_de_ocorrencias_do_bairro_logradouro = list(ocorrencias.find(id = lista_bairro_logradouros[x]['id']))
		for y in range(len(lista_de_ocorrencias_do_bairro_logradouro)):
			lista_ocorrencias.append(lista_de_ocorrencias_do_bairro_logradouro[y])
	return lista_ocorrencias
	
def cadastrar_tp_emergencia():
	novo_tp_emergencia = {'tp_emergencia': 'INCENDIO'}
	tp_emergencia.insert(novo_tp_emergencia)
	novo_tp_emergencia = {'tp_emergencia': 'AUXILIOS / APOIOS'}
	tp_emergencia.insert(novo_tp_emergencia)
	novo_tp_emergencia = {'tp_emergencia': 'PRODUTOS PERIGOSOS'}
	tp_emergencia.insert(novo_tp_emergencia)
	novo_tp_emergencia = {'tp_emergencia': 'SALVAMENTO / BUSCA / RESGATE'}
	tp_emergencia.insert(novo_tp_emergencia)
	novo_tp_emergencia = {'tp_emergencia': 'ATENDIMENTO PRE-HOSPITALAR'}
	tp_emergencia.insert(novo_tp_emergencia)
	novo_tp_emergencia = {'tp_emergencia': 'OCORRENCIA NAO ATENDIDA'}
	tp_emergencia.insert(novo_tp_emergencia)
	novo_tp_emergencia = {'tp_emergencia': 'DIVERSOS'}
	tp_emergencia.insert(novo_tp_emergencia)
	novo_tp_emergencia = {'tp_emergencia': 'ACIDENTE DE TRANSITO'}
	tp_emergencia.insert(novo_tp_emergencia)
	novo_tp_emergencia = {'tp_emergencia': 'ACOES PREVENTIVAS'}
	tp_emergencia.insert(novo_tp_emergencia)
	novo_tp_emergencia = {'tp_emergencia': 'AVERIGUACAO / CORTE DE ARVORE'}
	tp_emergencia.insert(novo_tp_emergencia)
	novo_tp_emergencia = {'tp_emergencia': 'AVERIGUACAO / MANEJO DE INSETO'}
	tp_emergencia.insert(novo_tp_emergencia)
	
def visualizar_tp_emergencia():
	emergencia = tp_emergencia.find_one(id=4)
	print(emergencia)

def get_relacao_bairro_logradouro(id):
	return bairro_logradouro.find_one(id = id)

def get_relacao_bairro(nome_do_bairro):
	bairro = bairros.find_one(nome_bairro = nome_do_bairro)
	return list(bairro_logradouro.find(id_bairro = bairro['id']))
	
def get_relacao_logradouro(nome_do_logradouro):
	logradouro = logradouros.find_one(nome_logradouro = nome_do_logradouro)
	return list(bairro_logradouro.find(id_logradouro = logradouro['id']))
	
def get_bairro(nome_do_bairro):
	bairro = bairros.find_one(nome_bairro = nome_do_bairro)
	return bairro
	
def get_bairro_id(id):
	bairro = bairros.find_one(id = id)
	return bairro