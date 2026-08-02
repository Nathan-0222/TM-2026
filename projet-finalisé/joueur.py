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
                print("Malheursement, son partenaire étant", self.amoureux.nom, "meurt de chagrin suite à son décès, sa carte était :", self.amoureux.carteatt.nom)
    
    def ressuciter(self):
        self.envie = True
        print("Le joueur", self.nom, "a été ressucité cette nuit !!!")
    
    def voter(self):
        vote = int(input(f"{self.nom}, qui votez-vous (insérer nombre) ? "))
        return vote