
mois = int(input("tapez le nombre d'un mois :"))
annee = int(input("tapez l'annee :"))
if mois ==  1 or mois == 3 or mois == 5 or mois == 7 or mois == 8 or mois == 10 or mois == 12:
       print("LE NOMBRE DU JOURS DE CE MOIS DANS CETTE ANNEE EST 31")
elif  mois == 4 or mois == 6 or mois ==  9 or mois ==11  :
       print("LE NOMBRE DU JOURS DE CE MOIS DANS CETTE ANNEE EST 30") 
elif  annee % 4 == 0 and  annee%100 != 0 or annee%400==0  :
       print("LE NOMBRE DU JOURS DE CE MOIS DANS CETTE ANNEE 29")  
else:
        print("LE NOMBRE DU JOURS DE CE MOIS DANS CETTE ANNEE 28")