class Joueur:

    def __init__(self, nom, carteatt):
        self.nb_vote = 0
        self.envie = True
        self.nom = nom
        self.carteatt = carteatt    #carteatt pour carte attribuée
        self.amoureux = None
    
    def mourir(self):
        self.envie = False
        print("Le joueur", self.nom, "est mort cette nuit ...")
    
    def ressuciter(self):
        self.envie = True
        print("Le joueur", self.nom, "a été ressucité cette nuit !!!")
    
    def voter(self, cible):
        vote = int(input(f"{self.nom}, qui votez-vous (insérer nombre) ? "))
        return vote