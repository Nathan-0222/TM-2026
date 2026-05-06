from carte import *
from joueur import *
from partie import *


ma_partie = Partie("ciao")
ma_partie.run()

c1 = Sorciere()

# j1 = Joueur("Nathan", c1) # ici il faudrait passer que le nom, la carte dans un deuxième temps

l1 = LoupGarou()
print(l1.nom)