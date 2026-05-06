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
        print("\n=== DÉBUT DE LA PARTIE ===")
        premiere_nuit = True 
        
        while True:
            # 1. PHASE DE NUIT
            print("\n--- LA NUIT TOMBE ---")
            print("Le village s'endort, tout le monde ferme les yeux.")
            
            if premiere_nuit:
                for j in self.liste_joueurs:
                    if j.carteatt.nom == "Voleur" and j.envie == True:
                        print("\nLe Voleur se réveille.")
                        # On suppose que tu lui passes la liste globale comme vu ensemble
                        j.carteatt.capacite_voleur(self.liste_joueurs) 
                        print("Le Voleur se rendort.")

            if premiere_nuit:
                for j in self.liste_joueurs:
                    if j.carteatt.nom == "Cupidon" and j.envie == True:
                        print("\nCupidon se réveille.")
                        j.carteatt.capacite_cupidon(self.liste_joueurs)
                        print("Cupidon se rendort.")
            
            premiere_nuit = False 

            for j in self.liste_joueurs:
                if j.carteatt.nom == "Voyante" and j.envie == True:
                    print("\nLa Voyante se réveille.")
                    j.carteatt.capacite_voyante() 
                    print("La Voyante se rendort.")

            print("\nLes Loups-Garous se réveillent pour choisir leur victime...")
            
            for j in self.liste_joueurs:
                if j.carteatt.nom == "Petite-Fille" and j.envie == True:
                    print("(La Petite-Fille peut entre-ouvrir les yeux pour espionner...)")

            for j in self.liste_joueurs:
                if j.carteatt.nom == "Loup-Garou" and j.envie == True:
                    j.carteatt.voter_victime() 
                    # Vote des loups à faire !!!!!!!!!!!!!!!!!
            print("Les Loups-Garous se rendorment.")

            for j in self.liste_joueurs:
                if j.carteatt.nom == "Sorciere" and j.envie == True:
                    print("\nLa Sorcière se réveille.")
                    # Comment gérer le passement de la victime des loups à la sorcière ??????????????
                    j.carteatt.capacite_sorciere() 
                    print("La Sorcière se rendort.")

            # 2. PHASE DE JOUR (RÉVEIL)

            print("\n--- LE SOLEIL SE LÈVE ---")
            print("Le village se réveille.")
            # Regarder si Victime est morte ou pas au final et l'annoncer !!!!!!!
            
            # VÉRIFICATION DE VICTOIRE
            loups = 0
            villageois = 0
            for j in self.liste_joueurs:
                if j.envie == True:
                    if j.carteatt.nom == "Loup-Garou":
                        loups += 1
                    else:
                        villageois += 1

            if loups == 0:
                print("\nVICTOIRE ! Tous les Loups-Garous sont morts, les Villageois gagnent !")
                break 
            elif loups >= villageois:
                print("\nDÉFAITE ! Les Loups-Garous sont assez nombreux pour dévorer le reste du village.")
                break
       
            # 3. PHASE DE JOUR (LE VOTE)
          
            print("\nIl est temps de débattre et de voter pour éliminer un suspect.")
            
            resultats_votes = [0] * len(self.liste_joueurs)
            
            for j in self.liste_joueurs:
                if j.envie == True:
                    # On demande à chaque joueur vivant de voter
                    print(f"\n C'est à {j.nom} de voter.")
                    choix = j.voter(None) 
                    resultats_votes[choix - 1] += 1 
            
            # Résolution du vote
            max_votes = max(resultats_votes)
            index_elimine = resultats_votes.index(max_votes)
            joueur_elimine = self.liste_joueurs[index_elimine]
            
            print(f"\n Le village a tranché. {joueur_elimine.nom} est condamné.")
            joueur_elimine.mourir()
            
            # --- VÉRIFICATION DE VICTOIRE (après le vote) ---
            loups = 0
            villageois = 0
            for j in self.liste_joueurs:
                if j.envie == True:
                    if j.carteatt.nom == "Loup-Garou":
                        loups += 1
                    else:
                        villageois += 1

            if loups == 0:
                print("\nVICTOIRE ! Tous les Loups-Garous sont morts, les Villageois gagnent !")
                break
            elif loups >= villageois:
                print("\nDÉFAITE ! Les Loups-Garous sont assez nombreux pour dévorer le reste du village.")
                break