def balisedeg(Class):
    if (Class.type_bar == "degressif" or Class.type_bar == "airbag"):
        Class.balisedeg = ", ou si à la date de constatation finale(¹), <SJR1> clôture à un <SJR3> supérieur ou égal à <DBAC> de son <NDR>"
        Class.balisedeg2 = "La barrière de remboursement anticipé automatique est dégressive au fil du temps. Elle est fixée à <BAC> du <NDR>  en fin de <F0> <1PR>, puis décroît de <DEG>% chaque <F0>, pour atteindre <ABDAC>% du <NDR> à la fin du <F0> <ADPR>."
        Class.balisedeg3 = "<balisedeg2>"

    else:
        Class.balisedeg = ""
        Class.balisedeg2 = ""
        Class.balisedeg3 = "<BAC> DU <NDR> de <SJR1>"



    if ((Class.type_bar == "degressif" or Class.type_bar == "airbag") and Class.DBAC == Class.PDI):
        Class.baliseCM = ""
        Class.deleteblocs.append("Cas médian :")
        Class.deleteblocs.append("(Soit un Taux de Rendement Annuel net de")



    #INCOMPHRENSION#
    if (Class.type_bar == "degressif" or Class.type_bar == "airbag") and Class.DBAC == Class.PDI:
        Class.baliseCM2 = "Le capital n’est donc exposé à un risque de perte à l’échéance(¹) que si <SJR1> clôture à un <SJR3> strictement inférieur à <PDI> de son <NDR> à la date de constatation finale(1)."
        # Class.deleteblocs.append("Cas médian :")
    else:
        Class.baliseCM22 = ("Sinon, si le mécanisme automatique de remboursement anticipé n’a pas été activé au préalable et si, à la date de constatation finale(1), <SJR1> clôture à un <SJR3> strictement inférieur à <DBAC> de son <NDR> mais supérieur ou égal à <PDI> de ce dernier, l’investisseur récupère l’intégralité de son capital initialement investi. Le capital n’est donc exposé à un risque de perte à l’échéance(1) que si <SJR1> clôture à un <SJR3> strictement inférieur à <PDI> de son <NDR> à la date de constatation finale(1).")


    #!INCOMPREHENSION!#

    if (Class.type_bar == "degressif" or Class.type_bar == "airbag") and Class.DBAC == Class.PDI:
        Class.baliseCM3 = "À la date de constatation finale(¹), <SJR1> clôture à un <SJR3> strictement supérieur à <DBAC> de son <NDR>"
    else:
        Class.baliseCM3 = "À la date de constatation finale(¹), <SJR1> clôture à un <SJR3> strictement inférieur à <DBAC> mais supérieur ou égal à <PDI> de son <NDR>"


    if (Class.type_bar == "degressif" or Class.type_bar == "airbag") and Class.DBAC == Class.PDI:
        Class.baliseCM4 = """À la date de constatation finale(¹), <SJR1> clôture à un <SJR3> strictement supérieur à <DBAC> de son <NDR> (<NSM> dans cet exemple). L’investisseur récupère alors l’intégralité de son capital initialement investi majorée d’un <GC> de <CPN> par <F0> écoulé depuis le <DDCI> (soit un gain total de <GCE> total )."""

    else: 
        Class.baliseCM4 = """À la date de constatation finale(¹), <SJR1> clôture à un <SJR3> strictement inférieur à <DBAC> de son <NDR> (<NSM> dans cet exemple). L’investisseur récupère alors l’intégralité de son capital initialement investi.
        """
