produit = {
    "produit0":
    {"nom": "Aspirateur",
    "prix unitaire (euro)": 80,
    "quantité en stock": 11}}

poduitAcheter = input("Combien de produit " + produit["produit0"]["nom"] + " voulez-vous acheter ? : ")

produit["produit0"]["quantité en stock"] -= int(poduitAcheter)


print(produit["produit0"]["nom"])
print(produit["produit0"]["prix unitaire (euro)"])
print(produit["produit0"]["quantité en stock"])

print("\nOops, ptite inflation de 10%...\n")
produit["produit0"]["prix unitaire (euro)"] *= 1.1

print(produit["produit0"]["nom"])
print(produit["produit0"]["prix unitaire (euro)"])
print(produit["produit0"]["quantité en stock"])