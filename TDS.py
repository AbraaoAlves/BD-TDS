#!/usr/bin/python
import MySQLdb
import json
import unicodedata

class TDS(object):

    def __init__(self):
        pass

    def queryByFamily(self, familyID):
        self.sql = """
                    SELECT medidorFamilia.nome as 'familiaNome',
                           medidorModelo.nome as 'modeloNome',
                           medidorTerminal.terminalsArrangement, medidorTerminal.terminals,
                           medidorImagem.imagem,
                           medidorAtribGerais.informacao,
                           caracteristica.nome_da_caracteristica, caracteristica.valorPadrao,
                           medidorPendencias.dataDeAbertura, medidorPendencias.dataDeConclusao, medidorPendencias.prioridade, medidorPendencias.observacoes
                    FROM medidor
                    INNER JOIN medidorFamilia ON medidor.medidorFamilia_id = medidorFamilia.id
                    INNER JOIN medidorModelo ON medidorModelo.medidorFamilia_id = medidorFamilia.id
                    INNER JOIN medidorTerminal ON medidor.medidorTerminal_id = medidorTerminal.id
                    INNER JOIN medidorAtribGerais ON medidor.medidorAtribGerais_id = medidorAtribGerais.id
                    INNER JOIN caracteristica ON caracteristica.medidorAtribGerais_id =  medidorAtribGerais.id
                    INNER JOIN medidorImagem ON medidor.medidorImagem_id = medidorImagem.id
                    INNER JOIN medidorPendencias ON medidor.medidorPendencias_id = medidorPendencias.id
                    WHERE medidorFamilia.id = """ +  str(familyID) + """;
                """
        return self.sql

    def queryByModel(self, modelID):
        self.sql = """
                    SELECT medidorFamilia.nome as 'familiaNome',
                           medidorModelo.nome as 'modeloNome',
                           medidorTerminal.terminalsArrangement, medidorTerminal.terminals,
                           medidorImagem.imagem,
                           medidorAtribGerais.informacao,
                           caracteristica.nome_da_caracteristica, caracteristica.valorPadrao,
                           medidorPendencias.dataDeAbertura, medidorPendencias.dataDeConclusao, medidorPendencias.prioridade, medidorPendencias.observacoes
                    FROM medidor
                    INNER JOIN medidorFamilia ON medidor.medidorFamilia_id = medidorFamilia.id
                    INNER JOIN medidorModelo ON medidorModelo.medidorFamilia_id = medidorFamilia.id
                    INNER JOIN medidorTerminal ON medidor.medidorTerminal_id = medidorTerminal.id
                    INNER JOIN medidorAtribGerais ON medidor.medidorAtribGerais_id = medidorAtribGerais.id
                    INNER JOIN caracteristica ON caracteristica.medidorAtribGerais_id =  medidorAtribGerais.id
                    INNER JOIN medidorImagem ON medidor.medidorImagem_id = medidorImagem.id
                    INNER JOIN medidorPendencias ON medidor.medidorPendencias_id = medidorPendencias.id
                    WHERE medidorFamilia.id = """ +  str(modelID) + """;
                """
        return self.sql

    def queryByUser(self, userID):
        self.sql = """
                    SELECT medidorFamilia.nome as 'familiaNome',
                           medidorModelo.nome as 'modeloNome',
                           medidorTerminal.terminalsArrangement, medidorTerminal.terminals,
                           medidorImagem.imagem,
                           medidorAtribGerais.informacao,
                           caracteristica.nome_da_caracteristica, caracteristica.valorPadrao,
                           medidorPendencias.dataDeAbertura, medidorPendencias.dataDeConclusao, medidorPendencias.prioridade, medidorPendencias.observacoes
                    FROM medidor
                    INNER JOIN medidorFamilia ON medidor.medidorFamilia_id = medidorFamilia.id
                    INNER JOIN medidorModelo ON medidorModelo.medidorFamilia_id = medidorFamilia.id
                    INNER JOIN medidorTerminal ON medidor.medidorTerminal_id = medidorTerminal.id
                    INNER JOIN medidorAtribGerais ON medidor.medidorAtribGerais_id = medidorAtribGerais.id
                    INNER JOIN caracteristica ON caracteristica.medidorAtribGerais_id =  medidorAtribGerais.id
                    INNER JOIN medidorImagem ON medidor.medidorImagem_id = medidorImagem.id
                    INNER JOIN medidorPendencias ON medidor.medidorPendencias_id = medidorPendencias.id
                    WHERE usuario.id = """ +  str(userID) + """;
                """
        return self.sql

    def queryByEletraPartNumber(self, partNumber):
        self.sql = """
                    SELECT medidorFamilia.nome as 'familiaNome',
                           medidorModelo.nome as 'modeloNome',
                           medidorTerminal.terminalsArrangement, medidorTerminal.terminals,
                           medidorImagem.imagem,
                           medidorAtribGerais.informacao,
                           caracteristica.nome_da_caracteristica, caracteristica.valorPadrao,
                           medidorPendencias.dataDeAbertura, medidorPendencias.dataDeConclusao, medidorPendencias.prioridade, medidorPendencias.observacoes
                    FROM medidor
                    INNER JOIN medidorFamilia ON medidor.medidorFamilia_id = medidorFamilia.id
                    INNER JOIN medidorModelo ON medidorModelo.medidorFamilia_id = medidorFamilia.id
                    INNER JOIN medidorTerminal ON medidor.medidorTerminal_id = medidorTerminal.id
                    INNER JOIN medidorAtribGerais ON medidor.medidorAtribGerais_id = medidorAtribGerais.id
                    INNER JOIN caracteristica ON caracteristica.medidorAtribGerais_id =  medidorAtribGerais.id
                    INNER JOIN medidorImagem ON medidor.medidorImagem_id = medidorImagem.id
                    INNER JOIN medidorPendencias ON medidor.medidorPendencias_id = medidorPendencias.id
                    WHERE medidorAtribGerais.eletrapartnumber = """ +  str(partNumber) + """;
                """
        return self.sql
    def queryCaracteristics(self, meterID):
        self.sql = """
                SELECT medidorFamilia.nome as 'familiaNome',
                medidorModelo.nome as 'modeloNome',
                caracteristica.nome_da_caracteristica, caracteristica.valorPadrao
                FROM medidor
                INNER JOIN medidorFamilia ON medidor.medidorFamilia_id = medidorFamilia.id
                INNER JOIN medidorModelo ON medidorModelo.medidorFamilia_id = medidorFamilia.id
                INNER JOIN medidorAtribGerais ON medidor.medidorAtribGerais_id = medidorAtribGerais.id
                INNER JOIN caracteristica ON caracteristica.medidorAtribGerais_id =  medidorAtribGerais.id
                WHERE medidor.id = """ + str(meterID) + """;
                """
        return self.sql


##############################################################################################################################
db = MySQLdb.connect(host="189.45.91.201",               # Host
                     user="administrador",               # Username
                     passwd=",,.#+eletra123456",         # Password
                     db="mydb",                          # Database
                     port=33306)                         # Porta
cur = db.cursor()
##############################################################################################################################

meter = TDS()

def whichQuery(idS, idQ):
    #id 1 procurar por familia
    if idS == 1:
        cur.execute(meter.queryByFamily(idQ))
    #id 2 procurar por modelo
    elif idS == 2:
        cur.execute(meter.queryByModel(idQ))
    #id 3 procurar por usuario que cadastrou
    elif idS == 3:
        cur.execute(meter.queryByUser(idQ))
    #id 4 procurar por numero de série eletra (somente numeros)
    elif idS == 4:
        cur.execute(meter.queryByEletraPartNumber(idQ))
    #id 5 procurar por apenas caracteristicas de um medidor especifico
    elif idS == 5:
        cur.execute(meter.queryCaracteristics(idQ))
    else:
        print("ID não existente")


#----------------------------------------------------Não mudar nada daqui pra baixo---------------------------------------------------
#----------------------------------------------A menos que voce saiba o que está fazendo----------------------------------------------
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
    json.dump(rowarray, outfile, True, default=date_handler, indent = 4, ensure_ascii=False)


db.close()
