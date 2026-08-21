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

        self.phase = "inscription"
        self.message = "Bonjour, inscrivez de 7 à 15 joueurs pour commencer !!"

        self.victime_loups = None
        self.sauve_par_sorciere = False
        self.victime_sorciere = None
        self.première_nuit = True

        self.a_deja_vote = []   #Liste pour savoir qui à déjà voté
        self.prochaine_phase = "matin"   #chasseur

    def ajouter_joueur(self, nom_joueur):
            
        nouveau_joueur = Joueur(nom_joueur, None) 
        self.liste_joueurs.append(nouveau_joueur)
        self.message = f"{nom_joueur} a rejoint la partie !!"

    def distribuer_cartes (self):
        self.nombre = len(self.liste_joueurs)
        self.pioche = []

        if self.nombre == 7:
             self.pioche = [LoupGarou(), LoupGarou(), Voyante(), Sorciere(), Villageois(), Villageois(), Villageois()]
             
        elif self.nombre == 8:
             self.pioche = [LoupGarou(), LoupGarou(), Voyante(), Sorciere(), Chasseur(), Villageois(), Villageois(), Villageois()]
             
        elif self.nombre == 9:
             self.pioche = [LoupGarou(), LoupGarou(), Voyante(), Sorciere(), Chasseur(), Cupidon(), Villageois(), Villageois(), Villageois()]
             
        elif self.nombre == 10:
             self.pioche = [LoupGarou(), LoupGarou(), LoupGarou(), Voyante(), Sorciere(), Chasseur(), PetiteFille(), Villageois(), Villageois(), Villageois()]
             
        elif self.nombre == 11:
             self.pioche = [LoupGarou(), LoupGarou(), LoupGarou(), Voyante(), Sorciere(), Cupidon(), PetiteFille(), Villageois(), Villageois(), Villageois(), Villageois()]
             
        elif self.nombre == 12:
             self.pioche = [LoupGarou(), LoupGarou(), LoupGarou(), Voyante(), Sorciere(), Chasseur(), PetiteFille(), Cupidon(), Voleur(), Villageois(), Villageois(), Villageois()]
            
        elif self.nombre == 13:
             self.pioche = [LoupGarou(), LoupGarou(), LoupGarou(), Voyante(), Sorciere(), Chasseur(), PetiteFille(), Cupidon(), Voleur(), Villageois(), Villageois(), Villageois(), Villageois()]
             
        elif self.nombre == 14:
             self.pioche = [LoupGarou(), LoupGarou(), LoupGarou(), Voyante(), Sorciere(), Chasseur(), PetiteFille(), Cupidon(), Voleur(), Villageois(), Villageois(), Villageois(), Villageois(), Villageois()]
            
        elif self.nombre == 15:
             self.pioche = [LoupGarou(), LoupGarou(), LoupGarou(), Voyante(), Sorciere(), Chasseur(), PetiteFille(), Cupidon(), Voleur(), Villageois(), Villageois(), Villageois(), Villageois(), Villageois(), Villageois()]

        self.message = "La composition de la partie est :\n"
        for carte in self.pioche:
            self.message = self.message + "-" + carte.nom + "\n"
        
        random.shuffle (self.pioche)

        for i in range (self.nombre):
             self.liste_joueurs[i].carteatt = self.pioche[i]

        self.message = "Les rôles sont attribuées !!!"


    def commencer_partie(self):

        self.distribuer_cartes()
        self.phase = "cupidon"
        self.première_nuit = True
        self.message = "Début de la partie \n --- LE VILLAGE S'ENDORT... ---"


    def passer_phase_nuit(self, phase_actuelle):

        if phase_actuelle == "cupidon":

            voleur_present = False
            for j in self.liste_joueurs:
                if j.carteatt.nom == "Voleur" and j.envie == True:
                    voleur_present = True

            if voleur_present == True:
                self.phase = "voleur"
                self.message = "Cupidon se rendort... \nLe Voleur se réveille !!"

            else:
                self.passer_phase_nuit("voleur")

        if phase_actuelle == "voleur":
        
            voyante_present = False
            for j in self.liste_joueurs:
                if j.carteatt.nom == "Voyante" and j.envie == True:
                    voyante_present = True
                    
            if voyante_present == True:
                self.phase = "voyante"
                self.message = "Le Voleur se rendort... \nLa Voyante se réveille !!"
                    
            else:
                self.passer_phase_nuit("voyante")

        if phase_actuelle == "voyante":
        
            self.phase = "loups"
            self.a_deja_vote = []
            for j in self.liste_joueurs:
                j.nb_vote = 0
            self.message = "La Voyante se rendort... \nLes Loups se réveillent pour choisir leur victime !!"

        
        if phase_actuelle == "loups":
        
            sorcière_present = False
            for j in self.liste_joueurs:
                if j.carteatt.nom == "Sorcière" and (j.envie == True or j == self.victime_loups):
                    sorcière_present = True
        
            if sorcière_present == True:
                self.phase = "sorciere"
                self.message = "Les Loups Garous se rendorment... \nLa Sorcière se réveille !!"
        
            else:
                self.passer_phase_nuit("sorciere")   #essai correction bug

        if phase_actuelle == "sorciere":
        
            self.resoudre_nuit()
    


    def action_cupidon(self, index_j1, index_j2):
    
        for j in self.liste_joueurs:
            if j.carteatt.nom == "Cupidon" and j.envie == True:
                j.carteatt.capacite_cupidon(self.liste_joueurs, index_j1, index_j2)
                self.message = "Cupidon a bien tiré sa flèche et a mis au monde un tout nouveau couple !!"
    
        self.passer_phase_nuit("cupidon")


    def action_voleur(self, choix_voleur, index_cible_voleur):

        for j in self.liste_joueurs:
            if j.carteatt.nom == "Voleur" and j.envie == True:
                j.carteatt.capacite_voleur(self.liste_joueurs, choix_voleur, index_cible_voleur)
                if choix_voleur == True:
                    self.message = "Le voleur a bien dérobé la carte de quelqu'un cette nuit !"
                else:
                    self.message = "Le voleur a décidé de rester tranquillement chez lui cette nuit."

        self.passer_phase_nuit("voleur")


    def action_voyante(self, index_joueur):
        
        for j in self.liste_joueurs:
            if j.carteatt.nom == "Voyante" and j.envie == True:
                j.carteatt.capacite_voyante(self.liste_joueurs, index_joueur)
                self.message = j.carteatt.capacite_voyante(self.liste_joueurs, index_joueur)
        
        self.passer_phase_nuit("voyante")


    def vote_de_nuit(self, index_cible, nom_du_loup):   #fait en sorte que quand un loup voteil esr enregistré dans la liste

        self.liste_joueurs[index_cible].nb_vote += 1
        self.a_deja_vote.append(nom_du_loup)   #vote enregistré
 
        loups_restants = 0   #je ferai dans interface.py en sorte que quand un loup a voté, tant que loups restants n'est pas egal à 0, le loup suivant votera
        for j in self.liste_joueurs:
            if j.carteatt.nom == "Loup-Garou" and j.envie == True:
                if j.nom not in self.a_deja_vote:
                    loups_restants += 1

        if loups_restants == 0:
 
            index_max = 0
            for i in range(len(self.liste_joueurs)):
                if self.liste_joueurs[i].nb_vote > self.liste_joueurs[index_max].nb_vote:
                    index_max = i
 
            self.victime_loups = self.liste_joueurs[index_max]
 
            for j in self.liste_joueurs:
                j.nb_vote = 0   #compteur à 0 pour vote_jour
            self.a_deja_vote = []
 
            self.passer_phase_nuit("loups")


    def action_sorciere(self, index_victime, choix_sorciere):

        for j in self.liste_joueurs:
            if j.carteatt.nom == "Sorcière" and (j.envie == True or j == self.victime_loups):
                self.sauve_par_sorcière, self.victime_sorcière = j.carteatt.capacite_sorciere(self.liste_joueurs, index_victime, choix_sorciere)
                if choix_sorciere == 1:
                    self.message = "Vous avez choisi de sauver " + self.victime_loups.nom + "."
                elif choix_sorciere == 2:
                    self.message = "La Sorcière a utilisé sa potion de mort."
                else:
                    self.message = "La Sorcière n'a rien fait."

        self.passer_phase_nuit("sorciere")


    def action_chasseur(self, index_cible_chasseur):
        cible = self.liste_joueurs[index_cible_chasseur]
        if cible.envie == True:
            cible.mourir()
            self.message = self.message + "\nLe Chasseur a emporté " + cible.nom + "dans sa tombe !"

        if not self.vérification_victoire():
            self.phase = self.prochaine_phase



    def resoudre_nuit(self):

        morts_cette_nuit = []

        if self.victime_loups != None and self.sauve_par_sorcière == False:
            morts_cette_nuit.append(self.victime_loups)

        if self.victime_sorcière != None:
            morts_cette_nuit.append(self.victime_sorcière)

        self.message = " LE SOLEIL SE LÈVE \nLe village se réveille...\n"

        chasseur_mort = False

        if len(morts_cette_nuit) == 0:
            self.message = self.message + "Personne n'est mort cette nuit !!!"

        else:
            for j in morts_cette_nuit:
                if j.envie == True:
                    j.mourir()
                    self.message = self.message + "Le joueur " + j.nom + " nous a quitté cette nuit, sa carte était : " + j.carteatt.nom + "\n"
                    if j.carteatt.nom == "Chasseur":
                        chasseur_mort = True

        if self.vérification_victoire():
            return

        #chasseur
        if chasseur_mort == True:
            self.phase = "chasseur"
            self.prochaine_phase = "matin"
            self.message += "\nLe Chasseur doit désigner sa cible !"

        else:
            self.phase = "matin"



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
            self.message = self.message + "VICTOIRE ! Tous les Loups-Garous sont morts, les Villageois gagnent !"
            self.phase = "fin"
            return True
        
        elif loups >= villageois:
            self.message = self.message + "DÉFAITE ! Les Loups-Garous sont assez nombreux pour dévorer le reste du village."
            self.phase = "fin"
            return True
        
        else:
            return False



    def vote_de_jour(self, nom_du_votant, index_cible):   #même système que vote_de_nuit

        self.liste_joueurs[index_cible].nb_vote += 1
        self.a_deja_vote.append(nom_du_votant)   #vote enregistré
         
        votants_restants = 0
        for j in self.liste_joueurs:
            if j.envie == True:
                if j.nom not in self.a_deja_vote:
                    votants_restants += 1
        
        if votants_restants == 0:
         
            index_max = 0
            for i in range(len(self.liste_joueurs)):
                if self.liste_joueurs[i].nb_vote > self.liste_joueurs[index_max].nb_vote:
                    index_max = i

            
         
            self.message = "Le joueur " + self.liste_joueurs[index_max].nom + " est mort par vote. Sa carte était : " + self.liste_joueurs[index_max].carteatt.nom
            self.liste_joueurs[index_max].mourir()
         
            for j in self.liste_joueurs:
                j.nb_vote = 0   #compteur à 0 pour vote_jour
            self.a_deja_vote = []
         

            if self.vérification_victoire():
                return
        
            else:
                voyante_presente = False
                for j in self.liste_joueurs:
                    if j.carteatt.nom == "Voyante" and j.envie == True:
                        voyante_presente = True

                if voyante_presente == True:
                    phase_nuit = "voyante"
                    self.message = self.message + "LA NUIT TOMBE... \nLa Voyante se réveille !!"
                else:
                    phase_nuit = "loups"
                    self.a_deja_vote = []
                    for j in self.liste_joueurs:
                        j.nb_vote = 0
                    self.message = self.message + "LA NUIT TOMBE... \nLes Loups-Garous se réveillent !!"

                if self.liste_joueurs[index_max].carteatt.nom == "Chasseur":
                    self.phase = "chasseur"
                    self.prochaine_phase = phase_nuit
                    self.message = self.message + "\nLe Chasseur est mort et doit tirer !"
                else:
                    self.phase = phase_nuit
