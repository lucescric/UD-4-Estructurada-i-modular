import random

# El programa elige un número al azar entre 1 y 100
secret = random.randint(1, 100)
intents = 0

print("He pensat un número entre 1 i 100. A veure si l'endevines!")

while True:
    intents += 1
    try:
        num = int(input("Introdueix un número: "))
    except ValueError:
        print("Si us plau, introdueix un número vàlid.")
        continue

    if num < secret:
        print("El meu número és major.")
    elif num > secret:
        print("El meu número és menor.")
    else:
        print(f"Correcte! Has encertat el número {secret}.")
        print(f"Has necessitat {intents} intents.")
        break
