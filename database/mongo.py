import site
import pymongo
from pymongo import MongoClient

#ajoute une valeud dans la collection clients qui se trouve dans la base de donnees templates
def add_value_data_base(ticker, equity, dividende="", sponsor="", siteweb="", inconvénient=""):
    cluster = MongoClient("mongodb+srv://guillaume:guigui@cluster0.eczef.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

    db = cluster["templates"]
    collection = db["clients"]

    post1 = {"Ticker": ticker, "Equity" : equity, "Dividende": dividende, "Sponsor": sponsor, "SiteWeb": siteweb, "Inconvénient": inconvénient}

    collection.insert_one(post1)

# add_value_data_base("Cac50", "ca")


#montre les valeurs de la base de la collections clients de la base de données templates
def show_database():
    cluster = MongoClient("mongodb+srv://guillaume:guigui@cluster0.eczef.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

    db = cluster["templates"]
    collection = db["clients"]
    list_elements_database = []
    for x in collection.find({}, {"_id":0, "Libelle": 1, "Ticker": 1 }): 
        list_elements_database.append(x)

    return(list_elements_database)


# show_database()

from openpyxl import load_workbook

def add_value():
    file_path = 'Classeur1.xlsx'
    wb = load_workbook(file_path)
    ws = wb['Feuil1']  # or wb.active
    
    i = 2
    while True:
        mystring = "A" + str(i)
        secondstring = "B" + str(i)

        if (ws[mystring].value is None):
            exit (2)

        if (ws[mystring].value is None):   
            ws[mystring].value = " "
        add_value_data_base(ws[mystring].value, ws[secondstring].value)
        i+=1
    wb.save(file_path)
# add_value()


def takeinformations(Class):
    #Recupere le sous jacent
    cluster = MongoClient("mongodb+srv://guillaume:guigui@cluster0.eczef.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

    db = cluster["templates"]
    collection = db["clients"]

    #remplacer par le bon element(ici ticker)
    results = collection.find({"Ticker":"CA FP Equity"})

    for result in results:
        Class.NOMSOUSJACENT = result["Ticker"]
        Class.DIVIDENDE = result["Dividende"]
        Class.SPONSOR = result["Sponsor"]
        Class.Site = result["SiteWeb"]
        Class.Ticker = result["Ticker"]
