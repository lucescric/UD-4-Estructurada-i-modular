from datetime import date, datetime, timedelta, time


# 17: dia de la setmana fa tres dies
hui = date.today()
fa_tres_dies = hui - timedelta(days=3)
dies_setmana = [
    "dilluns",
    "dimarts",
    "dimecres",
    "dijous",
    "divendres",
    "dissabte",
    "diumenge",
]
print(
    "17. Fa tres dies era:",
    fa_tres_dies.strftime("%d/%m/%Y"),
    "-",
    dies_setmana[fa_tres_dies.weekday()],
)
