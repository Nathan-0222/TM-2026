class Joueur:

    def __init__(self, nom, carteatt):
        self.nb_vote = 0
        self.envie = True
        self.nom = nom
        self.carteatt = carteatt    #carteatt pour carte attribuée
        self.amoureux = None
    
    def mourir(self):

        self.envie = False

        if self.amoureux != None:
            if self.amoureux.envie == True:
                self.amoureux.mourir()
    
    def ressuciter(self):
        self.envie = True
    
    def voter(self):
        vote = int(input(f"{self.nom}, qui votez-vous (insérer nombre) ? "))
        return vote