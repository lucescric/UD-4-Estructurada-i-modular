from datetime import date, datetime, timedelta, time

# 19: dia de la setmana 1/10/1940
d19 = date(1940, 10, 1)
dies_setmana = [
    "dilluns",
    "dimarts",
    "dimecres",
    "dijous",
    "divendres",
    "dissabte",
    "diumenge",
]
print("19. Dia de la setmana 1/10/1940:", dies_setmana[d19.weekday()])
