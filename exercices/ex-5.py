class CompteBancaire:
    def __init__ (self, titulaire, solde):
        self.titulaire = titulaire
        self.solde = solde
    def retrait(self, somme):
        if somme > self.solde:
            print ("Retrait impossible")
        else:
            self.somme -= somme
            print("Vous avez fait un retrait de", somme, "euros")
            print("Il vous reste", self.solde, "euros")
    def depot(self, somme)
        self.solde += somme
        print("Il vous reste", self.solde, "euros")
        print("Vous avez fait un ajout de", somme, "euros")

