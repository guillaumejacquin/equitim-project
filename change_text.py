from cmd import Cmd
from dataclasses import dataclass
from typing import List
from unicodedata import name
from calculs.abac import abac
from pptx import Presentation
from PIL import Image
from pptx.util import Inches
from pptx.enum.text import PP_ALIGN
import os
def elementsToReplaceDegressivite(Class, shapes):
    #si degressif on supprime les balises
    if Class.BAC_is_degressif == "oui":
        Class.desonndr = ""
        Class.longuephrase = ""
        Class.SDBAC = ""
        Class.PDINSM = ""
        Class.ETPDI = ""

#TOUS LES REMPLACEMENTS 
def elementsToReplaceRemplacement(Class, shapes):
    #mise en avant car transforme en bac

    replace_text({'<NDRTES>': Class.desonndr}, shapes)
    replace_text({'<longuephrase>': Class.longuephrase}, shapes)
    replace_text({'<SDBAC>': Class.SDBAC}, shapes)
    replace_text({'<PDINSM>': Class.PDINSM}, shapes)
    replace_text({'<TEST>': Class.ETPDI}, shapes) 

    replace_text({'<EBAC>': Class.EBAC}, shapes) 

    replace_text({'<NOM>':  Class.Nom}, shapes)
    replace_text({'<droit>':  Class.Droit}, shapes)
    replace_text({'<ISIN>':  Class.Isin}, shapes)
    replace_text({'<émission>':  Class.Emission_affichage}, shapes)
    replace_text({'<DCI>':  Class.DCI}, shapes)
    replace_text({'<1DR>':  Class.DR1_affichage}, shapes)
    replace_text({'<DPR>':  Class.DPR_affichage}, shapes)
    replace_text({'<DCF>':  Class.DCF_affichage}, shapes)
    replace_text({'<DEC>':  Class.DEC_affichage}, shapes)
    replace_text({'<F0>':  Class.F0}, shapes)
    replace_text({'<DDCI>':  Class.DDCI_affichage}, shapes)
    replace_text({'<TSJ1>':  Class.TSJ[0]}, shapes)
    # replace_text({'<TSJ2>':  Class.TSJ2}, shapes)
    # replace_text({'<TSJ3>':  Class.TSJ3}, shapes)
    # replace_text({'<TSJ4>':  Class.TSJ4}, shapes)
    # replace_text({'<TSJ5>':  Class.TSJ5}, shapes)
    replace_text({'<PCS1>':  Class.PCS1}, shapes)
    replace_text({'<PCS2>':  Class.PCS2}, shapes)
    replace_text({'<PCS3>':  Class.PCS3}, shapes)
    replace_text({'<PCS4>':  Class.PCS4}, shapes)
    replace_text({'<PCS5>':  Class.PCS5}, shapes)
    cpn = Class.CPN + "%"
    cpn = cpn.replace(".", ",")
    replace_text({'<CPN>':  cpn}, shapes)
    pdi = Class.PDI + "%"
    replace_text({'<PDI>':  pdi}, shapes)

    replace_text({'<ADCF>': Class.ADCF_affichage}, shapes) 

    #on rjaoute les % sans que ca ait un impact sur les calculs
    bac = Class.BAC + "%"
    bac = bac.replace(".", ",")

    replace_text({'<BAC>':  bac}, shapes)
    replace_text({'<BCPN>':  Class.BCPN}, shapes)
    pem = str(Class.PEM) + "%"
    replace_text({'<PEM>':  pem}, shapes)
    com = str(Class.COM) + "%"
    com = com.replace(".", ",")
    replace_text({'<COM>':  com}, shapes)
    nsd = Class.NSD + "%"
    replace_text({'<NSD>':  nsd}, shapes)
    nsm = Class.NSM + "%"
    replace_text({'<NSM>':  nsm}, shapes)
    nsf = str(Class.NSF) + "%"
    replace_text({'<NSF>':  nsf}, shapes)
    replace_text({'<ABDAC>':  Class.ABDAC}, shapes)
    dbac = str(Class.DBAC) + "%"
    dbac = dbac.replace(".", ",")

    replace_text({'<DBAC>':  dbac}, shapes)
    replace_text({'<DEG>':  Class.DEG}, shapes)

def elementsToReplaceCalcul(Class, shapes):
    replace_text({'<balisedeg1>': Class.balisedeg}, shapes) 
    replace_text({'<balisedeg2>': Class.balisedeg2}, shapes)     
    replace_text({'<balisedeg3>': Class.balisedeg3}, shapes) 
    replace_text({'<baliseCM>': Class.baliseCM}, shapes) 
    replace_text({'<baliseCM2>': Class.baliseCM2}, shapes)
    replace_text({'<baliseCM22>': Class.baliseCM22}, shapes) 

    replace_text({'<baliseCM3>': Class.baliseCM3}, shapes) 
    replace_text({'<baliseCM4>': Class.baliseCM4}, shapes)
    replace_text({'<SV>': Class.SV}, shapes) 

    replace_text({'<DDCI>': Class.DDCI}, shapes) 


    replace_text({'<F0s>':  Class.F0s}, shapes)


    replace_text({'<1PDC>': Class.PDC1_affichage}, shapes) 
    
    replace_text({'<2PDC>': Class.PDC2_affichage}, shapes) 
    replace_text({'<DDR>': Class.DDR}, shapes)
    replace_text({'<DIC>': Class.DIC}, shapes)
    
    pdiperf = str(int(Class.PDIPERF)) + "%"
    pdiperf = pdiperf.replace(".", ",")

    replace_text({'<PDIPERF>': pdiperf}, shapes)
    replace_text({'<1PR>': Class.PR1}, shapes)
    replace_text({'<DPRR>': Class.DPRR}, shapes)
    replace_text({'<TDP>': Class.TDP}, shapes)
    replace_text({'<GC>': Class.GC}, shapes)
    gca = str(Class.GCA) + "%"
    gca = gca.replace(".", ",")

    replace_text({'<GCA>': gca}, shapes)
    gce = str(Class.GCE) + "%"
    gce = gce.replace(".", ",")

    replace_text({'<GCE>': gce}, shapes)
    replace_text({'<ABAC>': Class.ABAC}, shapes)
    replace_text({'<NDR>': Class.NDR }, shapes)
    replace_text({'<ADPR>': Class.ADPR}, shapes)
    replace_text({'<SJR1>': Class.SJR1}, shapes)
    replace_text({'<SJR2>': Class.SJR2}, shapes)
    replace_text({'<SJR3>': Class.SJR3}, shapes)
    replace_text({'<SJR4>': Class.SJR4}, shapes)
    replace_text({'<SJR5>': Class.SJR5}, shapes)
    replace_text({'<SJR6>': Class.SJR6}, shapes)
    replace_text({'<SJR7>': Class.SJR7}, shapes)

    replace_text({'<F1>': Class.F1}, shapes)
    replace_text({'<F2>': Class.F2}, shapes)

    replace_text({'<TDS>': Class.TDS}, shapes)
    replace_text({'<DU>': Class.DU}, shapes)

    replace_text({'<sponsor>': Class.sponsor}, shapes)
    replace_text({'<SPONSOR>': Class.SPONSOR}, shapes)

    replace_text({'<TICKER>': Class.TICKER}, shapes)
    replace_text({'<NOMSOUSJACENT>': Class.NOMSOUSJACENT}, shapes)
    replace_text({'<DIVIDENDE>': Class.DIVIDENDE}, shapes)
    replace_text({'<SITE>': Class.Site}, shapes)
    replace_text({'<DPCI>': Class.DPCI}, shapes) 


    #CHANGER LE NOM DE LA BALISE ET DE LA CLASS dans myclass.py
    replace_text({'<balise>': Class.balise}, shapes)

    hardcode_replace(Class, shapes)

def hardcode_replace(Class, shapes):
    replace_text({"l' année": "l'année"}, shapes)
    

#PREMIER RAPPEL A DATE DERNIER RAPPEL

#avoir toutes les slides
def getAllSlides(prs):
    slides = [slide for slide in prs.slides]
    shapes = []

    for slide in slides:
        for shape in slide.shapes:
            shapes.append(shape)
    return shapes

#remplace le texte sur le ppt 
def replace_text(replacements: dict, shapes: List):
    for shape in shapes:
        for match, replacement in replacements.items():
            if shape.has_text_frame:
                if (shape.text.find(match)) != -1:
                    text_frame = shape.text_frame
                    for paragraph in text_frame.paragraphs:

                        for run in paragraph.runs:
                            cur_text = run.text
                            new_text = cur_text.replace(str(match), str(replacement))
                            run.text = new_text


            if shape.has_table:
                for row in shape.table.rows:
                    for cell in row.cells:
                        if match in cell.text:
                            new_text = cell.text.replace(match, replacement)
                            cell.text = new_text


#load le ppt, remplace les balises et le sauvegarde
def ChangeTextOnPpt(Class):
    NAME = "result/"+ Class.Nom + "- " + Class.Isin + "result.pptx" 
    prs_string = "templates/"+ Class.template + ".pptx" 
    prs = Presentation(prs_string)
    shapes = getAllSlides(prs)
    Class.shapes = shapes
    elementsToReplaceDegressivite(Class, shapes)
    elementsToReplaceRemplacement(Class, shapes)
    elementsToReplaceCalcul(Class, shapes)

    #on repasse une 2 eme fois au cas ou certaines transformations soient mal placées
    elementsToReplaceDegressivite(Class, shapes)
    elementsToReplaceRemplacement(Class, shapes)
    elementsToReplaceCalcul(Class, shapes)
    
    compteur = 0
    for shape in Class.shapes:
        textbox = shape
        for i in Class.deleteblocs:

            try:
                if (i in textbox.text):
                        print("paragraphe supprimé")
                        compteur+=1
                        sp = textbox.element
                        sp.getparent().remove(sp)

            except Exception:
                pass
            
    if compteur > 1:
        print(compteur, "paragraphes ont été supprimés")
    else:

        print(compteur, "paragraphe a été supprimé")

    compteur = 0

    for slide in prs.slides:
        for shape in slide.shapes:

            if shape.has_text_frame:
                
                if ("<graph1>" in shape.text):
                    cur_text = shape.text
                    new_text = cur_text.replace(str("<graph1>"), str(""))
                    shape.text = new_text
                    pic = slide.shapes.add_picture("graph1.png", Inches(0), Inches(6.75), Inches(7))
                
                if ("<graph2>" in shape.text):  
                    cur_text = shape.text
                    new_text = cur_text.replace(str("<graph2"), str(""))
                    shape.text = new_text
                    pic = slide.shapes.add_picture("graph2.png", Inches(0), Inches(2), Inches(4.25))

                if ("<graph5>" in shape.text):  
                        cur_text = shape.text
                        new_text = cur_text.replace(str("<graph5>"), str(""))
                        shape.text = new_text
                        pic = slide.shapes.add_picture("graph2.png", Inches(0), Inches(5.25), Inches(7))

    

    try:
        print("Nettoyage du projet, supression des documents inutiles")
        os.remove("graph1.png")
        print("Suppression de graph1.png")
        os.remove("graph2.png")
        print("Suppression de graph2.png")
        os.remove("graph3.png")
        print("Suppression de graph3.png")
        os.remove("graph4.png")
        print("Suppression de graph4.png")
        os.remove("graph5.png")
        print("Suppression de graph5.png")

    except Exception:
        print("OH NONNNN")
    prs.save(NAME)


