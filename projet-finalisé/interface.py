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

        ui.label("Voiçi la liste des joueurs, cliquez dessus quand c'est à votre tour pour cibler :")

        choix_cupidon = []

        def cliquer_cible(index_cible):

            if partie_en_cours.phase == "cupidon":
                choix_cupidon.append(index_cible)
                if len(choix_cupidon) == 2:
                    partie_en_cours.action_cupidon(choix_cupidon[0], choix_cupidon[1])
                    choix_cupidon.clear()   #vider liste

            elif partie_en_cours.phase == "voleur":
                partie_en_cours.action_voleur(True, index_cible)

            elif partie_en_cours.phase == "voyante":
                partie_en_cours.action_voyante(index_cible)

            elif partie_en_cours.phase == "loups":
                loup_actuel = None
                for j in partie_en_cours.liste_joueurs:
                    if j.carteatt.nom == "Loup-Garou" and j.envie == True:
                        if j.nom not in partie_en_cours.a_deja_vote:
                            loup_actuel = j
                            break

                if loup_actuel != None:
                    partie_en_cours.vote_de_nuit(index_cible, loup_actuel.nom)

            elif partie_en_cours.phase == "sorciere":
                partie_en_cours.action_sorciere(2, index_cible)
                            
            elif partie_en_cours.phase == "chasseur":
                partie_en_cours.action_chasseur(index_cible)  

            elif partie_en_cours.phase == "vote_jour":
                votant_actuel = None
                for j in partie_en_cours.liste_joueurs:
                    if j.envie == True and j.nom not in partie_en_cours.a_deja_vote:
                        votant_actuel = j
                        break

                if votant_actuel != None:
                    partie_en_cours.vote_de_jour(index_cible, votant_actuel.nom)

            zone_joueurs.refresh()
            zone_message.refresh()
            zone_actions.refresh()

                
        for j in range(len(partie_en_cours.liste_joueurs)):
            if partie_en_cours.liste_joueurs[j].envie == True:
                ui.button(partie_en_cours.liste_joueurs[j].nom, on_click = lambda j=j :cliquer_cible(j)).props('color="positive"')   #si je mets pas i=i, vu que boucle sera fini, le i pointera forcément la dernière valeur de i qui est le dernier joueur de la liste
            else:
                ui.button(partie_en_cours.liste_joueurs[j].nom + " (Mort)").props('color="gray"').disable()




    @ui.refreshable
    def zone_actions():


        #cupidon
        if partie_en_cours.phase == "cupidon":

                ui.label('Cupidon se réveille. Choisissez les deux amoureux :')


        #voleur
        elif partie_en_cours.phase == "voleur":
                
                ui.label("Le Voleur se réveille. Voulez-vous dérober la carte de quelqu'un ? (cliquez sur un joueur pour dérober sa carte)")
        
                def cliquer_voleur_non():
                    partie_en_cours.action_voleur(False, 0)
                    zone_message.refresh()
                    zone_joueurs.refresh()
                    zone_actions.refresh()

                ui.button("Non, je reste tranquille", on_click=cliquer_voleur_non)


        #voyante
        elif partie_en_cours.phase == "voyante":

                ui.label("La Voyante se réveille. Choisissez un joueur à observer :")


        #loup
        elif partie_en_cours.phase == "loups":

            for j in partie_en_cours.liste_joueurs:
                if j.carteatt.nom == "Petite-Fille" and j.envie == True:
                    ui.label("(La Petite-Fille peut entre-ouvrir les yeux pour espionner...)")


            ui.label("Veuillez à vous mettre d'accord les Loups-Garous, si vous ne le faites pas le jeu déterminera au hasard entre vos choix la victime finale.")
            loup_actuel = None
            for j in partie_en_cours.liste_joueurs:
                if j.carteatt.nom == "Loup-Garou" and j.envie == True:
                    if j.nom not in partie_en_cours.a_deja_vote:
                        loup_actuel = j
                        break

            if loup_actuel != None:
                ui.label("C'est au tour de " + loup_actuel.nom + " (Loup-Garou) de voter :")


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

                def cliquer_sauver():
                    partie_en_cours.action_sorciere(1, 0)
                    zone_message.refresh()
                    zone_joueurs.refresh()
                    zone_actions.refresh()

                def cliquer_rien():
                    partie_en_cours.action_sorciere(3, 0)
                    zone_message.refresh()
                    zone_joueurs.refresh()
                    zone_actions.refresh()

                ui.button("Sauver la victime", on_click=cliquer_sauver)
                ui.button("Ne rien faire", on_click=cliquer_rien)


        elif partie_en_cours.phase == "chasseur":

            ui.label("Le Chasseur tire sa dernière balle ! Choisissez sa cible :")


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