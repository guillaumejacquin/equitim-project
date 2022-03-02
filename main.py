from P_D_E.myclass import *
from calculs.dates.DR1 import DR1
from change_text import *
from calculs.dates.PDC1 import *
from calculs.dates.DDR import *
from calculs.dates.DIC import *
from calculs.pdiperf import *
from calculs.periodes.pr import *
from calculs.TDP import *
from calculs.GC import *
from calculs.abac import *
from calculs.ndr import *
from calculs.sjr import *
from calculs.TDS import *
from calculs.dates.DEC import *
from calculs.dates.DCF import *
from calculs.dates.DR1 import *
from calculs.dates.DPR import *
from calculs.dates.EMISSION import *
from calculs.periodes.f0s import *
from calculs.sponsor import *
from calculs.frequencedu import *
from calculs.balise import *
from database.mongo import *
import time

#traitement des données
def start_processus_template(Class):
    PDC1(Class)
    PDC2(Class)
    today_date(Class)
    dec(Class)
    dic(Class)
    pdiperf(Class)
    PR1(Class)
    DPRR(Class)
    TDP(Class)
    GC(Class)
    GCA(Class)
    ndr(Class)
    abac(Class)
    f1_f2(Class)
    SJR(Class)
    tds(Class)
    DCF(Class)
    DR1(Class)
    DPR(Class)
    emission(Class)
    f0s(Class)
    sponsor(Class)
    F0du(Class)
    balise(Class)
    takeinformations(Class)
    # apdr_(Class)

    ChangeTextOnPpt(Class)



def main():
    start = time.time()
    Myvar = InformationsForm()
    start_processus_template(Myvar)
    end = time.time()
    elapsed = end - start
    print("Votre pdf a été réalisé en", round(elapsed, 2), "secondes")


main()