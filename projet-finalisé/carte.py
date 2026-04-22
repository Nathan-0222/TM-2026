class Carte:
    # Classe mère 
    # def __init__(self):

    
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
        
class LoupGarou(Carte):
    def __init__(self):
            self.nom="Loup-Garou", 
            self.description="La capacité de votre carte est que, avec vos coéquipiers durant la nuit, vous pouvez en vous mettant d'accord tuer un joueur. Votre but est que vous soyez les derniers survivants !!!"
    
    def voter_victime(self):
        pass

class Chasseur(Carte):
    def __init__(self, joueur_qui_a_la_carte=None, liste_joueurs=None):
            self.nom="Chasseur", 
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
            self.nom="Voyante", 
            self.description="La capacité de votre carte est que, durant chaque tour pendant la nuit, vous avez le droit de connaître la carte du joueur de votre choix..."
    
    def capacite_voyante(self):
            
            print("Voici la liste des joueurs : ")
            for i in range(len(self.liste_joueurs)):
                print(f"{i + 1} - {self.liste_joueurs[i].nom}")

            n = int(input("Quelle est le numéro du joueur que vous souhaitez voir ?"))

            carte_de_la_cible = self.liste_joueurs[n-1].carteatt.nom
            print(f"La carte de {self.liste_joueurs[n-1].nom} est : {carte_de_la_cible}")

class PetiteFille(Carte):
    def __init__(self):
            self.nom="Petite-Fille", 
            self.description="La capacité de votre carte est que, lors du tour des loups garous uniquement, vous pouvez tricher en les observant discrètement en ouvrant vos yeux. Faites attention à ne pas être repéré, car vous risqueriez de..."

class Cupidon(Carte):
    def __init__(self):
            self.nom="Cupidon", 
            self.description="La capacité de votre carte est que vous pouvez mettre en couple deux personnes dans la partie. Un seul couple peut-être en vie à la fois. Si un des deux partenaires meurt, l'autre mourra aussi-tôt dans la tristesse..."

class Villageois(Carte):
    def __init__(self):
            self.nom="Villageois", 
            self.description="Votre carte n'a malheureusement pas de capacité spéciale durant la nuit, vous devrez donc être le plus à l'affût possible durant le vote !!!"

class Voleur(Carte):
    def __init__(self):
            self.nom="Voleur", 
            self.description="La capacité de votre carte est que, durant votre tour, vous pouvez échanger cette carte avec la carte d'un autre joueur choisi. Ne gâchez pas cette aptitude en faisant le mauvais choix !!!"
