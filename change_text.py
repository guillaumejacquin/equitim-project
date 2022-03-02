from cmd import Cmd
from dataclasses import dataclass
from typing import List
from unicodedata import name
from pptx import Presentation


#TOUS LES REMPLACEMENTS 
def elementsToReplaceRemplacement(Class, shapes):

    replace_text({'<Nom>':  Class.Nom}, shapes)
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
    replace_text({'<CPN>':  cpn}, shapes)
    pdi = Class.PDI + "%"
    replace_text({'<PDI>':  pdi}, shapes)


    #on rjaoute les % sans que ca ait un impact sur les calculs
    bac = Class.BAC + "%"
    replace_text({'<BAC>':  bac}, shapes)
    replace_text({'<BCPN>':  Class.BCPN}, shapes)
    replace_text({'<PEM>':  Class.PEM}, shapes)
    com = str(Class.COM) + "%"
    replace_text({'<COM>':  com}, shapes)
    nsd = Class.NSD + "%"
    replace_text({'<NSD>':  nsd}, shapes)
    replace_text({'<NSM>':  Class.NSM}, shapes)
    replace_text({'<NSF>':  Class.NSF}, shapes)
    replace_text({'<ABDAC>':  Class.ABDAC}, shapes)
    dbac = str(Class.DBAC) + "%"
    replace_text({'<DBAC>':  dbac}, shapes)
    replace_text({'<DEG>':  Class.DEG}, shapes)

def elementsToReplaceCalcul(Class, shapes):
    replace_text({'<DDCI>': Class.DDCI}, shapes) 
    replace_text({'<F0s>':  Class.F0s}, shapes)


    replace_text({'<1PDC>': Class.PDC1_affichage}, shapes) 
 
    replace_text({'<2PDC>': Class.PDC2_affichage}, shapes) 
    replace_text({'<DDR>': Class.DDR}, shapes)
    replace_text({'<DIC>': Class.DIC}, shapes)
    
    pdiperf = str(Class.PDIPERF) + "%"
    replace_text({'<PDIPERF>': pdiperf}, shapes)
    replace_text({'<1PR>': Class.PR1}, shapes)
    replace_text({'<DPRR>': Class.DPRR}, shapes)
    replace_text({'<TDP>': Class.TDP}, shapes)
    replace_text({'<GC>': Class.GC}, shapes)
    gca = str(Class.GCA) + "%"
    replace_text({'<GCA>': gca}, shapes)
    gce = str(Class.GCE) + "%"
    replace_text({'<GCE>': gce}, shapes)
    abac = str(Class.ABAC) + ""
    replace_text({'<ABAC>': abac}, shapes)
    replace_text({'<NDR>': Class.NDR }, shapes)
    replace_text({'<ADPR>': Class.ADPR}, shapes)
    replace_text({'<SJR1>': Class.SJR1}, shapes)
    replace_text({'<SJR2>': Class.SJR2}, shapes)
    replace_text({'<SJR3>': Class.SJR3}, shapes)
    replace_text({'<SJR4>': Class.SJR4}, shapes)
    replace_text({'<SJR5>': Class.SJR5}, shapes)
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
    replace_text({'<test>': "TESTTTTTTTTTTTTTTT"}, shapes)










    #CHANGER LE NOM DE LA BALISE ET DE LA CLASS dans myclass.py
    replace_text({'<balise>': Class.balise}, shapes)




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

    elementsToReplaceRemplacement(Class, shapes)
    elementsToReplaceCalcul(Class, shapes)
    prs.save(NAME)
