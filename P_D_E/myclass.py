class InformationsForm():
    def __init__(self):
        #LES VARIABLES QU ON VA REMPLIR INITIEES VIA LE FORMULAIRE
        self.template = "testmercredi"
        self.Nom = "Cap dix"
        self.Typologie = "athéna"
        self.Droit = "français"
        self.Isin = "F100140085F1"
        self.Emission = "2022-02-11"
        self.DCI = "11-03-2022"
        self.DR1 = "2023-03-13"
        self.DPR = "2023-03-27"
        self.DADR = "2027-12-27"
        self.DCF = "2028-03-13"
        self.DEC = "2028-03-27"
        self.ADCF = "2027-12-13"

        self.F0 = "trimestre"
        self.TSJ = ["BNP FP Equity", "STLA IM Equity", "", "", ""]


        self.PCS1 = "Euronext Paris"
        self.PCS2 = "Euronext Paris"
        self.PCS3 = ""
        self.PCS4 = ""
        self.PCS5 = ""


        self.CPN = "2.25"
        self.CPN_is_memoire = ""
        self.PDI = "60"
        self.BAC = "100"
        self.BAC_is_degressif = ""
        self.BCPN = "100"
        self.BCPN_is_degressif = ""

        self.PEM = "100"
        self.COM = "1.0"
        self.NSD = "30"
        self.NSM = "70"
        self.NSF = "115"

        self.ABDAC = "100"
        self.DBAC = "60"
        self.DEG = "0"


        self.type_strike = "strike normal"
        self.type_bar = "airbag"

        #self.sous_jacent_nom = ""
        self.sous_jacent = "wo action"
        #self.typeoffre = ""
    


        #on appelle la fonction pour  initier les variables de calcul
        self.var_calculs()
    
    #AUTRES VARIABLES, ICI CALCULS
    def var_calculs(self):
        self.NDR = ""
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
        self.SJR6 = ""
        self.SJR7 = ""

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


        self.balisedeg = ""
        self.balisedeg2 = ""
        self.balisedeg3 = ""
        self.baliseCM = ""
        self.baliseCM22 = ""
        self.baliseCM2 = ""

        self.baliseCM3 = ""
        self.baliseCM4 = ""
        self.SV = ""
        self.PRS = ""
        self.shapes = []
        self.deleteblocs = []
        self.var_degressivite()

    def var_degressivite(self):
        self.desonndr = "de son <NDR>"
        self.longuephrase = "Sinon, si le mécanisme de remboursement anticipé automatique n’a pas été activé au préalable et si, à la date de constatation finale(1), <SJR1> clôture à un <SJR3> strictement inférieur à <DBAC> mais supérieur ou égal à <PDI> de son <NDR>, l’investisseur récupère l’intégralité de son capital initialement investi. "
        self.SDBAC = "strictement inférieur à <DBAC> mais "
        self.PDINSM = "mais supérieur à <PDI> de ce dernier (<NSM> dans cet exemple)"
        self.ETPDI = "et <PDI> "
        self.var_graphs()
        
    def var_graphs(self):
        self.graph1 = ""
        self.graph2 = ""
        self.graph3 = ""
        self.graph4 = ""
        self.graph5 = ""
#si barriere degressive page 2 indice cloture  "DBAC"

#page 3 supprimer de son niveau de référence SI dégressif
#DDR


#page 3 date strike moyen pas verifie