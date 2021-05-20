######################## exo 1 ############################""


"""dans cette exercise vous devez rÃ©cuperer les diffÃ©rents morceaux
de la liste grace aux slices

la de dÃ©part est la suivante

liste = ["Maxime", "Martine", "Christopher", "Carlos", "Michael", "Eric"]
L'objectif de cet exercise est de rÃ©cuperer les informations grace aux slices:

--Les trois premiers employÃ©s ('Maxime', "Martine", "Christopher") dans une liste
trois premiers

--les trois derniers employÃ©s ('Carlos', "Michael" et Eric) dans une liste les trois
derniers.

--tous les employÃ©s sauf le premiers et le derniers dans une liste milieu

--Le premier et le derniers employÃ©dans une liste premier_dernier

"""
liste = ["Maxime", "Martine", "Christopher", "Carlos", "Michael", "Eric"]
trois_premiers =  print(liste[0:3]) # INSÃ‰RER CODE ICI
trois_derniers = print(liste[3:]) # INSÃ‰RER CODE ICI
milieu = print(liste[1:-1])# INSÃ‰RER CODE ICI
premier_dernier = print(liste[0::5]) # INSÃ‰RER CODE ICI
print("############### Fin de l'exercie numéro 1 #################")

################################ exo 2 #######################################

"""
Dans cet exercice, vous devez  ajouter le nombre 6 dans la liste.
Faites une vÃ©rification par la suite pour vous assurer que l'Ã©lÃ©ment a bien Ã©tÃ© ajoutÃ©.

La liste de dÃ©part est la suivante :
liste = [1, 2, 3, 4, 5] Vous devez ajouter le nombre 6 dans la liste.
VÃ©rifiez ensuite si le nombre 6 est prÃ©sent dans la liste, si c'est le cas, 
affichez la chaÃ®ne de caractÃ¨res  Le nombre 6 a bien Ã©tÃ© ajoutÃ© Ã  la liste.
"""
liste2 = [1, 2, 3, 4, 5]
liste2[4] = 6
i=6
if  i== liste2[4]:
    print(f"Le nombre {i} à bien été ajouter à la liste")
else:
    print(f"Erreur de l'ajout du nombre {i}")

############################# Exo 3 ##########################################
   
"""

Récuperer des élements dans une liste imbriquée
Dans cet exercice, vous devez Récuperer des informations Ã  l'intérieur de deux  listes imbriquées.
Le script dispose de deux listes contenant plusieurs listes imbriqués, une liste langage et une liste nombres. 
Vous devez Récuperer dans les variables python, deux et sept, respectivement la chaîne de caractères 'Python'
 contenue dans la liste langages et les nombres 2 et 7, contenus dans la liste nombres.
Vous n'avez pas besoin d'afficher les variables avec print, 
il suffit de Récuperer les bonnes valeurs dans les variables à  partir 
des listes et avec les indices des éléments.

"""
print(" ############################# Exo 3 ########################################## ")
langages = [["Python", "C++"], "Java"]
nombres = [1, [4, [2, 3]], 5, [6], [[7]]]
python =print(langages[0][0]) # entrez le code ici
deux= print(nombres[1][1][0]) # entrez le code ici
sept= print(nombres[4][0][0])# entrez le code ici
