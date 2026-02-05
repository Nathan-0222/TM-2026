class Eleve:
    
    def __init__ (self, nom, classe, note):
        self.nom = nom
        self.classe = age
        self.note = note

    def compare(eleve1, eleve2):
        if eleve1.note > eleve2.note:
            return eleve1.nom
        else:
            return eleve2.nom

riri = Eleve("Henri", "2MS3", 4.5)
firi = Eleve("Jacques", "2MS5", 3.8)
piri = Eleve("Alex", "2MS6", 5)

compare(piri,firi)
