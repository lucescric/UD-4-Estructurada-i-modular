from datetime import datetime, timedelta


def data_actual():
    avui = datetime.now().date()
    print("La data actual és:", avui)


def hora_actual():
    hora = datetime.now().time().strftime("%H:%M:%S")
    print("L'hora actual és:", hora)


def sumar_dies():
    try:
        dies = int(input("Introdueix el nombre de dies a sumar: "))
        nova_data = datetime.now().date() + timedelta(days=dies)
        print("La nova data és:", nova_data)
    except ValueError:
        print("Has d'introduir un número enter.")


def diferencia_dies():
    try:
        d1 = input("Introdueix la primera data (format YYYY-MM-DD): ")
        d2 = input("Introdueix la segona data (format YYYY-MM-DD): ")

        data1 = datetime.strptime(d1, "%Y-%m-%d").date()
        data2 = datetime.strptime(d2, "%Y-%m-%d").date()

        diferencia = abs((data2 - data1).days)

        print(f"{'Data 1':<12}{'Data 2':<12}{'Diferència (dies)':<20}")
        print(f"{data1:<12}{data2:<12}{diferencia:<20}")

    except ValueError:
        print("Format de data incorrecte.")


def anterior_posterior():
    try:
        d = input("Introdueix una data (format YYYY-MM-DD): ")
        data_usuari = datetime.strptime(d, "%Y-%m-%d").date()
        avui = datetime.now().date()

        if data_usuari < avui:
            print("La data introduïda és ANTERIOR a la data actual.")
        elif data_usuari > avui:
            print("La data introduïda és POSTERIOR a la data actual.")
        else:
            print("La data introduïda és EXACTAMENT la data actual.")

    except ValueError:
        print("Format de data incorrecte.")


def menu():
    while True:
        print("\n--- MENÚ D'OPERACIONS AMB DATES ---")
        print("1. Obtindre la data actual")
        print("2. Obtindre l’hora actual")
        print("3. Sumar dies")
        print("4. Diferència en dies")
        print("5. Anterior o Posterior")
        print("9. Eixir")

        opcio = input("Selecciona una opció: ")

        if opcio == "1":
            data_actual()
        elif opcio == "2":
            hora_actual()
        elif opcio == "3":
            sumar_dies()
        elif opcio == "4":
            diferencia_dies()
        elif opcio == "5":
            anterior_posterior()
        elif opcio == "9":
            print("Gràcies per utilitzar el programa. Adéu!")
            break
        else:
            print("Opció no vàlida. Torna-ho a intentar.")


# Executar el menú
menu()
