def annee(year):
    year = int(year)
    if (year%4==0 and year %100==0):
        if(year%400==0):
            print(f" {year} est une année bissestille  ")
        else:
            print("c'est pass une année bissestille")
    elif not(year%4==0 and year %100==0 and year%400==0):
        print("c'est pass une année bissestilles")
    day = input("Etrez une année pour voir si elle est  bissestille ou pas :")
    annee(day)   
