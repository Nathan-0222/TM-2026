class Carte:
    # Classe mère 
    # def __init__(self):

    
    def afficher_description(self):
        print(f"{self.nom} : {self.description}")
        
    #Comment faires les actions de nuit et gérer les pouvoirs ?

class Sorciere(Carte):
    def __init__(self):
        self.role = "Sorcière"
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
        super().__init__(
            nom="Loup-Garou", 
            description="La capacité de votre carte est que, avec vos coéquipiers durant la nuit, vous pouvez en vous mettant d'accord tuer un joueur. Votre but est que vous soyez les derniers survivants !!!"
        )
    
    def voter_victime(self):
        pass

class Chasseur(Carte):
    def __init__(self):
        super().__init__(
            nom="Chasseur", 
            description="La capacité de votre carte est que, lorsque vous mourrez, vous pouvez tuer n'importe quel joueur en vie. Faites le bon choix avant votre dernier souffle..."
        )
        
class Voyante(Carte):
    def __init__(self):
        super().__init__(
            nom="Voyante", 
            description="La capacité de votre carte est que, durant chaque tour pendant la nuit, vous avez le droit de connaître la carte du joueur de votre choix..."
        )

class PetiteFille(Carte):
    def __init__(self):
        super().__init__(
            nom="Petite-Fille", 
            description="La capacité de votre carte est que, lors du tour des loups garous uniquement, vous pouvez tricher en les observant discrètement en ouvrant vos yeux. Faites attention à ne pas être repéré, car vous risqueriez de..."
        )

class Cupidon(Carte):
    def __init__(self):
        super().__init__(
            nom="Cupidon", 
            description="La capacité de votre carte est que vous pouvez mettre en couple deux personnes dans la partie. Un seul couple peut-être en vie à la fois. Si un des deux partenaires meurt, l'autre mourra aussi-tôt dans la tristesse..."
        )

class Villageois(Carte):
    def __init__(self):
        super().__init__(
            nom="Villageois", 
            description="Votre carte n'a malheureusement pas de capacité spéciale durant la nuit, vous devrez donc être le plus à l'affût possible durant le vote !!!"
        )

class Voleur(Carte):
    def __init__(self):
        super().__init__(
            nom="Voleur", 
            description="La capacité de votre carte est que, durant votre tour, vous pouvez échanger cette carte avec la carte d'un autre joueur choisi. Ne gâchez pas cette aptitude en faisant le mauvais choix !!!"
        )





class Joueur:

    def __init__(self, nom, carteatt):
        self.nb_vote = 0
        self.envie = True
        self.nom = nom
        self.carteatt = carteatt    #carteatt pour carte attribuée
    
    def mourir(self):
        self.envie = False
        print("Le joueur", self.nom, "est mort cette nuit ...")
    
    def ressuciter(self):
        self.envie = True
        print("Le joueur", self.nom, "a été ressucité cette nuit !!!")
    
    def voter(self, cible):
        #Comment faire pour créer une liste pour chaque joueur enregistré 
        vote = int(input(f"{self.nom}, qui votez-vous (insérer nombre) ? "))
        return vote
        

    



class Partie:
    def __init__(self, mdp):
        self.mdp = mdp
        self.liste_joueurs = [] 
        self.loups_garous = []
        self.villageois = []

    def ajouter_joueur(self, nom_joueur):
        nouveau_joueur = Joueur(nom_joueur, None) 
        self.liste_joueurs.append(nouveau_joueur)
        print(nom_joueur, "a rejoint la partie !")

    def distribuer_cartes (self):
        #Comment faire en sorte de distribuer une carte pour chaque joueur selon la composition de cartes dans la partie (Elle qui dépend du nb. de joueurs)
        pass

    def vote_de_jour(self):

        print("Voici la liste des joueurs : ")
        for i in range(len(self.liste_joueurs)):
            print(f"{i + 1} - {self.liste_joueurs[i].nom}")

        liste_votes = [0] * len(self.liste_joueurs)

        for joueur in self.liste_joueurs:
            vote = joueur.voter() - 1
            liste_votes[vote] += 1


partie = Partie("ciao")

c1 = Sorciere()

# j1 = Joueur("Nathan", c1) # ici il faudrait passer que le nom, la carte dans un deuxième temps

partie.ajouter_joueur("Nathan")
partie.ajouter_joueur("Ilaria")
print(partie.liste_joueurs)

elimine = partie.liste_joueurs.pop(1)
print(f"{elimine.nom} est éliminé !")
print(partie.liste_joueurs)