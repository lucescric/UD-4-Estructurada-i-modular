import random

opcions = ["pedra", "paper", "tisores", "llangardaix", "spock"]

# Regles del joc: cada opció guanya contra dues i perd contra dues
guanya = {
    "tisores": ["paper", "llangardaix"],
    "paper": ["pedra", "spock"],
    "pedra": ["llangardaix", "tisores"],
    "llangardaix": ["spock", "paper"],
    "spock": ["tisores", "pedra"],
}

# La CPU tria una opció a l'atzar
cpu = random.choice(opcions)

# L'usuari tria una opció
usuari = input("Tria Pedra, Paper, Tisores, Llangardaix o Spock: ").strip().lower()

if usuari not in opcions:
    print("La paraula introduïda no ha sigut reconeguda.")
else:
    print(f"La CPU ha triat: {cpu.capitalize()}")
    print(f"Tu has triat: {usuari.capitalize()}")

    if usuari == cpu:
        print("Empat!")
    elif cpu in guanya[usuari]:
        print("Has guanyat!")
    else:
        print("Has perdut!")
