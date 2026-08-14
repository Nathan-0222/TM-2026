class Carte:
    # Classe mère 
    def __init__(self):
        pass

    
    def afficher_description(self):
        pass
        
    #Comment faires les actions de nuit et gérer les pouvoirs ?

class Sorciere(Carte):
    def __init__(self):
        self.nom = "Sorciere"
        self.description = "La capacité de votre carte est que pendant la partie, vous pouvez 1 seule fois ressusciter 1 joueur mort, et 1 seule fois en tuer 1. Faites les bons choix pour sauver le village des loups..."
        self.potion_vie = 1
        self.potion_mort = 1
    
    def utiliser_potion_vie(self):
        if self.potion_vie ==1:
            self.potion_vie -= 1
    
    def utiliser_potion_mort(self):
        if self.potion_mort ==1:
            self.potion_mort -= 1

    def capacite_sorciere(self, index_victime, liste_joueurs, choix_sorciere):

        sauve_par_sorciere = False
        victime_sorciere = None

        if choix_sorciere == 1:

            if self.potion_vie == 1:

                self.utiliser_potion_vie()
                sauve_par_sorciere = True

            else:

                pass


        elif choix_sorciere == 2:

            if self.potion_mort == 1:

                self.utiliser_potion_mort()
                victime_sorciere = liste_joueurs[index_victime]

            else:

                pass


        return sauve_par_sorciere, victime_sorciere
       
        
class LoupGarou(Carte):
    def __init__(self):
        self.nom="Loup-Garou"
        self.description="La capacité de votre carte est que, avec vos coéquipiers durant la nuit, vous pouvez en vous mettant d'accord tuer un joueur. Votre but est que vous soyez les derniers survivants !!!"
    
    def capacite_loupgarou(self):
        pass



class Chasseur(Carte):
    def __init__(self, joueur_qui_a_la_carte=None, liste_joueurs=None):
        self.nom="Chasseur"
        self.description="La capacité de votre carte est que, lorsque vous mourrez, vous pouvez tuer n'importe quel joueur en vie. Faites le bon choix avant votre dernier souffle..."
        self.joueur_qui_a_la_carte = joueur_qui_a_la_carte
        self.liste_joueurs = liste_joueurs

    
    def capacite_chasseur(self, index_cible):
    
        if self.joueur_qui_a_la_carte.envie == False:

            n = int(input("Quel est le numéro du joueur que vous souhaitez tuer avant de mourir ? "))
            
            self.liste_joueurs[index_cible].mourir()

        else:

            pass

        
class Voyante(Carte):
    def __init__(self):
        self.nom="Voyante"
        self.description="La capacité de votre carte est que, durant chaque tour pendant la nuit, vous avez le droit de connaître la carte du joueur de votre choix..."

    def capacite_voyante(self, liste_joueurs, index_joueur):

        carte_de_la_cible = liste_joueurs[index_joueur].carteatt.nom
        return f"La carte de {liste_joueurs[index_joueur].nom} est : {carte_de_la_cible}"
    

class PetiteFille(Carte):
    def __init__(self):
            self.nom="Petite-Fille" 
            self.description="La capacité de votre carte est que, lors du tour des loups garous uniquement, vous pouvez tricher en les observant discrètement en ouvrant vos yeux. Faites attention à ne pas être repéré, car vous risqueriez de..."


class Cupidon(Carte):
    def __init__(self):
            self.nom="Cupidon" 
            self.description="La capacité de votre carte est que vous pouvez mettre en couple deux personnes dans la partie. Un seul couple peut-être en vie à la fois. Si un des deux partenaires meurt, l'autre mourra aussi-tôt dans la tristesse..."

    def capacite_cupidon(self, liste_joueurs, index_j1, index_j2):

        joueur1 = liste_joueurs[index_j1]
        joueur2 = liste_joueurs[index_j2]

        joueur1.amoureux = joueur2
        joueur2.amoureux = joueur1

      
class Villageois(Carte):
    def __init__(self):
        self.nom="Villageois" 
        self.description="Votre carte n'a malheureusement pas de capacité spéciale durant la nuit, vous devrez donc être le plus à l'affût possible durant le vote !!!"


class Voleur(Carte):
    def __init__(self):
            self.nom="Voleur"
            self.description="La capacité de votre carte est que, durant votre tour, vous pouvez échanger cette carte avec la carte d'un autre joueur choisi. Ne gâchez pas cette aptitude en faisant le mauvais choix !!!"

    def capacite_voleur(self, liste_joueurs, choix_voleur, index_cible_voleur):

        voleur_joueur = None
        for j in liste_joueurs:
            if j.carteatt.nom == "Voleur":
                voleur_joueur = j
        
        if choix_voleur == True:

            cible = liste_joueurs[index_cible_voleur]

            carte_temporaire = voleur_joueur.carteatt
            voleur_joueur.carteatt = cible.carteatt
            cible.carteatt = carte_temporaire

        else:

            pass
