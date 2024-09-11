# TODO: Créer un script permettant le formattage du livre des records des JO.

''''  Demander la nationalité de l'athlète
- Demander le nom de l'athlète
- Demander la date du record
- Demander la discipline
- Demander la catégorie, qui peut être nulle
- Demander le record
'''


country = input("De quelle nationalité est l'athlète ? ")
athlete = input("Quelle est le nom de l'athelète ?")
date = input("Quelle est la date du record ?")
discipline= input("Quelle est la discipline ?")
Categorie = input("Quelle est la catégorie ?")
Record = input("Quelle est le record ?")

print("Nouveau Rocord:")
print("----------------------")
print(date)
print(f"{discipline} - {Categorie}")
print(f"{athlete} {country} - {Record}")