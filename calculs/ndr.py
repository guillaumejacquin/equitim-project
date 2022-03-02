def ndr(Class):
    if Class.TDP == "action" and Class.type_strike == "strike normal":
        Class.NDR = "Cours Initial" #la

    elif Class.TDP == "action" and (Class.type_strike == "best strike" or Class.type_strike == "strike moyen"):
        Class.NDR = "Cours de Référence"

    elif Class.TDP == "indice" and Class.type_strike == "strike normal":
        Class.NDR = "Niveau Initial" #celui la

    elif Class.TDP == "indice" and (Class.type_strike == "best strike" or Class.type_strike == "strike moyen"):
        Class.NDR = "Niveau de Référence"

    else:
        Class.NDR = "ERREUR!!!!!!"


#quand c 'est action  et strike normal ndr  = cours initial 
# si action et best strike ou strike moyenne = cours de reférence
# #quand c 'est indice  et strike normal ndr  = niveau initial

# si indice et best strike ou strike moyenne = niveau de référence
#quand c est panier on dit niveau de référence ou niveau initial