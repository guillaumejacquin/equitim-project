def balise(Class):
    strike = Class.type_strike
    ndr = Class.NDR
    sjr1 = Class.SJR1
    sjr3 = Class.SJR3
    ddi = Class.DCI

    if (Class.TDP == "action"):
        du = "de l'"
    else:
        du = "du"


    if (strike == "strike normal"):
        mystring = "le "+ Class.NDR + " correspond au " + sjr3 + " de clôture de " + sjr1 + " le " + ddi

    if (strike == "strike moyen"):
        mystring = "le "+ Class.NDR + " correspond à la moyenne arithmétique des " + sjr3 + " de clôture de " + sjr1 + " aux dates suivantes: " + ddi


    if (strike == "best strike"):
        mystring = "le "+ Class.NDR + " correspond au " + sjr3 + " le plus bas observé aux dates suivantes: " + ddi

    Class.balise = mystring
