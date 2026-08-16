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
        champ_nom.value = ""   #supp la valeur mise pour mettre case vide

        zone_liste_accueil.refresh()
        zone_bouton_commencer.refresh()

    ui.button('Ajouter ce joueur', on_click=cliquer_ajouter)
        



@ui.page('/jeu')
def page_jeu():

    if partie_en_cours.phase == "inscription":
        ui.navigate.to('/accueil')
        return

    ui.label('Jeu du Loup Garou')
    ui.separator()


    @ui.refreshable
    def zone_message():
        ui.label(partie_en_cours.message)   #zone qui remplace print(message jeu)


    @ui.refreshable
    def zone_joueurs():   #zone affichant constamment la liste des joueurs (plus simple)
        if len(partie_en_cours.liste_joueurs) == 0:
            return
        ui.label('Voiçi la liste des joueurs :')
        for i in range (len(partie_en_cours.liste_joueurs)):
            if partie_en_cours.liste_joueurs[i].envie == True:
                ui.label(str(i + 1) + '-' + partie_en_cours.liste_joueurs[i].nom)
            else:
                ui.label('Décédé -' + partie_en_cours.liste_joueurs[i].nom)


    @ui.refreshable
    def zone_actions():


        #cupidon
        if partie_en_cours.phase == "cupidon":

            cupidon_present = False
            for j in range(len(partie_en_cours.liste_joueurs)):
                if j.carteatt.nom == "cupidon" and j.envie == True:
                    cupidon_present = True

            if cupidon_present == True:

                ui.label('Cupidon se réveille. Choisissez les deux amoureux :')
                champ_j1 = ui.number(label='Numéro du 1er joueur', value=1, min=1, max=len(partie_en_cours.liste_joueurs))
                champ_j2 = ui.number(label='Numéro du 2ème joueur', value=1, min=1, max=len(partie_en_cours.liste_joueurs))

                def cliquer_cupidon():
                    index_j1 = int(champ_j1) - 1
                    index_j2 = int(champ_j2) - 1
                    partie_en_cours.action_cupidon(index_j1, index_j2)
                    zone_message.refresh()
                    zone_joueurs.refresh()
                    zone_actions.refresh()

                ui.button('Valider le couple', on_click=cliquer_cupidon)

            else:

                partie_en_cours.passer_phase_suivante("cupidon")
                zone_message.refresh()
                zone_actions.refresh()


        #voleur
        elif partie_en_cours.phase == "voleur":
        
            voleur_present = False
            for j in partie_en_cours.liste_joueurs:
                if j.carteatt.nom == "Voleur" and j.envie == True:
                    voleur_present = True
        
            if voleur_present == True:
                ui.label("Le Voleur se réveille. Voulez-vous dérober la carte de quelqu'un ?")
                champ_cible = ui.number(label="Numéro du joueur à cambrioler", value=1, min=1, max=len(partie_en_cours.liste_joueurs))
        
                def cliquer_voleur_oui():
                    index_cible_voleur = int(champ_cible.value) - 1
                    partie_en_cours.action_voleur(True, index_cible_voleur)
                    zone_message.refresh()
                    zone_joueurs.refresh()
                    zone_actions.refresh()
        
                def cliquer_voleur_non():
                    partie_en_cours.action_voleur(False, 0)
                    zone_message.refresh()
                    zone_joueurs.refresh()
                    zone_actions.refresh()
        
                ui.button("Oui, je vole !", on_click=cliquer_voleur_oui)
                ui.button("Non, je reste tranquille", on_click=cliquer_voleur_non)
        
            else:
                partie_en_cours.passer_phase_nuit("voleur")
                zone_message.refresh()
                zone_actions.refresh()


        #voyante
        elif partie_en_cours.phase == "voyante":
        
            voyante_presente = False
            for j in partie_en_cours.liste_joueurs:
                if j.carteatt.nom == "Voyante" and j.envie == True:
                    voyante_presente = True
        
            if voyante_presente == True:
                ui.label("La Voyante se réveille. Choisissez un joueur à observer :")
                champ_cible = ui.number(label="Numéro du joueur à observer", value=1, min=1, max=len(partie_en_cours.liste_joueurs))
        
                def cliquer_voyante():
                    index_cible = int(champ_cible.value) - 1
                    partie_en_cours.action_voyante(index_cible)
                    zone_message.refresh()
                    zone_joueurs.refresh()
                    zone_actions.refresh()
        
                ui.button("Regarder", on_click=cliquer_voyante)
        
            else:
                partie_en_cours.passer_phase_nuit("voyante")
                zone_message.refresh()
                zone_actions.refresh()