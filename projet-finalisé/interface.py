from nicegui import ui
from partie import *

partie = None

@ui.page('/acceuil')
def acceuil():
    ui.label('Jeu du Loup-Garou')