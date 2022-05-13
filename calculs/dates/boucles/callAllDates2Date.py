from pickle import TRUE
import pandas as pd
import datetime
from dateutil.relativedelta import relativedelta
import sys
from calculs.dates.boucles.getAllDates2Dates import *

def callAllDates2Date(Class):
    #print("jour suivant, exclus", get_all_dates_between_2_dates_with_special_begin(Class, Class.DDCI, Class.DCF, Class.DR1, True, True))
    #print("jour d'avant, exclus", get_all_dates_between_2_dates_with_special_begin_substraction(Class, Class.DDCI, Class.DCF, Class.DR1, exclus=True))
    Class.Datesconstatations1 = get_all_dates_between_2_dates_with_special_begin(Class, Class.DDCI, Class.DCF, Class.DR1, True)
    Class.Datesconstatations2 = get_all_dates_between_2_dates_with_special_begin(Class, Class.DDCI, Class.DCF, Class.DR1, True)

    Class.Datesconstatations3 = get_all_dates_between_2_dates_with_special_begin(Class, Class.DDCI, Class.DCF, Class.DDCI, True)
    Class.Datesconstatations4 = get_all_dates_between_2_dates_with_special_begin(Class, Class.DDCI, Class.DCF, Class.DDCI, True)
