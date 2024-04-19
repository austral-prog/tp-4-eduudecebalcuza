def leap_year():
    year1 = int(input('Ingrese su año:'))
    if year1 % 4 == 0:
        if year1 % 400 == 0: 
            print(f'El año {year1} es bisiesto')
        elif year1 % 400 != 0: 
            print(f'El año {year1} no es bisiesto')
    else:
        print(f'El año {year1} no es bisiesto')
