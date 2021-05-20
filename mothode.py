"""
Dans cet exercice, vous devez :

Afficher la phrase mdp_trop_court en majuscule si le mot de passe entré est égal à  0.

Afficher la phrase mdp_trop_court avec une majuscule sur la première lettre si le mot de passe entré est plus petit que 8.

Afficher la phrase "Votre mot de passe ne contient que des nombres." si le mot de passe entré ne contient que des nombres.

Afficher la phrase "Inscription terminée." si le mot de passe est valide.

Script de départ :
"""
"""
mdp = input("Entrez un mot de passe (min 8 caractÃ¨res) : ")
mdp_trop_court = "votre mot de passe est trop court."

Questions pour cet exercice
Comment utiliser les structures conditionnelles et 
des mÃ©thodes de chaÃ®nes de caractÃ¨res pour vÃ©rifier 
la validitÃ© du mot de passe ?

# afficher votre reponse

# ici
"""



import re
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
     elif mdp.isdigit():
          affiche="le mot de passe contient que des nombres"
          print(affiche)
     elif len(mdp) >= 8:
          affiche= "Inscription terminée "
          print(affiche)
mdp = input("donne moit un mode passe : ")
mot_de_passe(mdp)