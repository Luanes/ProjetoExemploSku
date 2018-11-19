# coding: utf-8

import dataset

db = dataset.connect('sqlite:///webPageBombeiros.db')
ocorrencias = db['ocorrencias']
bairro_logradouro = db['bairro_logradouro']
logradouros = db['logradouros']
bairros = db['bairros']
tp_emergencia = db['tp_emergencia']