from sympy import *
x = symbols("x")

lim = 1e100000

y1 = factorial(2*(x+1)) * (x ** (2 * x))
y2 = ((x + 1) ** (2 * (x + 1)) * factorial(2 * x))

derivativesY1 = []
derivativesY2 = []

derivativesY1.append(y1)
derivativesY2.append(y2)

derivative = 0
locked = True
while locked:
    derivativesY1.append(diff(derivativesY1[derivative], x))
    derivativesY2.append(diff(derivativesY2[derivative], x))

    if derivativesY1[derivative].subs(x, lim)/derivativesY2[derivative].subs(x, lim) != nan and abs(derivativesY1[derivative].subs(x, lim)/derivativesY2[derivative].subs(x, lim)) != oo and abs(derivativesY1[derivative].subs(x, lim)/derivativesY2[derivative].subs(x, lim)) != zoo:
        locked = False
        print(derivative)
        print(derivativesY1[derivative].subs(x, lim) / derivativesY2[derivative].subs(x, lim))
    if derivative % 100 == 0 and derivative != 0:
        print(derivative)
    derivative += 1
