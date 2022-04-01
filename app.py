
from flask import Flask
from flask import render_template, url_for, request
import sys
from main import *
from flask_cors import CORS


sys.path.append("../")
from app import *
app = Flask(__name__)
CORS(app)




@app.route("/add", methods=["POST"])
def add_articles():
    Myclass = InformationsForm()

    data = request.json
    print(data)
    Myclass.template = data["template"]
    Myclass.Nom = data["Nom"]
    Myclass.Typologie = data["Typologie"]
    Myclass.Droit = data["Droit"]
    Myclass.Isin = data["Isin"]
    


    #probleme de date, je coupe pour que ca enelever la merde apres 
    emission = data["Emission"]
    Myclass.Emission = emission[0:10]

    dci = data["DCI"]
    Myclass.DCI = dci[0:10]
    

    dr1 = data["DR1"]
    Myclass.DR1 = dr1[0:10]
    Myclass.DPR = data["DPR"]

    dadr = data["DADR"]
    Myclass.DADR = dadr[0:10]
    
    dcf = data["DCF"]
    Myclass.DCF = dcf[0:10]

    dec = data["DEC"]
    Myclass.DEC = dec[0:10]

    
    Myclass.ADCF = data["ADCF"]
    Myclass.F0 = data["F0"]
    Myclass.TSJ = data["TSJ"]
    Myclass.PCS1 = data["PCS1"]
    Myclass.PCS2 = data["PCS2"]
    Myclass.PCS3 = data["PCS3"]
    Myclass.PCS4 = data["PCS4"]
    Myclass.PCS5 = data["PCS5"]

    Myclass.CPN = data["CPN"]
    Myclass.CPN_is_memoire = data["CPN_is_memoire"]
    Myclass.PDI = data["PDI"]
    Myclass.BAC = data["BAC"]
    Myclass.BAC_is_degressif = data["BAC_is_degressif"]
    Myclass.BCPN = data["BCPN"]
    Myclass.BCPN_is_degressif = data["BCPN_is_degressif"]

    Myclass.PEM = data["PEM"]
    Myclass.COM = data["COM"]
    Myclass.NSD = data["NSD"]
    Myclass.NSM = data["NSM"]
    Myclass.NSF = data["NSF"]
    Myclass.ABDAC = data["ABDAC"]
    Myclass.DBAC = data["DBAC"]
    Myclass.DEG = data["DEG"]
    Myclass.type_strike = data["type_strike"]
    Myclass.type_bar = data["type_bar"]
    Myclass.sous_jacent = data["sous_jacent"]



    main(Myclass)

    
    return "AHHHHH"

@app.route('/test', methods=["POST" , "GET"])
def test():
    print("?")
    if (request.method == "POST"):
        print("?????")
        # print(request.headers)
        # template = request.form["name"]
        print('-------------')
        #print(template)
        print("------------")

    return 'Hello, aaa!'


def remplissage_classe(request_form, Class):
        Class.template = request.form["template"]
        Class.Nom =  request.form["Nom"]
        Class.Typologie = request.form["Typologie"]
        Class.Droit = request.form["Droit"]
        Class.Isin = request.form["Isin"]
        Class.Emission = request.form["Emission"]
        Class.DCI = request.form["DCI"]
        Class.DR1 = request.form["DR1"]
        Class.DPR = request.form["DPR"]
        Class.DADR =  request.form["DADR"]
        Class.DCF =  request.form["DCF"]
        Class.DEC =  request.form["DEC"]
        Class.ADCF =  request.form["ADCF"]
        Class.F0 = request.form["F0"]
        Class.TSJ = request.form["TSJ"]
        Class.PCS1 = request.form["PCS1"]
        Class.PCS2 = request.form["PCS2"]
        Class.PCS3 = request.form["PCS3"]
        Class.PCS4 = request.form["PCS4"]
        Class.PCS5 = request.form["PCS5"]
        Class.CPN =  request.form["CPN"]
        Class.CPN_is_memoire =  request.form["CPN_is_memoire"]
        Class.PDI =  request.form["PDI"]
        Class.BAC =  request.form["BAC"]
        Class.BAC_is_degressif = request.form["BAC_is_degressif"]
        Class.BCPN = request.form["BCPN"]
        Class.BCPN_is_degressif = request.form["BCPN_is_degressif"]

        Class.PEM = request.form["PEM"]
        Class.COM = request.form["COM"]
        Class.NSD = request.form["NSD"]
        Class.NSM = request.form["NSM"]
        Class.NSF =  request.form["NSF"]

        Class.ABDAC = request.form["ABDAC"]
        Class.DBAC = request.form["DBAC"]
        Class.DEG = request.form["DEG"]


        Class.type_strike = request.form["type_strike"]
        Class.type_bar = request.form["type_bar"]

        Class.sous_jacent = request.form["sous_jacent"]
        Class.Template = request.form["Template"]

        
        #Class.typeoffre = ""
        #Class.sous_jacent_nom = ""


@app.route('/generate-pdf', methods=["POST" , "GET"])
def generate_pdf():
    Myclass = InformationsForm()

    if (request.method == "POST"):
        request.form["sous_jacent"]
        remplissage_classe(request, Myclass)
        main(Myclass)

        return("POUET POUET")

    else:
        main(Myclass)
        return("done")

