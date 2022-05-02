def boucleTRA(Class, date1, date2, date3, variable=100):
    first_date = date1 #max entre date émission et strike
    second_date = date2 #date_echeance
    third_date = date3

    flux_var = variable #Scenario Defavorable = flux_var
    first_date = datetime.strptime(first_date, '%Y-%m-%d')
    dates = [second_date, third_date]

    print("allez stp")
    #la ca doit boucler sa mere
    for i in dates:
        print("oui")

        flux_var2 = variable +1

        print("ici1")
        def flux(second_date, flux_var):
            second_date = datetime.strptime(second_date, '%Y-%m-%d')
            soustract2dates = abs(first_date - second_date)
            soustract2dates = soustract2dates.days
            flux_varNet = float(flux_var)*0.99**(float(soustract2dates)/365)
            return(flux_varNet)
        print("ici2")

        flux_varNet = flux(second_date, flux_var)
        print("ici3")

        flux_var = variable +1
        flux_varNet2 = flux(third_date, flux_var)
        print("ici3")
   

    result = (xirr([first_date,second_date, third_date], [-100, float(flux_varNet), float(flux_varNet2)]))

    try:
        result = float(result) *100
        result = round(result, 2)
        result = (f'{result:.2f}')

    except Exception:
        pass
    print("ici4")

    return(result)