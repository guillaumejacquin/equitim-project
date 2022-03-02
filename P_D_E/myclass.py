class InformationsForm():
    def __init__(self):
        #LES VARIABLES QU ON VA REMPLIR INITIEES VIA LE FORMULAIRE
        self.template = "test"
        self.Nom = "Uluwatu test mercredi"
        self.Typologie = "athéna"
        self.Droit = "anglais"
        self.Isin = "XS2061794066"
        self.Emission = "2022-03-17"
        self.DCI = "09-06-2022"
        self.DR1 = "2023-06-09"
        self.DPR = "2022-06-16"
        self.DADR = "2034-03-16"
        self.DCF = "2034-06-09"
        self.DEC = "2034-06-16"

        self.F0 = "trimestre"
        self.TSJ = ["SPEZBDET Index", "", "", "", ""]


        self.PCS1 = ""
        self.PCS2 = ""
        self.PCS3 = ""
        self.PCS4 = ""
        self.PCS5 = ""


        self.CPN = "2.75"
        self.CPN_is_memoire = "oui"
        self.PDI = "50"
        self.BAC = "50"
        self.BAC_is_degressif = "oui"
        self.BCPN = "50"
        self.BCPN_is_degressif = "oui"

        self.PEM = "100"
        self.COM = "1.0"
        self.NSD = "30"
        self.NSM = "50"
        self.NSF = "120"

        self.ABDAC = "50.55"
        self.DBAC = "50"
        self.DEG = "1.15"


        self.type_strike = "strike moyen"
        self.sous_jacent_nom = ""
        self.sous_jacent = "mono indice"
        self.typeoffre = ""
        self.NDR = ""


        #on appelle la fonction pour  initier les variables de calcul
        self.var_calculs()
    
    #AUTRES VARIABLES, ICI CALCULS
    def var_calculs(self):
        self.DDCI = ""
        self.PDC1 = ""
        self.PDC2 = ""
        self.DDR = ""
        self.DIC = ""
        self.PDIPERF = ""
        self.DTRAT = ""
        self.PR1 = ""
        self.DPRR = ""
        self.TDP = ""
        self.GC = ""
        self.GCA = ""
        self.GCE = ""
        self.ABAC = ""
        self.ADPR = ""
        self.F1 = ""
        self.F2 = ""

        self.SJR1 = ""
        self.SJR2 = ""
        self.SJR3 = ""
        self.SJR4 = ""
        self.SJR5 = ""

        self.TDS = ""
        

        self.PDC1_affichage = ""
        self.PDC2_affichage = ""
        self.DDCI = ""
        self.DEC_affichage = ""
        self.DFC_affichage = ""
        self.Emission_affichage = ""
        self.F0s = "s"

        self.sponsor = "sponsor"
        self.balise = ""
        self.DU = "du"
        self.NOMSOUSJACENT = ""
        self.DIVIDENDE = ""
        self.TICKER = ""
        self.Site = ""
        self.inconvenient = ""



#si barriere degressive page 2 indice cloture  "DBAC"

#page 3 supprimer de son niveau de référence SI dégressif





#METTRE une , au lieu de .