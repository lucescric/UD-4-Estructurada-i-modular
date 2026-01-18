from datetime import datetime, timedelta


def dia_8000(data_naixement):
    """
    Rep una data de naixement en format YYYY-MM-DD
    i retorna la data en què la persona complirà 8000 dies.
    """
    naix = datetime.strptime(data_naixement, "%Y-%m-%d").date()
    data_8000 = naix + timedelta(days=8000)
    return data_8000
