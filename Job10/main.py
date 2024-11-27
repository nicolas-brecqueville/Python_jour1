investissementInitial = 5000
tauxRendementAnnuel = 4

print(investissementInitial * (tauxRendementAnnuel/100))

print("Augmentation de l'investissement de 5000€, +2 points de pourcentage.")
investissementInitial += 5000
tauxRendementAnnuel += 2 # Augmentation du taux de 2 point de pourcentage

print(investissementInitial * (tauxRendementAnnuel/100))

print("Diminution de l'investissement de 10%, -1 point de pourcentage.")
investissementInitial *= 0.9
tauxRendementAnnuel -= 1 # Augmentation du taux de 2 point de pourcentage

print(investissementInitial * (tauxRendementAnnuel/100))