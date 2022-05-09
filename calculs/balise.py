def balise(Class):
    strike = Class.type_strike
    ndr = Class.NDR
    sjr1 = Class.SJR1
    sjr3 = Class.SJR3
    ddi = Class.DDCI_affichage
    ddi2 = Class.DPCI
    

    if (Class.TDP == "action"):
        du = "de l'"
    else:
        du = "du"


    if (strike == "strike normal"):
        mystring = "Le "+ Class.NDR + " correspond au " + sjr3 + " de clôture de " + sjr1 + "" + Class.NOMSOUSJACENT +  " le " + ddi

    print("Class.SJR3333333 = ", Class.SJR3)
    if (strike == "strike moyen"):
        mystring = "Le "+ Class.NDR + " correspond à la moyenne arithmétique des " + sjr3 + " de clôture de " + sjr1 + " " + Class.NOMSOUSJACENT + " du " + ddi + " au " + ddi2

    if (strike == "best strike"):
        mystring = "Le "+ Class.NDR + " correspond au " + sjr3 + " " + Class.NOMSOUSJACENT + " le plus bas observé aux dates suivantes : \n" + Class.DCI + "."

    Class.balise = mystring


#DCF MAJUSCULE