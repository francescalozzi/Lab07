from database.DB_connect import ConnessioneDB
from model.museoDTO import Museo

"""
    Museo DAO
    Gestisce le operazioni di accesso al database relative ai musei (Effettua le Query).
"""

class MuseoDAO:
    def __init__(self):
        pass


    def get_all_museums(self):
        conn = ConnessioneDB.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM museo ORDER BY nome"
        cursor.execute(query)

        righe = cursor.fetchall()
        musei = [] #lista vuota dove accumuliamo gli oggetti Museo

        for riga in righe:
            museo = Museo(riga['id'],
                          riga['nome'],
                          riga['tipologia'])  #crea oggetto museo con valori della riga
            #si sarebbe anche potuto scrivere --> Museo(**riga) per una flessibilità più alta

            musei.append(museo)

        cursor.close()
        conn.close()
        return musei