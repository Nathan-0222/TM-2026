from carte import *
from joueur import *
from partie import *


partie = Partie("ciao")
partie.run(self)

c1 = Sorciere()

# j1 = Joueur("Nathan", c1) # ici il faudrait passer que le nom, la carte dans un deuxième temps

partie.ajouter_joueur()
print(partie.liste_joueurs)

elimine = partie.liste_joueurs.pop(1)
print(f"{elimine.nom} est éliminé !")
print(partie.liste_joueurs)