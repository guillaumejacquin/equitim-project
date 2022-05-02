from datetime import date
from pandas import array
from pyxirr import xirr
from datetime import datetime, timedelta
from dateutil.relativedelta import *
import pandas as pd


def tra_athena(Class):
    Class.TRA_A_S1 = (xirr_test(Class, Class.PDC2, Class.DEC, Class.NSD))
    Class.TRA_A_S2_100 = (xirr_test(Class, Class.PDC2, Class.DEC, 100))
    Class.TRA_A_S2_GAIN = (xirr_test(Class, Class.PDC2, Class.DEC, float(Class.GCE)+100))
    Class.TRA_M_SJ = (xirr_test(Class, Class.PDC2, Class.DEC, float(Class.NSM)))
    tra_a = float(Class.CPN) * float(Class.PR1) + 100
    Class.TRA_F_A = (xirr_test(Class, Class.PDC2, Class.DR1, tra_a))
    Class.TRA_F_SJ = (xirr_test(Class, Class.PDC2, Class.DR1, Class.NSF))
    tra_mra_min_a =  float(Class.CPN)*float(Class.ADPR)+100
    Class.ADCF = Class.ADCF[0:10]
    Class.TRA_MIN_A = (xirr_test(Class, Class.PDC2, Class.DADR, tra_mra_min_a))
    Class.TRA_echeance_perte_A = (xirr_test(Class, Class.PDC2, Class.DEC, Class.PDI))

def phoenix_3dates(Class, période1, période2):
        Class.TRA_D_P = (xirr_3dates_phoenix(Class, Class.PDC2,str(période1), Class.DEC, Class.CPN, Class.NSD))
        Class.TRA_M_P = (xirr_3dates_phoenix(Class, Class.PDC2,période2, Class.DEC, Class.CPN, 100))
        Class.TRA_M_MP = (xirr_3dates_phoenix(Class, Class.PDC2,période2, Class.DEC, float(Class.CPN)*2, 100))
        Class.TRA_GM_P = (xirr_3dates_phoenix(Class, Class.PDC2,période2, Class.DEC, Class.CPN,  float(Class.CPN) +100))
        
        tragmpm = float(Class.GCE) + 100 - 2 * float(Class.CPN)
        Class.TRA_GM_PM = (xirr_3dates_phoenix(Class, Class.PDC2,période2, Class.DEC, float(Class.CPN) * 2, tragmpm))

        Class.TRA_MIN_P = (xirr_test(Class, Class.PDC2, Class.ADCF, float(Class.CPN) + 100))

        tra_mra_min_pm = float(Class.CPN) * Class.ADPR  + 100
        Class.TRA_MRA_MIN_PM = (xirr_test(Class, Class.PDC2, Class.ADCF, tra_mra_min_pm))


def xirr_test(Class, date1, date2, variable=100):
    first_date = date1 #max entre date émission et strike
    DPR = Class.DPR#first_date_autocall
    second_date = date2 #date_echeance

    flux_var = variable #Scenario Defavorable = flux_var

    # #variable formules
    first_date = datetime.strptime(first_date, '%Y-%m-%d')
    second_date = datetime.strptime(second_date, '%Y-%m-%d')
    soustract2dates = abs(first_date - second_date)
    soustract2dates = soustract2dates.days
    flux_varNet = float(flux_var)*0.99**(float(soustract2dates)/365)
    result = (xirr([first_date,second_date], [-100, float(flux_varNet)]))

    try:
        result = float(result) *100
        result = round(result, 2)
        result = (f'{result:.2f}')

    except Exception:
        pass
    return(result)

def xirr_3dates_phoenix(Class, date1, date2, date3, variable, variable2):
    first_date = date1 #max entre date émission et strike
    second_date = date2 #date_echeance
    third_date = date3

    flux_var = variable #Scenario Defavorable = flux_var
    flux_var2 = variable2
    # #variable formules
    first_date = datetime.strptime(first_date, '%Y-%m-%d')
    second_date = datetime.strptime(second_date, '%Y-%m-%d')
    third_date = datetime.strptime(third_date, '%Y-%m-%d')

    soustract2dates = abs(first_date - second_date)
    soustract2dates = soustract2dates.days
    flux_varNet = float(flux_var)*0.99**(float(soustract2dates)/365)

    soustracttheseconddates = abs(third_date - first_date)
    soustracttheseconddates = soustracttheseconddates.days
    flux_varNet2 = float(flux_var2)*0.99**(float(soustracttheseconddates)/365)
    result = (xirr([first_date,second_date, third_date], [-100, float(flux_varNet), float(flux_varNet2)]))
    
    print("1: ", first_date, second_date, third_date, flux_varNet, flux_varNet2, variable2)
    try:
        result = float(result) *100
        result = round(result, 2)
        result = (f'{result:.2f}')

    except Exception:
        pass
    return(result)

def boucleTRA(Class, date1, date2, date3, variable, variable2):
    first_date = date1 #max entre date émission et strike
    second_date = date2 #date_echeance
    third_date = date3

    flux_var = variable
    first_date = datetime.strptime(first_date, '%Y-%m-%d')
    dates = [second_date, third_date]
    fluxx = []

    def flux(second_date, flux_var):
            second_date = datetime.strptime(second_date, '%Y-%m-%d')
            soustract2dates = abs(first_date - second_date)
            
            soustract2dates = soustract2dates.days

            flux_varNet = float(flux_var)*0.99**(float(soustract2dates)/365)
            return(flux_varNet)

    #la ca doit boucler sa mere
    for i in dates:
        fluxx.append(flux(i, flux_var))
        flux_var = float(flux_var) +1

    print(fluxx)
    print("2: ", first_date, second_date, third_date, fluxx[0], fluxx[1], variable2)

    test = [ -100 , float(fluxx[0]), float(fluxx[1])] 
    result = (xirr([first_date,second_date, third_date], [-100, float(fluxx[0]), float(fluxx[1])]))
    print(result)

    try:
        result = float(result) *100
        result = round(result, 2)
        result = (f'{result:.2f}')

    except Exception:
        pass
    return(result)




def ALL_TRA(Class):
    #athéna
    tra_athena(Class)
    
    #Phoenix
    Class.TRA_D_P = 0

    #Class.TRA_MRE_Min_P = (xirr_test(Class, Class.PDC2, Class.ADCF, tra_mra_min_a))

    if (Class.F0 == "jours"):
        compteur = relativedelta(days=+1) 

    if (Class.F0 == "mois"):
        compteur = relativedelta(months=+1)

    if (Class.F0 == "trimestre"):
        compteur = relativedelta(months=+3)        
    
    if (Class.F0 == "semestre"):
        compteur = relativedelta(months=+6)

    if (Class.F0 == "année"):
        compteur = relativedelta(years=+1)    
    
    compteurvar = Class.DEC
    date_time_obj = datetime.strptime(Class.PDC2, '%Y-%m-%d')
    compteurvar = datetime.strptime(compteurvar, '%Y-%m-%d')
    période = 0

    array_dates = []
    
    while (date_time_obj < compteurvar ):
        array_dates.append(date_time_obj)
        date_time_obj += compteur
        période += 1

    df = pd.DataFrame()
    df["dates"] = array_dates
    try:
        période1 = df["dates"][[1]].to_string(index = False)
        période2 = df["dates"][[2]].to_string(index = False)
        phoenix_3dates(Class)

    except Exception:
        print("rip")
    Class.TRA_D_P = (xirr_3dates_phoenix(Class, Class.PDC2,str(période1), Class.DEC, Class.CPN, Class.NSD))

    print("Result1", Class.TRA_D_P )

    test2 = (boucleTRA(Class, Class.PDC2,str(période1), Class.DEC, Class.CPN, Class.NSD))
    print("---------------")
    print(Class.PDC2)
    print(période1)
    print(Class.DEC)
    print(Class.CPN)
    print(Class.NSD)
    print("Result2", test2)
    print("---------------")
