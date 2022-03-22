def abac(Class):
    if (Class.BAC_is_degressif != ""):
        Class.ABAC = "la barrière dégressive de remboursement anticipé automatique"

    else:
        mystring = str(Class.BAC) + "%"
        Class.ABAC = mystring
