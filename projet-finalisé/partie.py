import random
from joueur import *
from carte import *

class Partie:
    def __init__(self, mdp):
        self.mdp = mdp
        self.liste_joueurs = [] 
        self.loups_garous = []
        self.villageois = []
        self.sorcière = None
        self.petite_fille = None

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
             self.liste_joueurs[i].carteatt = self.pioche[i]

        print("Les rôles sont attribuées !!!")
        



    def vote_de_jour(self):

        self.affiche_joueurs()

        liste_votes = [0] * len(self.liste_joueurs)

        for joueur in self.liste_joueurs:
            vote = joueur.voter() - 1
            liste_votes[vote] += 1
        
        index_max = liste_votes.index(max(liste_votes))
        print("Le joueur", self.liste_joueurs[index_max].nom,"est mort cette nuit")
        self.liste_joueurs[index_max].mourir()

    def vérification_victoire(self):

        loups = 0
        villageois = 0
        for j in self.liste_joueurs:
            if j.envie == True:
                if j.carteatt.nom == "Loup-Garou":
                    loups += 1
                else:
                    villageois += 1

        if loups == 0 :
            print("\nVICTOIRE ! Tous les Loups-Garous sont morts, les Villageois gagnent !")
            return True
        elif loups >= villageois:
            print("\nDÉFAITE ! Les Loups-Garous sont assez nombreux pour dévorer le reste du village.")
            return True
        else:
            return False
    
    def affiche_joueurs(self):
        print("Voici la liste des joueurs : ")
        for i in range(len(self.liste_joueurs)):
            if self.liste_joueurs[i].envie:
                print(f"{i + 1} - {self.liste_joueurs[i].nom}")
            else:
                print(f"{i + 1} - décédé")

        
    def vote_de_nuit(self):
        
        self.affiche_joueurs()

        liste_votes = [0] * len(self.liste_joueurs)

        for j in self.liste_joueurs:
            print(j.carteatt.nom)
            if j.carteatt.nom == "Loup-Garou" and j.envie == True:
                vote = j.voter() - 1
                liste_votes[vote] += 1
        
        index_max = liste_votes.index(max(liste_votes))
        victime = self.liste_joueurs[index_max]
        victime.mourir()
        return victime
        
    


    
    def run(self):

        self.ajouter_joueur()
        self.distribuer_cartes()

        print("\n=== DÉBUT DE LA PARTIE ===")
        premiere_nuit = True 
        
        while True:
            # 1. PHASE DE NUIT
            print("\n--- LA NUIT TOMBE ---")
            print("Le village s'endort, tout le monde ferme les yeux.")

            if premiere_nuit:
                for j in self.liste_joueurs:
                    if j.carteatt.nom == "Cupidon" and j.envie == True:
                        print("\nCupidon se réveille.")
                        j.carteatt.capacite_cupidon(self.liste_joueurs)      #pas encore fait
                        print("Cupidon se rendort.")
            
            premiere_nuit = False 

            for j in self.liste_joueurs:
                if j.carteatt.nom == "Voleur" and j.envie == True:
                    print("\nLe Voleur se réveille.")
                    j.carteatt.capacite_voleur(self.liste_joueurs)    #pas encore fait
                    print("Le Voleur se rendort.")

            for j in self.liste_joueurs:
                if j.carteatt.nom == "Voyante" and j.envie == True:
                    print("\nLa Voyante se réveille.")
                    j.carteatt.capacite_voyante(self.liste_joueurs) 
                    print("La Voyante se rendort.")

            print("\nLes Loups-Garous se réveillent pour choisir leur victime...")
            
            for j in self.liste_joueurs:
                if j.carteatt.nom == "Petite-Fille" and j.envie == True:
                    print("(La Petite-Fille peut entre-ouvrir les yeux pour espionner...)")

            victime = self.vote_de_nuit()


            print("Les Loups-Garous se rendorment.")

            for j in self.liste_joueurs:
                if j.carteatt.nom == "Sorciere" and j.envie == True:
                    print("\nLa Sorcière se réveille.")
                    j.carteatt.capacite_sorciere(victime, self.liste_joueurs) 
                    print("La Sorcière se rendort.")

            # 2. PHASE DE JOUR (RÉVEIL)

            print("\n--- LE SOLEIL SE LÈVE ---")
            print("Le village se réveille.")

            # Regarder si Victime est morte ou pas au final et l'annoncer !!!!!!!

            if victime.envie == False:
                print("Malheureusement,", victime.nom, "nous a quitté cette nuit..")

            else:
                print("Personne n'est mort cette nuit !!!")

                                                           #Comment annoncer la victime qui a pu être tué par la sorcière si potion de mort utiliser ????????????????????????????????????????????????????????????
            
            # VÉRIFICATION DE VICTOIRE
            
            if self.vérification_victoire():
                break
       
            # 3. PHASE DE JOUR (LE VOTE)
          
            self.vote_de_jour()
            
            # --- VÉRIFICATION DE VICTOIRE (après le vote) ---

            if self.vérification_victoire():
                break
