def SJR(Class):
    sousjacent = Class.sous_jacent

    #Réalisation des  phrases
    if sousjacent == "mono action":
        Class.SJR1 = "l’action"
        Class.SJR2 = "celle-ci"
        Class.SJR3 = "cours"
        Class.SJR4 = "de"
        Class.SJR5 = "cours"
        Class.SJR6 = "de l'action"
       
       
        Class.SJR7 = "de l'action"


    if sousjacent == "wo action":
        Class.SJR1 = "l’action la moins performante"
        Class.SJR2 = "celle-ci"
        Class.SJR3 = "cours"
        Class.SJR4 = "de"
        Class.SJR5 = "cours"
        Class.SJR6 = "des actions"
        Class.SJR7 = "de l'action la moins performante"

    if sousjacent == "equipondéré action":
        Class.SJR1 = "le panier équipondéré"
        Class.SJR2 = "celui-ci"
        Class.SJR3 = "niveau"
        Class.SJR4 = "du"
        Class.SJR5 = "niveaux"
        Class.SJR6 = "des actions"
        Class.SJR7 = "du panier équipondéré"


    if sousjacent == "mono indice":
        Class.SJR1 = "l'indice"
        Class.SJR2 = "celui-ci"
        Class.SJR3 = "niveau"
        Class.SJR4 = "niveau"
        Class.SJR5 = "niveaux"
        Class.SJR6 = "de" + str(Class.SJR1)
        Class.SJR7 = "de l'indice"


    if sousjacent == "wo indice":
        Class.SJR1 = "l'indice le moins performant"
        Class.SJR2 = "celui-ci"
        Class.SJR3 = "niveau"
        Class.SJR4 = "niveau"
        Class.SJR5 = "niveaux"
        Class.SJR6 = "des indices"
        Class.SJR7 = "de l'indice le moins performant"


    if sousjacent == "equipondéré indice":
        Class.SJR1 = "le panier équipondéré"
        Class.SJR2 = "celui-ci"
        Class.SJR3 = "niveau"
        Class.SJR4 = "niveau"
        Class.SJR5 = "niveaux"
        Class.SJR6 = "des indices"
        Class.SJR7 = "du panier équipondéré"


#equipondere action ou equipondéré indice