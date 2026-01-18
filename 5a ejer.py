from datetime import datetime


def dies_viscuts(data_naixement):
    """
    Rep una data de naixement en format YYYY-MM-DD
    i retorna quants dies ha viscut la persona.
    """
    naix = datetime.strptime(data_naixement, "%Y-%m-%d").date()
    avui = datetime.now().date()
    return (avui - naix).days
