class Carte:
    # Classe mère 
    def __init__(self):
        pass

    
    def afficher_description(self):
        print(f"{self.nom} : {self.description}")
        
    #Comment faires les actions de nuit et gérer les pouvoirs ?

class Sorciere(Carte):
    def __init__(self):
        self.nom = "Sorcière"
        self.description = "La capacité de votre carte est que pendant la partie, vous pouvez 1 seule fois ressusciter 1 joueur mort, et 1 seule fois en tuer 1. Faites les bons choix pour sauver le village des loups..."
        self.potion_vie = 1
        self.potion_mort = 1
    
    def utiliser_potion_vie(self):
        if self.potion_vie ==1:
            self.potion_vie -= 1
        else:
            print("Pas de potion disponible")
    
    def utiliser_potion_mort(self):
        if self.potion_mort ==1:
            self.potion_mort -= 1
        else:
            print("Pas de potion disponible")

    def capacite_sorciere(self, victime, liste_joueurs):
        print(f"Le joueur {victime.nom} a été choisi par les loups.")
        x = int(input("Que voulez vous utiliser, choisissez 1 pour la potion de vie en le ressucitant, 2 pour la potion de mort afin d'éliminer quelqu'un et 3 pour ne rien faire :"))
        if x == 1:
            self.utiliser_potion_vie()
            victime.ressuciter()
        elif x == 2:

            print("Voici la liste des joueurs : ")
            for i in range(len(liste_joueurs)):
                print(f"{i + 1} - {liste_joueurs[i].nom}")
            
            victime2 = int(input("Quel est le numéro de la personne que vous voulez tuer ?"))
            liste_joueurs[victime2-1].mourir()

        else:
            victime.mourir()

         
        
class LoupGarou(Carte):
    def __init__(self):
        self.nom="Loup-Garou"
        print(self.nom) 
        self.description="La capacité de votre carte est que, avec vos coéquipiers durant la nuit, vous pouvez en vous mettant d'accord tuer un joueur. Votre but est que vous soyez les derniers survivants !!!"
    
    def capacite_loupgarou(self):
        pass



class Chasseur(Carte):
    def __init__(self, joueur_qui_a_la_carte=None, liste_joueurs=None):
        self.nom="Chasseur"
        self.description="La capacité de votre carte est que, lorsque vous mourrez, vous pouvez tuer n'importe quel joueur en vie. Faites le bon choix avant votre dernier souffle..."
        self.joueur_qui_a_la_carte = joueur_qui_a_la_carte
        self.liste_joueurs = liste_joueurs

    
    def capacite_chasseur(self):
    
        if self.joueur_qui_a_la_carte.envie == False:
            print("Voici la liste des joueurs : ")
        
            for i in range(len(self.liste_joueurs)):
                print(f"{i + 1} - {self.liste_joueurs[i].nom}")    #Est ce que ca marche comme ca en utilisant le self.liste_joueurs ou je dois changer qqch ?

            n = int(input("Quel est le numéro du joueur que vous souhaitez tuer avant de mourir ? "))
            
            self.liste_joueurs[n-1].mourir()

        else:
            print("Vous ne pouvez pas encore utiliser votre capacité.")


        
class Voyante(Carte):
    def __init__(self):
        self.nom="Voyante"
        self.description="La capacité de votre carte est que, durant chaque tour pendant la nuit, vous avez le droit de connaître la carte du joueur de votre choix..."

    def capacite_voyante(self, liste_joueurs):
            
        print("Voici la liste des joueurs : ")
        for i in range(len(liste_joueurs)):
            print(f"{i + 1} - {liste_joueurs[i].nom}")

        n = int(input("Quelle est le numéro du joueur que vous souhaitez voir ?"))

        carte_de_la_cible = liste_joueurs[n-1].carteatt.nom
        print(f"La carte de {liste_joueurs[n-1].nom} est : {carte_de_la_cible}")

class PetiteFille(Carte):
    def __init__(self):
            self.nom="Petite-Fille" 
            self.description="La capacité de votre carte est que, lors du tour des loups garous uniquement, vous pouvez tricher en les observant discrètement en ouvrant vos yeux. Faites attention à ne pas être repéré, car vous risqueriez de..."

class Cupidon(Carte):
    def __init__(self):
            self.nom="Cupidon" 
            self.description="La capacité de votre carte est que vous pouvez mettre en couple deux personnes dans la partie. Un seul couple peut-être en vie à la fois. Si un des deux partenaires meurt, l'autre mourra aussi-tôt dans la tristesse..."

    def capacite_cupidon(self, liste_joueurs):

        print("Voici la liste des joueurs : ")
        for i in range(len(liste_joueurs)):
                print(f"{i + 1} - {liste_joueurs[i].nom}")

        j1 = int(input("Quel est le numéro du premier joueur voudriez vous mettre en couple ? :"))
        j2 = int(input("Quel est le numéro du deuxième joueur voudriez vous mettre en couple ? :"))

        joueur1 = liste_joueurs[j1 - 1]
        joueur2 = liste_joueurs[j2 - 1]

        joueur1.amoureux = joueur2
        joueur2.amoureux = joueur1

        print("Cupidon a bien tiré sa flèche et a mis au monde un tout nouveau couple !!")
      
class Villageois(Carte):
    def __init__(self):
        self.nom="Villageois" 
        self.description="Votre carte n'a malheureusement pas de capacité spéciale durant la nuit, vous devrez donc être le plus à l'affût possible durant le vote !!!"

class Voleur(Carte):
    def __init__(self):
            self.nom="Voleur"
            self.description="La capacité de votre carte est que, durant votre tour, vous pouvez échanger cette carte avec la carte d'un autre joueur choisi. Ne gâchez pas cette aptitude en faisant le mauvais choix !!!"

    def capacite_voleur(self, liste_joueurs):

        voleur_joueur = None
        for j in range(liste_joueurs):
            if j.carteatt.nom == "Voleur":
                voleur_joueur = j

        a = input("Voulez vous dérobez la carte de quelqu'un cette nuit ? (oui/non) :")
        
        if a == "oui" or "Oui" or "OUI":

            print("Voici la liste des joueurs : ")
            for i in range(len(liste_joueurs)):
                print(f"{i + 1} - {liste_joueurs[i].nom}")

            n = int(input("Quel est le numéro du joueur que vous souhaitez cambrioler cette nuit ? :"))

            cible = liste_joueurs[n-1]

            carte_temporaire = voleur_joueur.carteatt
            voleur_joueur.carteatt = cible.carteatt
            cible.carteatt = carte_temporaire

            print("Le voleur a bien dérobé la maison de quelqu'un parmi nous cette nuit.. N'oubliez pas de fairre attention !!")

        else:

            print("Le voleur a décidé de rester tranquillement chez lui cette nuit")

