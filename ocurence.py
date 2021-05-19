from math import sqrt
def occurence(car,ch):
    """
    cette fonction renvoie le nombre de caractère car contenue dans la chaine ch
    """
    nc=0
    i=0
    while i <len(ch):
        if ch[i]==car:
            nc=nc +1
        i=i+1
    return nc
############################################
#corqs principale de la function
print("Veuillez entrer un nombre :")
nbr=eval(input())
print("Veuillez entrer une phrase :")
phr=input()
print("Veuillez entrer un caractère à compter :")
cch=input()
no=occurence(cch,phr)
rc=sqrt(nbr**3)

print("La racine carre du cube ",end=" ")
print("du nombre fourni vaut ",end=' ')
print(rc)
print("la phrase contient ",end=' ')
print(no,"caractère", cch)

