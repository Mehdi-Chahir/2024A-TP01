# TODO: Créer un script pour calculer les ressources nécessaires pour assainir la Seine.
# TODO: Importer les modules nécessaires.
''''  
Comme vous le savez, l'eau de la Seine n'est pas la plus propre. Afin de permettre aux épreuves en eau libre de se dérouler dans ce cours d'eau, le comité aurait besoin de votre aide pour calculer les différentes ressources nécessaires pour assainir la Seine.  

Afin d'assainir 5L d'eau, il faut :  

- 1 filtre
- 3 lampes UV
- 0,5kg de chlore

Consignes:  

- Demander la quantité d'eau à assainir
- Afficher les quantités totales de chaque matérieau requis

Exemple:  


![Exemple gif ex2](./assets/ex2.gif)

| Sorties | Entrées |
|:-|:-|
|Quantité d'eau à assainir (en L): | 10 |
| Voici les matériaux requis pour l'assainissement de 10L d'eau:<br>- 2 filtres<br>- 6 lampes UV<br>- 1kg de chlore||
'''



import math

water_quantity = float(input("Entrer la quantité d'eau à assainir en litre") )
x=water_quantity

#print("votre quantité d'eau à assainir est de " x ")
lampesUV=3
chlore=0.5
filtre=1

filtreNecessaire= (x*1)/5
lampeNecessaire= (x*3)/5
chloreNecessaire=(x*0.5)/5

print("Voici les matériaux requis pour l'assainissement de", x,   "L d'eau :" ,filtreNecessaire ,"filtres, ",lampeNecessaire, "lampes UV ""et" ,chloreNecessaire, "kg de chlore" )
#print("la quantité nécessaire de filtre est de " filtreNecessaire)
#print("la quantité nécessaire de filtre est de " lampeNecessaire)
#print("la quantité nécessaire de filtre est de " chloreNecessaire)


