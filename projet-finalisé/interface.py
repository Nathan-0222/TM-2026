from nicegui import ui
from partie import *

partie_en_cours = Partie("ciao")

@ui.page('/acceuil')
def page_acceuil():

    ui.label('Bienvenu dans ce jeu du Loup-Garou')
    ui.label('Inscrivez de 7 à 15 joueurs pour commencer !!')
    ui.separator()

    champ_nom = ui.input(label = 'Nom du joueur')

    @ui.refreshable   #zone affichant l'état de l'inscription des joeurs
    def zone_liste_accueil():
        if len(partie_en_cours.liste_joueurs) == 0:
            ui.label('Aucun joueur inscrit pour le moment')
        else:
            ui.label(str(len(partie_en_cours.liste_joueurs)) + 'joueur(s) inscrit(s) :')
            for j in range (len(partie_en_cours.liste_joueurs)):
                ui.label(str(j+1) + ' - ' + partie_en_cours.liste_joueurs[j].nom)

    @ui.refreshable
    def zone_bouton_commencer():
        if len(partie_en_cours.liste_joueurs) > 7 and len(partie_en_cours.liste_joueurs) < 15:

            def cliquer_commencer():
                partie_en_cours.commencer_partie()
                ui.navigate.to(/jeu)

            ui.button('Commencer Partie', on_click=cliquer_commencer)

        else:
            nb_manquants = 7 - len(partie_en_cours.liste_joueurs)
            ui.label('Vous êtes pas assez pour commencer la partie, il vous manque' + str(nb_manquants) + 'joueurs pour commencer')

    zone_liste_accueil()
    ui.separator()
    zone_bouton_commencer()
    ui.separator()

    def cliquer_ajouter():
        nom = champ_nom.value
        if nom == "":
            return
        
        if len(partie_en_cours.liste_joueurs) > 15:
            return

        partie_en_cours.ajouter_joueur(nom)
        champ_nom.value = ""   #supprime la valeur mise pour mettre case vide

        zone_liste_accueil.refresh()
        zone_bouton_commencer.refresh()

    ui.button('Ajouter ce joueur', on_click=cliquer_ajouter)
        



@ui.page('/jeu')
def zone_jeu():
    pass