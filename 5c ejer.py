from datetime import datetime, timedelta


def dies_viscuts(data_naixement):
    naix = datetime.strptime(data_naixement, "%Y-%m-%d").date()
    avui = datetime.now().date()
    return (avui - naix).days


def dia_8000(data_naixement):
    naix = datetime.strptime(data_naixement, "%Y-%m-%d").date()
    return naix + timedelta(days=8000)


def programa():
    print("=== CÀLCUL DE DIES VISCUTS I DIA DELS 8000 DIES ===")
    data = input("Introdueix la teua data de naixement (YYYY-MM-DD): ")

    try:
        viscuts = dies_viscuts(data)
        data8000 = dia_8000(data)

        print(f"\nHas viscut {viscuts} dies.")
        print(f"Compliràs 8000 dies el dia: {data8000}")

    except ValueError:
        print("Format de data incorrecte. Usa YYYY-MM-DD.")


# Executar el programa
programa()
