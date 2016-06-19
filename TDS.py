#!/usr/bin/python
import MySQLdb
import json
import unicodedata

db = MySQLdb.connect(host="189.45.91.201",  # Host
                     user="administrador",           # Username
                     passwd=",,.#+eletra123456",         # Password
                     db="tds",             # Database
                     port=33306)

cur = db.cursor()

cur.execute("""
    SELECT medidorFamilia.nome,
           medidorModelo.nome,
           medidorTerminal.terminalsArrangement, medidorTerminal.terminals,
           medidorImagem.imagem,
           medidorAtribGerais.informacao,
           caracteristica.nome_da_caracteristica, caracteristica.valorPadrao,
           medidorPendencias.dataDeAbertura, medidorPendencias.dataDeConclusao, medidorPendencias.prioridade, medidorPendencias.observacoes,
           usuario.username
    FROM medidor
    INNER JOIN medidorFamilia ON medidor.medidorFamilia_id = medidorFamilia.id
    INNER JOIN medidorModelo ON medidorModelo.medidorFamilia_id = medidorFamilia.id
    INNER JOIN medidorTerminal ON medidor.medidorTerminal_id = medidorTerminal.id
    INNER JOIN medidorAtribGerais ON medidor.medidorAtribGerais_id = medidorAtribGerais.id
    INNER JOIN caracteristica ON caracteristica.medidorAtribGerais_id =  medidorAtribGerais.id
    INNER JOIN medidorImagem ON medidor.medidorImagem_id = medidorImagem.id
    INNER JOIN medidorPendencias ON medidor.medidorPendencias_id = medidorPendencias.id
    INNER JOIN usuario ON medidorPendencias.usuario_id = usuario.id;
""")

results = cur.fetchall()

rowarray = []
columns = [desc[0] for desc in cur.description]

for row in results:
    d = dict(zip(columns, row))
    rowarray.append(d)

def date_handler(obj):
    if hasattr(obj, 'isoformat'):
        return obj.isoformat()
    else:
        raise TypeError

with open('data.json', 'w') as outfile:
    json.dump(rowarray, outfile, True, default=date_handler, indent = 2, ensure_ascii=False)


db.close()