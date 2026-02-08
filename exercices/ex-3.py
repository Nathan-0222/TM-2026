class Chrono:
    def __init__ (self, heures, minutes, secondes):
        self.heures = heures
        self.minutes = minutes
        self.secondes = secondes
    def affiche(self):
        return "Il est" + str(self.heures) + "heures" + str(self.minutes) + "minutes et" + str(self.secondes) + "secondes"
    def avance(self, secondes):
        self.secondes = self.secondes + secondes
        self.minutes = self.minutes + secondes//60
        self.secondes = self.secondes % 60
        self.heures = self.heures + self.minutes//60
        self.minutes = self.minutes % 60
