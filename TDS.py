#!/usr/bin/python
# -*- coding: cp1252 -*-
#!/usr/bin/python
import MySQLdb
import json
import unicodedata
import os
class TDS(object):

    db = None
    cur = None

    def __init__(self):
        ##############################################################################################################################
        self.db = MySQLdb.connect(host="189.45.91.201",               # Host
                             user="administrador",               # Username
                             passwd=",,.#+eletra123456",         # Password
                             db="mydb",                          # Database
                             port=33306)                         # Porta
        self.cur = self.db.cursor()
        ##############################################################################################################################

    def __delattr__(self):
        db.close()
        print("DESTROYED")

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
                           dataDeAbertura, medidorPendencias.dataDeConclusao, medidorPendencias.prioridade, medidorPendencias.observacoes
                    FROM medidor
                    INNER JOIN medidorFamilia ON medidor.medidorFamilia_id = medidorFamilia.id
                    INNER JOIN medidorModelo ON medidorModelo.id = medidor.id
                    INNER JOIN medidorTerminal ON medidor.medidorTerminal_id = medidorTerminal.id
                    INNER JOIN medidorAtribGerais ON medidor.medidorAtribGerais_id = medidorAtribGerais.id
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
                SELECT caracteristica.nome_da_caracteristica, caracteristica.valorPadrao
                FROM medidor
                INNER JOIN medidorFamilia ON medidor.medidorFamilia_id = medidorFamilia.id
                INNER JOIN medidorModelo ON medidorModelo.medidorFamilia_id = medidorFamilia.id
                INNER JOIN medidorAtribGerais ON medidor.medidorAtribGerais_id = medidorAtribGerais.id
                INNER JOIN caracteristica ON caracteristica.medidorAtribGerais_id =  medidorAtribGerais.id
                WHERE medidor.id = """ + str(meterID) + """;
                """
        return self.sql

    def whichQuery(self, idS, idQ):
        #id 1 procurar por familia
        if idS == 1:
            self.cur.execute(self.queryByFamily(idQ))
        #id 2 procurar por modelo
        elif idS == 2:
            self.cur.execute(self.queryByModel(idQ))
        #id 3 procurar por usuario que cadastrou
        elif idS == 3:
            self.cur.execute(self.queryByUser(idQ))
        #id 4 procurar por numero de série eletra (somente numeros)
        elif idS == 4:
            self.cur.execute(self.queryByEletraPartNumber(idQ))
        #id 5 procurar por apenas caracteristicas de um medidor especifico
        elif idS == 5:
            self.cur.execute(self.queryCaracteristics(idQ))
        else:
            print("ID não existente")

    def convertSql(self):
        self.results = self.cur.fetchall()
        self.rowarray = {}
        self.columns = [desc[0] for desc in self.cur.description]
        for self.row in self.results:
            self.d = dict(zip(self.columns, self.row))
            self.rowarray.update(self.d)
        return self.rowarray

    def convertFeatures(self):
        self.results = self.cur.fetchall()
        self.rowarray = {}
        self.columns = [desc[0] for desc in self.cur.description]
        for self.row in self.results:
            self.d = {}
            self.d[self.row[0]] = self.row[1]
            self.rowarray.update(self.d)
        return self.rowarray;

    #
    def QueryMedidorFull(self, idQ):
        self.whichQuery(2,idQ)
        self.rowarray = self.convertSql();
        self.whichQuery(5, idQ)
        self.rowarray2 = self.convertFeatures();
        self.rowarray.update(self.rowarray2)
        return self.rowarray

    def date_handler(self, obj):
        if hasattr(obj, 'isoformat'):
            return obj.isoformat()
        else:
            raise TypeError

    def saveFile(self, rowarray):
        with open('data.json', 'w') as outfile:
            json.dump(rowarray, outfile, True, default=self.date_handler, indent = 4, ensure_ascii=False)


#Ex:
meter = TDS()
print meter.QueryMedidorFull(1)
meter.saveFile(meter.QueryMedidorFull(1))
