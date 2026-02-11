from datetime import date, datetime, timedelta, time

# 18: nom en valencià del mes actual
mesos_val = {
    1: "gener",
    2: "febrer",
    3: "març",
    4: "abril",
    5: "maig",
    6: "juny",
    7: "juliol",
    8: "agost",
    9: "setembre",
    10: "octubre",
    11: "novembre",
    12: "desembre",
}
hui = date.today()

print("18. Mes actual en valencià:", mesos_val[hui.month])
