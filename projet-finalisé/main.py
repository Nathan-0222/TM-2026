class Carte:
    
    def __init__(self, nomcarte, ):
        self.nomcarte = nomcarte
        


class Joueur:

    def __init__(self, nom, carteatt):
        self.en_vie = True
        self.nom = nom
        self.carteatt = carteatt    #carteatt pour carte attribuée
    
    def mourir(self):
        self.en_vie = False
        print("Le joueur", self.nom, "est mort cette nuit ...")
    
    def ressuciter(self):
        self.en_vie = True
        print("Le joueur", self.nom, "a été ressucité cette nuit !!!")
    
    def voter(cible):

    



class Partie:
    
    L = []      #Liste du nb. de joueurs
    nombre-joueurs = len(L)    #nb. de joueurs afin de savoir combien de cartes distribuées
    
    def __init__ (self, mdp):
        self.mdp = mdp
         