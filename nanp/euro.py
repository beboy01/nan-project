#un =1.65
#for i in range(16384):
#    dollar =un*i
#print("on a:",i ,"euro = ",dollar , "dollars")
#Un =2
#for i in range(12):
#    Un=Un+1
 #   Un=(Un-1)*3
  #  print("On a U_",i,"=",Un, "et 3U_",i, "==",Un)
def volume(a,b,c):
    return a*b*c
longueur = int(input("Veullez renseignez la longeur du parapépipède : "))
largeur = int(input("Veullez renseignez la largeur du parapépipède : "))
hauteur = int(input("Veullez renseignez la hauteur du parapépipède  : "))
vol= volume(longueur,largeur,hauteur)
if(longueur>largeur and longueur>hauteur):
    print(f" la le parapépipède de longeur ,{longueur} , de largeur ,{largeur} et de hauteur ,{hauteur} à pour volume :,{vol}")
else:
    print("vous n'avez pas un paralélogramme car son largeur ou sa hauteur es superieur a la longueur")
    
