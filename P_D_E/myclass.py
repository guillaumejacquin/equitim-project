class InformationsForm():
    def __init__(self):
        #LES VARIABLES QU ON VA REMPLIR INITIEES VIA LE FORMULAIRE
        self.template = "test15"
        self.Nom = "LOKT BNP JUIN 2022"
        self.Typologie = "athéna"
        self.Droit = "français"
        self.Isin = "TBD"
        self.Emission = "2022-03-25"
        self.DCI = "04-03-2022, 03-06-2022"
        self.DR1 = "2023-06-05"
        self.DPR = "2023-06-19"
        self.DADR = "2027-05-17"
        self.DCF = "2027-06-03"
        self.DEC = "2027-06-17"
        self.ADCF = "2027-05-03"

        self.F0 = "mois"
        self.TSJ = ["BNP FP Equity", "", "", "", ""]


        self.PCS1 = "Euronext Paris"
        self.PCS2 = ""
        self.PCS3 = ""
        self.PCS4 = ""
        self.PCS5 = ""


        self.CPN = "0.70"
        self.CPN_is_memoire = ""
        self.PDI = "60"
        self.BAC = "95"
        self.BAC_is_degressif = ""
        self.BCPN = "95"
        self.BCPN_is_degressif = "oui"

        self.PEM = "100"
        self.COM = "1.0"
        self.NSD = "30"
        self.NSM = "70"
        self.NSF = "120"

        self.ABDAC = "95"
        self.DBAC = "95"
        self.DEG = "0"


        self.type_strike = "strike moyen"
        self.sous_jacent_nom = ""
        self.sous_jacent = "mono action"
        self.typeoffre = ""
        self.NDR = ""
    


        #on appelle la fonction pour  initier les variables de calcul
        self.var_calculs()
    
    #AUTRES VARIABLES, ICI CALCULS
    def var_calculs(self):
        self.DDCI = ""
        self.DPCI = ""
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
        self.ADCF_affichage = ""
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
        self.EBAC = "et <BAC>"

        test = ""

        self.var_degressivite()

    def var_degressivite(self):
        self.desonndr = "de son <NDR>"
        self.longuephrase = "Sinon, si le mécanisme de remboursement anticipé automatique n’a pas été activé au préalable et si, à la date de constatation finale(1), <SJR1> clôture à un <SJR3> strictement inférieur à <DBAC> mais supérieur ou égal à <PDI> de son <NDR>, l’investisseur récupère l’intégralité de son capital initialement investi. "
        self.SDBAC = "strictement inférieur à <DBAC> mais "
        self.PDINSM = "mais supérieur à <PDI> de ce dernier (<NSM> dans cet exemple)"
        self.ETPDI = "et <PDI> "
        
#si barriere degressive page 2 indice cloture  "DBAC"

#page 3 supprimer de son niveau de référence SI dégressif
#DDR


#page 3 date strike moyen pas verifie