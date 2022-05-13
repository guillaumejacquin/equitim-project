import pandas as pd
import datetime
from dateutil.relativedelta import relativedelta
import sys


def get_all_dates_between_2_dates_with_special_begin(Class, date_départ, date_de_fin, date_debut_analyse, exclus=False):
    date_depart = date_départ
    date_fin = date_de_fin
    
    result_dates = []
    inFile = "database/Calendar_US_Target.xlsx"
    inSheetName = "Sheet1"
    df =(pd.read_excel(inFile, sheet_name = inSheetName))

    date_depart = datetime.datetime.strptime(date_depart, '%Y-%m-%d')
    date_fin = datetime.datetime.strptime(date_fin, '%Y-%m-%d')
    date_calcul_depart = datetime.datetime.strptime(date_debut_analyse, '%Y-%m-%d')

    var_date_depart = date_depart

    time_to_add = ""

    if (Class.F0 == "mois"):
        time_to_add = relativedelta(months=1)    
        
    if (Class.F0 == "trimestre"):
        time_to_add = relativedelta(months=3)    

    if (Class.F0 == "semestre"):
        time_to_add = relativedelta(months=6)    

    if (Class.F0 == "année"):
        time_to_add = relativedelta(years=1)    


    while var_date_depart <= date_fin:
        mask = (df['TARGETirs_holi'] >= var_date_depart) # JOUR SUIVANT
        result = df[mask]['TARGETirs_holi'].iloc[0]



        if (result >= date_calcul_depart):
            result = (str(result)[0:10])
            result = result[8:10] + "/" + result[5:7] + "/" + result[0:4]
            result_dates.append(str(result))

        
        var_date_depart = var_date_depart + time_to_add
    
    if (exclus == True):
        result_dates = result_dates[1:-1]
    return(result_dates)


def get_all_dates_between_2_dates_with_special_begin_substraction(Class, date_départ, date_de_fin, date_debut_analyse, exclus=False):
    date_depart = date_départ
    date_fin = date_de_fin
    
    result_dates = []
    inFile = "database/Calendar_US_Target.xlsx"
    inSheetName = "Sheet1"
    df =(pd.read_excel(inFile, sheet_name = inSheetName))

    date_depart = datetime.datetime.strptime(date_depart, '%Y-%m-%d')
    date_fin = datetime.datetime.strptime(date_fin, '%Y-%m-%d')
    date_calcul_depart = datetime.datetime.strptime(date_debut_analyse, '%Y-%m-%d')

    var_date_depart = date_depart

    time_to_add = ""

    if (Class.F0 == "mois"):
        time_to_add = relativedelta(months=1)    
        
    if (Class.F0 == "trimestre"):
        time_to_add = relativedelta(months=3)    

    if (Class.F0 == "semestre"):
        time_to_add = relativedelta(months=6)    

    if (Class.F0 == "année"):
        time_to_add = relativedelta(years=1)    


    while var_date_depart <= date_fin:
        df['mask'] = (var_date_depart <= df['TARGETirs_holi']) # JOUR SUIVANT
        print(df.head())
        print(df[df.mask =="True"].head(1))

        if (result >= date_calcul_depart):
            result = (str(result)[0:10])
            result = result[8:10] + "/" + result[5:7] + "/" + result[0:4]
            result_dates.append(str(result))

        
        var_date_depart = var_date_depart + time_to_add
    
    if (exclus == True):
        result_dates = result_dates[1:-1]
    return(result_dates)
