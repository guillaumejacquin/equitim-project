from datetime import date

def today_date(Class):
    today = date.today()
    d4 = today.strftime("%d/%m/%Y")
    Class.DDR = d4