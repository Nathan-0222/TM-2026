from pathlib import Path   #sert pour les images -> ou est ce qu'on peut les trouver
from nicegui import ui, app
from partie import *

dossier_images = Path(__file__).parent / 'image'   #indique chemin d'accès depuis l'endroit que lance le terminal initialement
dossier_sons = Path(__file__).parent / 'sons'   #même chose que pour images
app.add_static_files('/image', dossier_images)
app.add_static_files('/sons', dossier_sons)

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
        nb = len(partie_en_cours.liste_joueurs)
        if nb >= 7:   #Petit détail encore, tant que plus grand que 7 bouton commencer tojours affichable, mais dès que + que 15 joueurs impossible d'ajjouter nouveau joueur (boutons non visibles)
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
            ui.notify('Entrez un nom', type="warning")
            return
        
        if len(partie_en_cours.liste_joueurs) >= 15:   #Petit changement, avant cela autorisait jusqu'à 16 joueurs (> et pas >=)
            ui.notify('Maximum 15 joueurs !!', type='warning')
            return

        if partie_en_cours.ajouter_joueur(nom) == False:   #Petit détail encore, notification si nom déja pris (lié avec la fonction ajouter joueur dans partie.py)
            ui.notify('Ce nom est déjà pris !', type='negative')
            return

        partie_en_cours.ajouter_joueur(nom)
        champ_nom.value = ""   #supp la valeur mise pour mettre case vide

        zone_liste_accueil.refresh()
        zone_bouton_commencer.refresh()

    ui.button('Ajouter ce joueur', on_click=cliquer_ajouter)
        



@ui.page('/jeu')
def page_liens():

    if partie_en_cours.phase == "inscription":
        ui.navigate.to('/')
        return

    ui.label('Jeu du Loup Garou')
    ui.separator()
    ui.label('Chaque joueur doit cliquer sur son nom pour ouvrir sa fenêtre privée !!')

    for i in range(len(partie_en_cours.liste_joueurs)):
        nom_j = partie_en_cours.liste_joueurs[i].nom
        ui.button(nom_j, on_click=lambda i=i: ui.navigate.to(f'/joueur/{i}', new_tab = True))

    nb_joues = [0]   #combien de sons ont été joués
    occupe = [False]   #savoir si son est déjà en cours. évite que sons "écrasé"

    @ui.refreshable
    def zone_sons():
        if occupe[0] == True:
            lecteur = partie_en_cours.messages[nb_joues[0]].jouer()   #lance le son à l'instance de la valeur de la variable nb_joues : si nb_joues = 1 alors cela prendra le 2ème message de la liste paartie_en_cours.messages et jouera l'audio
            lecteur.on('ended', son_fini)
            lecteur.on('error', son_erreur)

    def son_erreur():   #débuguage : voir quels sons sont pas lancés
        ui.notify('Fichier introuvable : ' + partie_en_cours.messages[nb_joues[0]].cle + '.mp3')
        son_fini()

    def son_fini():   #mentionne que son est fini -> nouveau peut jouer donc occupe[0] devient False
        nb_joues[0] += 1
        occupe[0] = False
        zone_sons.refresh()

    def verifier_son():
        if occupe[0] == False and nb_joues[0] < len(partie_en_cours.messages):   #Si aucun son joue (occupe = False) alors possible de lancer le prochain son, si d'autres messages ont été crées en ce temps
            occupe[0] = True
            zone_sons.refresh()

    def lancer_naration():
        ui.timer(0.3, verifier_son)   #verifie si possible de lancer son toutes les 0,3 secondes

    ui.separator()
    ui.button("Lancer la Narration ", on_click=lancer_naration)
    zone_sons()



@ui.page('/joueur/{id_joueur}')
def page_joueur(id_joueur: int):

    if partie_en_cours.phase == "inscription":
        ui.navigate.to('/')
        return

    joueur_actuel = partie_en_cours.liste_joueurs[id_joueur]
    choix_cupidon = []

    with ui.column().classes('w-full h-screen justify-between items-center text-center p-6 pb-40 overflow-hidden'):     #pour que tout centré : h-screen pour 100% de la hauteur de l'écran / p-6 pour la padding comme en CSS (sert à mettre une marge pour que les elements touchent pas le bord) / justify-between pour répartir éléments page verticalement / overflow-hidden pour le non-scroll(masqué) / pb-10 pour marge en bas qui permet que texte colle pas

        ui.label('Fenêtre de : ' + joueur_actuel.nom)
        ui.label('Votre carte est : ' + joueur_actuel.carteatt.nom)
        ui.image(f'/image/{joueur_actuel.carteatt.nom}.webp').classes('w-30')
        with ui.expansion('Description de ma carte'):   #sert à afficher description de la carte pour ceux qui ne connaissent pas les règles
            ui.label(joueur_actuel.carteatt.description)
        ui.separator()


        @ui.refreshable
        def zone_message():
            ui.label(partie_en_cours.message.texte)   #zone qui remplace print(message jeu)
            if joueur_actuel.carteatt.message_prive != "":
                ui.label("Message privé : " + joueur_actuel.carteatt.message_prive)


        @ui.refreshable
        def zone_joueurs():   #zone affichant constamment la liste des joueurs (plus simple)
            if len(partie_en_cours.liste_joueurs) == 0:
                return

            ui.label("Voiçi la liste des joueurs, cliquez dessus quand c'est à votre tour pour cibler :")


            def cliquer_cible(index_cible):

                if partie_en_cours.phase == "cupidon":
                    if index_cible in choix_cupidon:   #Permet que cupidon ne puisse pas définir deux fois le même amoureux
                        ui.notify('Choisissez deux joueurs différents !', type='warning')
                        return
                    choix_cupidon.append(index_cible)
                    if len(choix_cupidon) == 2:
                        partie_en_cours.action_cupidon(choix_cupidon[0], choix_cupidon[1])
                        choix_cupidon.clear()   #vider liste

                elif partie_en_cours.phase == "voleur":
                    if partie_en_cours.liste_joueurs[index_cible] is joueur_actuel:   #Voleur ne peut pas se voler lui-même
                        ui.notify('Vous ne pouvez pas vous voler vous-même !', type='warning')
                        return
                    partie_en_cours.action_voleur(True, index_cible)

                elif partie_en_cours.phase == "voyante":
                    partie_en_cours.action_voyante(index_cible)

                elif partie_en_cours.phase == "loups":
                    if joueur_actuel.nom not in partie_en_cours.a_deja_vote:
                        partie_en_cours.vote_de_nuit(index_cible, joueur_actuel.nom)

                elif partie_en_cours.phase == "sorciere":
                    partie_en_cours.action_sorciere(2, index_cible)
                                
                elif partie_en_cours.phase == "chasseur":
                    partie_en_cours.action_chasseur(index_cible)  

                elif partie_en_cours.phase == "vote_jour":
                    if joueur_actuel.nom not in partie_en_cours.a_deja_vote:
                        partie_en_cours.vote_de_jour(index_cible, joueur_actuel.nom)

                tout_rafraichir()

            est_mon_tour = ((partie_en_cours.phase == "cupidon" and joueur_actuel.carteatt.nom == "Cupidon" and joueur_actuel.envie == True) or
                        (partie_en_cours.phase == "voleur" and joueur_actuel.carteatt.nom == "Voleur" and joueur_actuel.envie == True) or
                        (partie_en_cours.phase == "voyante" and joueur_actuel.carteatt.nom == "Voyante" and joueur_actuel.envie == True) or
                        (partie_en_cours.phase == "loups" and joueur_actuel.carteatt.nom == "LoupGarou" and joueur_actuel.envie == True and joueur_actuel.nom not in partie_en_cours.a_deja_vote ) or
                        (partie_en_cours.phase == "sorciere" and joueur_actuel.carteatt.nom == "Sorciere" and joueur_actuel.envie == True) or
                        (partie_en_cours.phase == "chasseur" and joueur_actuel.carteatt.nom == "Chasseur" and joueur_actuel.envie == True) or
                        (partie_en_cours.phase == "vote_jour" and joueur_actuel.envie == True and joueur_actuel.nom not in partie_en_cours.a_deja_vote))   #sinon avant morts pouvaient voter
            

            with ui.row():   #permet de mettre boutons en ligne et pas en colonne
                for j in range(len(partie_en_cours.liste_joueurs)):
                    joueur = partie_en_cours.liste_joueurs[j]
                    nom_bouton = joueur.nom
                    if joueur is joueur_actuel:
                        nom_bouton = nom_bouton + " (vous)"

                    if joueur.envie == True:
                        bouton = ui.button(nom_bouton, on_click=lambda j=j: cliquer_cible(j)).props('color="positive"')   #si je mets pas i=i, vu que boucle sera fini, le i pointera forcément la dernière valeur de i qui est le dernier joueur de la liste
                        if est_mon_tour == False:
                            bouton.props('color="red"').disable()
                    else:
                        ui.button(nom_bouton + " (Mort : " + joueur.carteatt.nom + ")").props('color="grey"').disable()




        @ui.refreshable
        def zone_actions():


            #cupidon
            if partie_en_cours.phase == "cupidon" and joueur_actuel.carteatt.nom == "Cupidon":

                ui.label('Choisissez les deux amoureux :')


            #voleur
            elif partie_en_cours.phase == "voleur" and joueur_actuel.carteatt.nom == "Voleur":
                    
                ui.label("Le Voleur se réveille. Voulez-vous dérober la carte de quelqu'un ? (cliquez sur un joueur pour dérober sa carte)")
            
                def cliquer_voleur_non():
                    partie_en_cours.action_voleur(False, 0)
                    tout_rafraichir()

                ui.button("Non, je reste tranquille", on_click=cliquer_voleur_non)


            #voyante
            elif partie_en_cours.phase == "voyante" and joueur_actuel.carteatt.nom == "Voyante":

                ui.label("La Voyante se réveille. Choisissez un joueur à observer :")


            #verif carte pour voleur
            elif partie_en_cours.phase == "verif_carte":

                nb_vivants = 0
                for j in partie_en_cours.liste_joueurs:
                    if j.envie == True:
                        nb_vivants += 1

                ui.label("Tout le monde vérifie sa carte (en haut de l'écran)")
                ui.label(str(len(partie_en_cours.a_deja_vote)) + "/" + str(nb_vivants) + "ont déjà votés")

                def cliquer_carte_vue():
                    partie_en_cours.a_deja_vote.append(joueur_actuel.nom)

                    if len(partie_en_cours.a_deja_vote) == nb_vivants:
                        partie_en_cours.a_deja_vote = []   #réinitialise liste
                        partie_en_cours.annoncer("verif_carte_fin")
                        partie_en_cours.passer_phase_nuit("voleur")   #reprend nuit

                    tout_rafraichir()

                if joueur_actuel.envie == True and joueur_actuel.nom not in partie_en_cours.a_deja_vote:
                    ui.button("J'ai vu ma carte", on_click=cliquer_carte_vue)



            #loup
            elif partie_en_cours.phase == "loups":

                if joueur_actuel.carteatt.nom == "PetiteFille" and joueur_actuel.envie == True:
                    ui.label("(La Petite-Fille peut entre-ouvrir les yeux pour espionner...)")

                if joueur_actuel.carteatt.nom == "LoupGarou" and joueur_actuel.envie == True:   #rajout dàtail : affichage mieux pour combien de loups ont voté, et si c'est à son tour ou non de voter
                    nb_loups = 0
                    for j in partie_en_cours.liste_joueurs:
                        if j.carteatt.nom == "LoupGarou" and j.envie == True:
                            nb_loups += 1

                    ui.label("Mettez-vous d'accord, Loups-Garous, sinon le jeu tirera au hasard entre vos choix.")
                    ui.label(str(len(partie_en_cours.a_deja_vote)) + "/" + str(nb_loups) + " loup(s) ont voté")   #nouvel affichage
                    if joueur_actuel.nom in partie_en_cours.a_deja_vote:
                        ui.label("Vous avez voté, en attente des autres loups...")
                    else:
                        ui.label("C'est à vous de voter :")


            #sorciere
            elif partie_en_cours.phase == "sorciere" and joueur_actuel.carteatt.nom == "Sorciere":

                ui.label("La Sorcière se réveille.")
                if partie_en_cours.victime_loups != None:
                    ui.label("Les loups ont choisi : " + partie_en_cours.victime_loups.nom)
                ui.label("Il vous reste : " + str(joueur_actuel.carteatt.potion_vie) + " potion de vie et " + str(joueur_actuel.carteatt.potion_mort) + " potion de mort")

                def cliquer_sauver():
                    partie_en_cours.action_sorciere(1, 0)
                    tout_rafraichir()

                def cliquer_rien():
                    partie_en_cours.action_sorciere(3, 0)
                    tout_rafraichir()

                if joueur_actuel.carteatt.potion_vie == 1 and partie_en_cours.victime_loups != None:   #Comme ça présent que si besoin
                    ui.button("Sauver la victime", on_click=cliquer_sauver)
                ui.button("Ne rien faire", on_click=cliquer_rien)


            elif partie_en_cours.phase == "chasseur" and joueur_actuel.carteatt.nom == "Chasseur":

                ui.label("Le Chasseur tire sa dernière balle ! Choisissez sa cible :")


            #matin
            elif partie_en_cours.phase == "matin":


                ui.label('--- LE VILLAGE SE REVEILLE ---')
                if partie_en_cours.vérification_victoire():
                    tout_rafraichir()
                    return

                else:
                    def cliquer_passer_au_vote():
                        partie_en_cours.a_deja_vote = []
                        for j in partie_en_cours.liste_joueurs:
                            j.nb_vote = 0
                        partie_en_cours.phase = "vote_jour"
                        partie_en_cours.annoncer("vote", "--- LE VILLAGE VOTE ---\nChaque joueur vivant vote pour éliminer un suspect.")
                        tout_rafraichir()

                ui.button("Passer au vote du village →", on_click=cliquer_passer_au_vote)


            #vote matin
            elif partie_en_cours.phase == "vote_jour":

                nb_vivants = 0   #même affichage ue pour les loups
                for j in partie_en_cours.liste_joueurs:
                    if j.envie == True:
                        nb_vivants += 1

                ui.label(str(len(partie_en_cours.a_deja_vote)) + "/" + str(nb_vivants) + " joueurs ont voté")   #nouvel affichage
                if joueur_actuel.envie == True:
                    if joueur_actuel.nom in partie_en_cours.a_deja_vote:
                        ui.label("Vous avez voté, en attente des autres...")
                    else:
                        ui.label("C'est à vous de voter :")
                else:
                    ui.label("Vous êtes mort, vous ne pouvez plus voter.")


            #fin potentiel
            elif partie_en_cours.phase == "fin":

                ui.label("La partie est terminée !")
                ui.button("Retour à l'accueil", on_click=lambda: ui.navigate.to('/'))


        def tout_rafraichir():
            zone_message.refresh()
            zone_actions.refresh()
            zone_joueurs.refresh()



        zone_message()
        ui.separator()
        zone_joueurs()
        ui.separator()
        zone_actions()

        dernier_etat = {   #inspirer du modèle pour raffraîchir les pages des différents joueurs dans le fichier app3.py de la prof
            "phase" : partie_en_cours.phase,
            "messages" : partie_en_cours.message.texte,
            "nb_morts" : 0,
            "nb_votes" : len(partie_en_cours.a_deja_vote),
            "prive" : joueur_actuel.carteatt.message_prive,
            "carte" : joueur_actuel.carteatt.nom   #pour bug voleur aussi
        }

        def verifier_changements():

            nb_morts = 0
            for j in partie_en_cours.liste_joueurs:
                if j.envie == False:
                    nb_morts += 1

            etat_actuel = {
                "phase" : partie_en_cours.phase,
                "messages" : partie_en_cours.message.texte,
                "nb_morts" : nb_morts,
                "nb_votes" : len(partie_en_cours.a_deja_vote),
                "prive" : joueur_actuel.carteatt.message_prive,
                    "carte" : joueur_actuel.carteatt.nom   #pour bug voleur aussi
            }

            phases_nuit = ["nuit", "cupidon", "voleur", "voyante", "loups", "sorciere", "verif_carte"]
            if partie_en_cours.phase in phases_nuit:
                if partie_en_cours.phase == "loups" and joueur_actuel.carteatt.nom == "LoupGarou":
                    ui.query('body').style('background-color: #990000; color: white; margin: 0; padding: 0; overflow: hidden')   #notation rgb pour couleur rouge vif / margin: 0; ... sert à éliminer barre de scroll latérale et verticale non nécéssaire
                else:
                    ui.query('body').style('background-color: #121212; color: white; margin: 0; padding: 0; overflow: hidden')   #notation rgb pour couleur noir
            else:
                ui.query('body').style('background-color: #ffffff; color: black; margin: 0; padding: 0; overflow: hidden')   #notation rgb pour couleur blanc

            ui.query('.q-separator').style('background-color: #38bdf8; width: 80%; margin: auto')   #les ui.separator ne se voyaient pas dans la nuit car noir, alors là ils sont tout le temps en bleau clair pour être vus dans les deux (.q-separator désigne donc les ui.separator crées)

            if etat_actuel["carte"] != dernier_etat["carte"]:   #bug voleur : carte affichés sur personne concerné ne change pas
                ui.navigate.reload()
                return

            if (etat_actuel["messages"] != dernier_etat["messages"]) or (etat_actuel["prive"] != dernier_etat["prive"]) :
                zone_message.refresh()

            if (etat_actuel["phase"] != dernier_etat["phase"] or etat_actuel["nb_votes"] != dernier_etat["nb_votes"] or etat_actuel["nb_morts"] != dernier_etat["nb_morts"]):
                zone_joueurs.refresh()
                zone_actions.refresh()

            dernier_etat.update(etat_actuel)

        ui.timer(0.5, verifier_changements)



ui.run(title="Loup Garou", reload=False, port=8086)