from math import*
a = input("Donnez moi votre note :")
note =float(a)
if note <3:
    print('Sans commentaire ...')
elif note>=3 and note < 6:
    print("tu n'as rien compris!")
elif note>=7 and note <10:
    print("il faut tous revoir !")
elif note>=11 and note <14:
    print("Peut mieux fait!") 
elif note>=15 and note <18:
    print("Bon travaille !") 
elif note>=18 and note <20:
    print("Excellent !!") 
elif note==20 :
    print("C'est sans faute !")
