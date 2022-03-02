from datetime import date

def today_date(Class):
    today = date.today()

    d4 = today.strftime("%d/%m/%y")
    Class.DDR = d4