
def mot_de_passe(mdp):
     
     affiche=" "
     max= 8
     if len(mdp)==0:
          affiche= "mot de passe trop cour "
          affiche = affiche.upper()
          print(affiche)
     elif len(mdp) >0 and len(mdp)<= max:
          affiche="mot de passe inferieur à 8"
          affiche= affiche.capitalize()
          print(affiche)
     elif max <= len(mdp):
          affiche= "mot de pas "
          print(affiche)
mdp = input("donne moit un mode passe : ")
mot_de_passe(mdp)
