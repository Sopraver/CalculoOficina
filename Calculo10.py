import sympy

def calculo():
    y = float(input("Insira o valor de Y: "))
    x = sympy.Symbol("numero")
    equacao = sympy.Eq(x - 0.1 * x, y)
    resultado = sympy.solve([equacao], (x,))
    print(resultado)

