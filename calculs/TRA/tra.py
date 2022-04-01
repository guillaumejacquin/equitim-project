from datetime import date
from pyxirr import xirr
from datetime import datetime

# test = (xirr(['2020-01-01', '2021-01-01', '2022-01-01','2023-01-01'], [-100, 10, 10,110]))
# test = test *100
# test = round(test, 2)
# test = (f'{test:.2f}')

# print(test)

def xirr_test(Class, date1, date2, variable=100):
    first_date = date1 #max entre date émission et strike
    DPR = Class.DPR#first_date_autocall
    last_date_autocall = '2032-02-12' #last_date_autocall
    second_date = date2 #date_echeance


    flux_var = variable #Scenario Defavorable = flux_var
    GCE = 60 # total des gains à l'échéance 
    PR1 = 4 # Première période de rappel
    CPN = 1.50 #Coupon périodique
    PDI = 50 # Barrière de protection de capital

    # #variable formules
    first_date = datetime.strptime(first_date, '%Y-%m-%d')
    second_date = datetime.strptime(second_date, '%Y-%m-%d')
    soustract2dates = abs(first_date - second_date)
    soustract2dates = soustract2dates.days
    flux_varNet = float(flux_var)*0.99**(float(soustract2dates)/365)

    result = (xirr([first_date,second_date], [-100, float(flux_varNet) ]))
    result = float(result) *100
    result = round(result, 2)
    result = (f'{result:.2f}')
    return(result)




#TRA.A = athéna  == coupon ataucall
#Tra.p = phoenix = coupon phoenix
#sinon les 2