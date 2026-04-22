import random
from joueur import *
from carte import *

class Partie:
    def __init__(self, mdp):
        self.mdp = mdp
        self.liste_joueurs = [] 
        self.loups_garous = []
        self.villageois = []

    def ajouter_joueur(self):

        nj = int(input("Combien de joueurs (entre 7 et 15) ?"))
        while nj < 7 or nj > 15:
            nj = int(input("Valeur invalide, rentrez une valeur entre 7 et 15 : "))  

        for i in range(nj):
            nom_joueur = input(f"Nom du joueur {i+1}: ")
            nouveau_joueur = Joueur(nom_joueur, None) 
            self.liste_joueurs.append(nouveau_joueur)
            print(nom_joueur, "a rejoint la partie !")

    def distribuer_cartes (self):
        self.nombre = len(self.liste_joueurs)
        self.pioche = []

        print("Dans ce jeu du loup-garou, vous devez être de 7 à 15 joueurs maximum pour jouer")

        if self.nombre == 7:
             self.pioche = [LoupGarou(), LoupGarou(), Voyante(), Sorciere(), Villageois(), Villageois(), Villageois()]
             print("La composition de la partie est :")
             for carte in self.pioche:
                print("-", carte.nom)
        elif self.nombre == 8:
             self.pioche = [LoupGarou(), LoupGarou(), Voyante(), Sorciere(), Chasseur(), Villageois(), Villageois(), Villageois()]
             print("La composition de la partie est :")
             for carte in self.pioche:
                print("-", carte.nom)
        elif self.nombre == 9:
             self.pioche = [LoupGarou(), LoupGarou(), Voyante(), Sorciere(), Chasseur(), Cupidon(), Villageois(), Villageois(), Villageois()]
             print("La composition de la partie est :")
             for carte in self.pioche:
                print("-", carte.nom)
        elif self.nombre == 10:
             self.pioche = [LoupGarou(), LoupGarou(), LoupGarou(), Voyante(), Sorciere(), Chasseur(), PetiteFille(), Villageois(), Villageois(), Villageois()]
             print("La composition de la partie est :")
             for carte in self.pioche:
                print("-", carte.nom)
        elif self.nombre == 11:
             self.pioche = [LoupGarou(), LoupGarou(), LoupGarou(), Voyante(), Sorciere(), Cupidon(), PetiteFille(), Villageois(), Villageois(), Villageois(), Villageois()]
             print("La composition de la partie est :")
             for carte in self.pioche:
                print("-", carte.nom)
        elif self.nombre == 12:
             self.pioche = [LoupGarou(), LoupGarou(), LoupGarou(), Voyante(), Sorciere(), Chasseur(), PetiteFille(), Cupidon(), Voleur(), Villageois(), Villageois(), Villageois()]
             print("La composition de la partie est :")
             for carte in self.pioche:
                print("-", carte.nom)
        elif self.nombre == 13:
             self.pioche = [LoupGarou(), LoupGarou(), LoupGarou(), Voyante(), Sorciere(), Chasseur(), PetiteFille(), Cupidon(), Voleur(), Villageois(), Villageois(), Villageois(), Villageois()]
             print("La composition de la partie est :")
             for carte in self.pioche:
                print("-", carte.nom)
        elif self.nombre == 14:
             self.pioche = [LoupGarou(), LoupGarou(), LoupGarou(), Voyante(), Sorciere(), Chasseur(), PetiteFille(), Cupidon(), Voleur(), Villageois(), Villageois(), Villageois(), Villageois(), Villageois()]
             print("La composition de la partie est :")
             for carte in self.pioche:
                print("-", carte.nom)
        elif self.nombre == 15:
             self.pioche = [LoupGarou(), LoupGarou(), LoupGarou(), Voyante(), Sorciere(), Chasseur(), PetiteFille(), Cupidon(), Voleur(), Villageois(), Villageois(), Villageois(), Villageois(), Villageois(), Villageois()]
             print("La composition de la partie est :")
             for carte in self.pioche:
                print("-", carte.nom)
        
        random.shuffle (self.pioche)

        for i in range (self.nombre):
             self.liste_joueurs[i].carteatt = pioche[i]

        print("Les rôles sont attribuées !!!")
        



    def vote_de_jour(self):

        print("Voici la liste des joueurs : ")
        for i in range(len(self.liste_joueurs)):
            print(f"{i + 1} - {self.liste_joueurs[i].nom}")

        liste_votes = [0] * len(self.liste_joueurs)

        for joueur in self.liste_joueurs:
            vote = joueur.voter() - 1
            liste_votes[vote] += 1


    
    def run(self):

        self.ajouter_joueur()
        self.distribuer_cartes()

        print("Que le village s'endorme...")