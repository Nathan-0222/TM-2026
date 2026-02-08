
class Livre():

    def __init__(self, titre, auteur, etat):
        self.titre = titre
        self.auteur = auteur
        self.etat = etat

    def degrade(self):
        if self.etat > 0:
            self.etat -= 1

    def description(self):
        print("Titre :", self.titre)
        print("Auteur :",self.auteur)
        print("Etat :", self.etat)

class Bibliotheque:

    def __init__(self):
        self.livres = []

    def ajoute(self, livre):
        self.livres.append(livre)

    def supprime_livres_abimes(self):
        for livre in self.livres:
            if livre.etat == 0:
                self.livres.remove(livre)

    def inventaire(self):
        print("---------------")
        print("contenu de ma bibliothèque :")
        print("---------------")
        for livre in self.livres:
            livre.description()
            print()
ma_bibli = Bibliotheque()
livre1 = Livre("Les Misérables", "Victor Hugo", 3)
livre2 = Livre("Les fleurs du mal", "Charles Baudelaire", 1)
livre1.description()
ma_bibli.ajoute(livre1)
ma_bibli.ajoute(livre2)
ma_bibli.inventaire()
