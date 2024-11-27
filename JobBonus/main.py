chaine = input("Rentrez une chaine de cractere : ")
i = 0

for lettre in chaine:
    i += 1
    if lettre == "e":
        print("La chaine contient un e")
        break
    elif i == len(chaine):
        print("La chaine ne contient pas de e")



