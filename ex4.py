# TODO: Écrire un programme qui demande le pourcentage de charge actuel de la batterie du bateau,
#        calcule la distance restante en km en fonction de ce pourcentage,
#        et affiche le résultat au format "XX km".
#        Assurez une gestion du pourcentage valide au cours de votre programme (% toujours dans [0 ; 100]).

battery_level = int(input("Quelle est le Pourcentage de la batterie : "))

if battery_level >= 50:
    print(f"{battery_level*2}Km")
elif battery_level >= 25 :
    print(f"{battery_level*0.5}Km")
elif battery_level >=10 :
    print(f"{battery_level*1}Km")
elif battery_level >= 5 :
    print(f"{battery_level*2.5}Km")
elif battery_level >= 0:
    print(f"{battery_level*6}Km")

          