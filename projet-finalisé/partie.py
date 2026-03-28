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