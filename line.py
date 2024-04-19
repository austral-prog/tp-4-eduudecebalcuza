import math
def line():
    a = float(input('Ingrese el coeficiente A:'))
    b = float(input("Ingrese el coeficiente B:"))
    x1 = float(input("Ingrese el coeficiente X1:"))
    x2 = float(input("Ingrese el coeficiente X2:"))
    print('El coeficiente A de su ecuación de la recta es:', a)
    print('El coeficiente B de su ecuación de la recta es:', b)
    print('El coeficiente X1 de su ecuación de la recta es:', x1)
    print('El coeficiente X2 de su ecuación de la recta es:', x2)

    print('\nPara la siguiente ecuación:')
    ecuacion = f"Y = {a}X + {b}"
    print(f'\t{ecuacion}\n')

    print('Dados los siguientes puntos:')
    print(f'\tP1 ({x1}, {a * x1 + b})')
    print(f'\tP2 ({x2}, {a * x2 + b})\n')
    

    y1 = a * x1 + b
    p1 = (x1,y1)
    
    y2 = a * x2 + b
    p2 = (x2, y2)
    

    print(f'La distancia entre ellos es: {math.dist(p1, p2)}')
