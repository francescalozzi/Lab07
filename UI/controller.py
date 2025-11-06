import flet as ft
from UI.view import View
from model.model import Model

"""
CONTROLLER:
- Intermediario tra MODELLO e VIEW
- Gestisce la logica dell'applicazione
"""

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.museo_selezionato = None
        self.epoca_selezionata = None

        # POPOLA DROPDOWN
        self.popola_dropdown()

        # Imposta le callback
        self._view.dropdown_musei.on_change = self.callback_museo
        self._view.dropdown_epoche.on_change = self.callback_epoca

        # Imposta l'azione del bottone
        self._view.btn_mostra_artefatti.on_click = self.mostra_artefatti

    #POPOLA DROPDOWN
    def popola_dropdown(self):
        musei = self._model.get_musei()
        epoche = self._model.get_epoche()

        self._view.dropdown_musei.options = [ft.dropdown.Option(m) for m in musei]
        self._view.dropdown_epoche.options = [ft.dropdown.Option(e) for e in epoche]

        self._view.dropdown_musei.value = musei[0]
        self._view.dropdown_epoche.value = epoche[0]

        self._view.update()

    #CALLBACKS DROPDOWN
    def callback_museo(self, e):
        # e. control = oggetto grafico (DropDown) che genera l'evento in questo caso la selezione di un museo
        #e.control.value = valore selezionato dall'utente
        self.museo_selezionato = e.control.value
        #self.mostra_artefatti(e) --> in questo modo non dovrei schiacciare il bottone 'Mostra artefatti'

    def callback_epoca(self, e):
        self.epoca_selezionata = e.control.value
        #self.mostra_artefatti(e) --> in questo modo non dovrei schiacciare il bottone 'Mostra artefatti'

    #AZIONE: MOSTRA ARTEFATTI
    def mostra_artefatti(self, e):
        museo = self.museo_selezionato or "Nessun filtro"
        epoca = self.epoca_selezionata or "Nessun filtro"

        artefatti = self._model.get_artefatti_filtrati(museo, epoca)

        self._view.lista_artefatti.controls.clear()

        if not artefatti:
            self._view.show_alert("Nessun artefatto trovato per i filtri selezionati.")
        else:
            for a in artefatti:
                self._view.lista_artefatti.controls.append(ft.Text(str(a)))

        self._view.update()

