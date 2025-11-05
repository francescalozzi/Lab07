from database.DB_connect import ConnessioneDB
from model.artefattoDTO import Artefatto

"""
    ARTEFATTO DAO
    Gestisce le operazioni di accesso al database relative agli artefatti (Effettua le Query).
"""

class ArtefattoDAO:
    def __init__(self):
        pass


    def get_all_epoche(self):
        conn = ConnessioneDB.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = ("SELECT DISTINCT epoca FROM artefatto ORDER BY epoca")
        cursor.execute(query)
        epoche = []

        righe = cursor.fetchall()
        for riga in righe:
            epoche.append(riga['epoca'])

        cursor.close()
        conn.close()
        return epoche

    def get_artefatti_filtrati(self, id_museo = None, epoca = None):
        # funzione che restituisce artefatti filtrati per museo e/o epoca
        # se uno dei due filtri è None il filtro non viene applicato

        conn = ConnessioneDB.get_connection()
        cursor = conn.cursor(dictionary=True)

        query = """ SELECT * FROM artefatto
                WHERE (%s IS NULL or id_museo = %s)
                AND (%s IS NULL or epoca = %s)
                ORDER BY nome"""

        parametri = (id_museo, id_museo, epoca, epoca)
        cursor.execute(query, parametri)

        artefatti = []

        righe = cursor.fetchall()
        for riga in righe:
            artefatto = Artefatto(**riga)
            artefatti.append(artefatto)

        cursor.close()
        conn.close()
        return artefatti

