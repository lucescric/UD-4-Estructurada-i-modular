import random

opcions = ["pedra", "paper", "tisores"]

# a) La CPU tria una opció a l'atzar
cpu = random.choice(opcions)

# b) L'usuari tria una opció
usuari = input("Tria Pedra, Paper o Tisores: ").strip().lower()

if usuari not in opcions:
    print("La paraula introduïda no ha sigut reconeguda.")
else:
    print(f"La CPU ha triat: {cpu.capitalize()}")
    print(f"Tu has triat: {usuari.capitalize()}")

    # c) Determinar el resultat
    if usuari == cpu:
        print("Empat!")
    elif (
        (usuari == "pedra" and cpu == "tisores")
        or (usuari == "paper" and cpu == "pedra")
        or (usuari == "tisores" and cpu == "paper")
    ):
        print("Has guanyat!")
    else:
        print("Has perdut!")
