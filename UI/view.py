import flet as ft
from UI.alert import AlertManager

"""
VIEW:
- Rappresenta l'interfaccia utente
- Riceve i dati dal MODELLO e li presenta senza modificarli
"""

class View:
    def __init__(self, page: ft.Page):
        # Page setup
        self.page = page
        self.page.title = "Lab07"
        self.page.horizontal_alignment = "center"
        self.page.theme_mode = ft.ThemeMode.DARK

        # Alert
        self.alert = AlertManager(page)

        # Controller (verrà collegato dopo)
        self.controller = None

    def set_controller(self, controller):
        self.controller = controller

    def update(self):
        self.page.update()

    def show_alert(self, messaggio):
        self.alert.show_alert(messaggio)

    # --- INTERFACCIA ---
    def load_interface(self):
        """Crea e aggiunge gli elementi della UI alla pagina."""

        # Sezione 1: Titolo
        self.txt_titolo = ft.Text(value="Musei di Torino", size=38, weight=ft.FontWeight.BOLD)

        # Sezione 2: Filtraggio
        self.dropdown_musei = ft.Dropdown(label="Museo", width=200)
        self.dropdown_epoche = ft.Dropdown(label="Epoca", width=200)
        self.btn_mostra_artefatti = ft.ElevatedButton(text="Mostra Artefatti")

        self.filtri_col = ft.Column(
            controls=[
                ft.Row(controls= [self.dropdown_musei, self.dropdown_epoche],
                        alignment="center",
                        spacing=20
                ),
                ft.Row(controls= [self.btn_mostra_artefatti],
                       alignment="center"
                       )
                ],
            alignment="center",
            spacing=10)




        # Sezione 3: Lista artefatti
        self.lista_artefatti = ft.ListView(expand=True, spacing=10, padding=10)

        # Toggle Tema
        self.toggle_cambia_tema = ft.Switch(label="Tema scuro", value=True, on_change=self.cambia_tema)

        # Layout completo
        self.page.add(
            self.toggle_cambia_tema,
            self.txt_titolo,
            ft.Divider(),

            # Sezione 2: Filtraggio
            self.filtri_col,
            ft.Divider(),

            # Sezione 3: Artefatti
            self.lista_artefatti,
        )

        self.page.scroll = "adaptive"
        self.page.update()

    # --- TEMA SCURO/CHIARO ---
    def cambia_tema(self, e):
        """Cambia il tema scuro/chiaro"""
        self.page.theme_mode = ft.ThemeMode.DARK if self.toggle_cambia_tema.value else ft.ThemeMode.LIGHT
        self.toggle_cambia_tema.label = "Tema scuro" if self.toggle_cambia_tema.value else "Tema chiaro"
        self.page.update()

