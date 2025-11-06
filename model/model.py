from database.museo_DAO import MuseoDAO
from database.artefatto_DAO import ArtefattoDAO

'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di MuseoDAO e ArtefattoDAO)
'''

class Model:
    def __init__(self):
        self._museo_dao = MuseoDAO()
        self._artefatto_dao = ArtefattoDAO()

    # --- ARTEFATTI ---
    def get_artefatti_filtrati(self, museo:str, epoca:str):
        """Restituisce la lista di tutti gli artefatti filtrati per museo e/o epoca (filtri opzionali)."""
        #recuperiamo tutti i musei per trovare l'id corrispondente
        musei = self._museo_dao.get_all_museums()

        #se utente sceglie 'Nessun filtro' o non seleziona nulla?

        if museo == 'Nessun filtro' or museo is None:
            id_museo = None
        else :
            #cerchiamo id del museo corrispondente a nome selzionato
            #next() = restituisce il primo elemento del generatore che soddisfa la condizione
            #con secondo argomento None se non trova nulla restituisce None

            id_museo = next((mus.id for mus in musei if mus.nome == museo), None)

        if epoca == 'Nessun filtro' or epoca is None:
            epoca = None
        else:
            epoca = epoca.strip().lower()


        #viene interrogato il DAO e viene restituita la lista di oggetti Artefatto

        return self._artefatto_dao.get_artefatti_filtrati(id_museo, epoca)

    def get_epoche(self):
        """Restituisce la lista di tutte le epoche."""

        epoche = self._artefatto_dao.get_all_epoche()
        return['Nessun filtro'] + epoche


    # --- MUSEI ---
    def get_musei(self):
        """ Restituisce la lista di tutti i musei."""

        musei = self._museo_dao.get_all_museums()
        return ['Nessun filtro'] + [mus.nome for mus in musei]

