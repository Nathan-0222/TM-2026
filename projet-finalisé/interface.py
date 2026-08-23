from nicegui import ui
from partie import *

partie_en_cours = Partie("ciao")

@ui.page('/')
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
        if len(partie_en_cours.liste_joueurs) >= 7 and len(partie_en_cours.liste_joueurs) < 15:

            def cliquer_commencer():
                partie_en_cours.commencer_partie()
                ui.navigate.to('/jeu')

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
        ui.navigate.to('/')
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

                ui.label('Cupidon se réveille. Choisissez les deux amoureux :')
                champ_j1 = ui.number(label='Numéro du 1er joueur', value=1, min=1, max=len(partie_en_cours.liste_joueurs))
                champ_j2 = ui.number(label='Numéro du 2ème joueur', value=1, min=1, max=len(partie_en_cours.liste_joueurs))

                def cliquer_cupidon():
                    index_j1 = int(champ_j1.value) - 1
                    index_j2 = int(champ_j2.value) - 1
                    partie_en_cours.action_cupidon(index_j1, index_j2)
                    zone_message.refresh()
                    zone_joueurs.refresh()
                    zone_actions.refresh()

                ui.button('Valider le couple', on_click=cliquer_cupidon)

            #else:   sert plus à rien vu que la partie vérifie automatiquement et s'il esst là il y aura forcément l'action

                #partie_en_cours.passer_phase_nuit("cupidon")
                #zone_message.refresh()
                #zone_actions.refresh()


        #voleur
        elif partie_en_cours.phase == "voleur":
                
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


        #voyante
        elif partie_en_cours.phase == "voyante":

                ui.label("La Voyante se réveille. Choisissez un joueur à observer :")
                champ_cible = ui.number(label="Numéro du joueur à observer", value=1, min=1, max=len(partie_en_cours.liste_joueurs))
        
                def cliquer_voyante():
                    index_cible = int(champ_cible.value) - 1
                    partie_en_cours.action_voyante(index_cible)
                    zone_message.refresh()
                    zone_joueurs.refresh()
                    zone_actions.refresh()
        
                ui.button("Regarder", on_click=cliquer_voyante)


        #loup
        elif partie_en_cours.phase == "loups":

            for j in partie_en_cours.liste_joueurs:
                if j.carteatt.nom == "Petite-Fille" and j.envie == True:
                    ui.label("(La Petite-Fille peut entre-ouvrir les yeux pour espionner...)")

            loup_actuel = None
            for j in partie_en_cours.liste_joueurs:
                if j.carteatt.nom == "Loup-Garou" and j.envie == True:
                    if j.nom not in partie_en_cours.a_deja_vote:
                        loup_actuel = j
                        break

            if loup_actuel != None:
                ui.label("C'est au tour de " + loup_actuel.nom + " (Loup-Garou) de voter :")
                champ_cible = ui.number(label="Numéro de la victime", value=1, min=1, max=len(partie_en_cours.liste_joueurs))

                def cliquer_vote_loup():
                    index_cible = int(champ_cible.value) - 1
                    partie_en_cours.vote_de_nuit(index_cible, loup_actuel.nom)
                    zone_message.refresh()
                    zone_joueurs.refresh()
                    zone_actions.refresh()

                ui.button("Voter", on_click=cliquer_vote_loup)


        #sorciere
        elif partie_en_cours.phase == "sorciere":

            potions = None   
            for j in partie_en_cours.liste_joueurs:
                if j.carteatt.nom == "Sorciere" and (j.envie == True or j == partie_en_cours.victime_loups):
                    potions = j.carteatt

            if potions != None:   #joue pas si pas de potion
                ui.label("La Sorcière se réveille.")
                if partie_en_cours.victime_loups != None:
                    ui.label("Les loups ont choisi : " + partie_en_cours.victime_loups.nom)
                ui.label("Il vous reste : " + str(potions.potion_vie) + " potion de vie et " + str(potions.potion_mort) + " potion de mort")
                ui.label("Choisissez  1 = sauver la victime, 2 = tuer quelqu'un, 3 = ne rien faire")

                champ_choix = ui.number(label="Votre choix (1, 2 ou 3)", value=3, min=1, max=3)
                champ_cible_mort = ui.number(label="Si choix 2 : numéro du joueur à tuer", value=1, min=1, max=len(partie_en_cours.liste_joueurs))

                def cliquer_sorciere():
                    choix = int(champ_choix.value)
                    index_cible_mort = int(champ_cible_mort.value) - 1
                    partie_en_cours.action_sorciere(choix, index_cible_mort)
                    zone_message.refresh()
                    zone_joueurs.refresh()
                    zone_actions.refresh()

                ui.button("Valider", on_click=cliquer_sorciere)


        elif partie_en_cours.phase == "chasseur":

            ui.label("Le Chasseur tire sa dernière balle ! Choisissez sa cible :")
            champ_cible = ui.number(label="Choisissez le numéro de votre cible :", value=1, min=1, max=len(partie_en_cours.liste_joueurs))

            def tir_chasseur():
                partie_en_cours.action_chasseur(int(champ_cible.value) - 1)
                zone_message.refresh()
                zone_joueurs.refresh()
                zone_actions.refresh()

            ui.button("Tirer", on_click=tir_chasseur)


        #matin
        elif partie_en_cours.phase == "matin":


            ui.label('--- LE VILLAGE SE REVEILLE ---')
            if partie_en_cours.vérification_victoire():
                zone_message.refresh()
                zone_joueurs.refresh()
                zone_actions.refresh()
                return

            else:
                def cliquer_passer_au_vote():
                    partie_en_cours.a_deja_vote = []
                    for j in partie_en_cours.liste_joueurs:
                        j.nb_vote = 0
                    partie_en_cours.phase = "vote_jour"
                    partie_en_cours.message = "--- LE VILLAGE VOTE ---\nChaque joueur vivant vote pour éliminer un suspect."
                    zone_message.refresh()
                    zone_joueurs.refresh()
                    zone_actions.refresh()

            ui.button("Passer au vote du village →", on_click=cliquer_passer_au_vote)


        #vote matin
        elif partie_en_cours.phase == "vote_jour":

            votant_actuel = None
            for j in partie_en_cours.liste_joueurs:
                if j.envie == True and j.nom not in partie_en_cours.a_deja_vote:
                    votant_actuel = j
                    break

            if votant_actuel != None:
                ui.label("C'est au tour de " + votant_actuel.nom + " de voter :")
                champ_cible = ui.number(label="Numéro du joueur à éliminer", value=1, min=1, max=len(partie_en_cours.liste_joueurs))

                def cliquer_vote_jour():
                    index_cible = int(champ_cible.value) - 1
                    partie_en_cours.vote_de_jour(index_cible, votant_actuel.nom)
                    zone_message.refresh()
                    zone_joueurs.refresh()
                    zone_actions.refresh()

                ui.button("Voter", on_click=cliquer_vote_jour)


        #fin potentiel
        elif partie_en_cours.phase == "fin":

            ui.label("La partie est terminée !")
            ui.button("Retour à l'accueil", on_click=lambda: ui.navigate.to('/'))


    zone_message()
    ui.separator()
    zone_joueurs()
    ui.separator()
    zone_actions()


ui.run(title="Loup Garou", reload=False, port=8086)