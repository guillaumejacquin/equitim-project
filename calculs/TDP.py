
def TDP(Class):
    is_index = True

    #on filtre le tableau en enlevant les cases vides (si l utilisateur prend 3 choix, on enlevera les2 derniers)
    Class.TSJ = list(filter(("").__ne__, Class.TSJ))

    for i in Class.TSJ:
        if not "index"  or "Index" or "INDEX" in  i:
            is_index = False
            break

    if is_index == False:
        Class.TDP = "indice"
    else:
        Class.TDP = "action"




