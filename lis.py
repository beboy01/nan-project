
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
langages = [["Python", "C++"], "Java"]
nombres = [1, [4, [2, 3]], 5, [6], [[7]]]

python =print(langages[0][0]) # entrez le code ici
deux= print(nombres[1][1][0]) # entrez le code ici
sept= print(nombres[4][0][0])# entrez le code ici

# creer deux programme avec la boucle for et la boucle while
# qui affiche les 100 premiers nombres entiers premiers.
liste=[]
resul=0
for num in range(0, 101):
    
    for i in range(2, num):
        resul=num %i
        if resul!=0:
            liste[i] = liste.append(resul)
            print(liste)
    
