from datetime import date, datetime, timedelta, time

# 16: dia de la setmana 22/4/2022
d16 = date(2022, 4, 22)
dies_setmana = [
    "dilluns",
    "dimarts",
    "dimecres",
    "dijous",
    "divendres",
    "dissabte",
    "diumenge",
]
print("16. Dia de la setmana 22/4/2022:", dies_setmana[d16.weekday()])
