for i in range(2,101):
     trouver=0
     for j in range(2,i):
          if i%j==0:
               trouver=1
     if trouver==0:
          print(f" {i}  " )