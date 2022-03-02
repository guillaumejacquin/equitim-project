def SJR(Class):
    sousjacent = Class.sous_jacent

    #Réalisation des  phrases
    if sousjacent == "mono action":
        Class.SJR1 = "l’action"
        Class.SJR2 = "celle-ci"
        Class.SJR3 = "cours"
        Class.SJR4 = "de"
        Class.SJR5 = "cours"

    if sousjacent == "wo action":
        Class.SJR1 = "l’action la moins performante"
        Class.SJR2 = "celle-ci"
        Class.SJR3 = "cours"
        Class.SJR4 = "de"
        Class.SJR5 = "cours"

    if sousjacent == "equipondéré action":
        Class.SJR1 = "le panier équipondéré"
        Class.SJR2 = "celui-ci"
        Class.SJR3 = "niveau"
        Class.SJR4 = "du"
        Class.SJR5 = "niveaux"

    if sousjacent == "mono indice":
        Class.SJR1 = "l'indice"
        Class.SJR2 = "celui-ci"
        Class.SJR3 = "niveau"
        Class.SJR4 = "niveau"
        Class.SJR5 = "niveaux"

    if sousjacent == "wo indice":
        Class.SJR1 = "l'indice le moins performant"
        Class.SJR2 = "celui-ci"
        Class.SJR3 = "niveau"
        Class.SJR4 = "niveau"
        Class.SJR5 = "niveaux"

    if sousjacent == "equipondéré indice":
        Class.SJR1 = "le panier équipondéré"
        Class.SJR2 = "celui-ci"
        Class.SJR3 = "niveau"
        Class.SJR4 = "niveau"
        Class.SJR5 = "niveaux"