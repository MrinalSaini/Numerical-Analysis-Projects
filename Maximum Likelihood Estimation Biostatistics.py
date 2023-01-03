# PROJECT 3

## Importing Libraries
from sympy import Symbol, diff, lambdify

## Newton Raphson Iterations
def Newt_iter(f, df, p):
    x = p-(f(p)/df(p))
    i = 1
    print("x%d ="%(i), x)
    while x != p:
        i = i+1
        p = x
        x = x-(f(x)/df(x))
        print("x%d ="%(i), x)
    return x

## Finding the derivatives of the likelihood
p = Symbol('p')
l = (p**46)*(1-p**2)**77
l_1 = diff(l, p)
l_2 = diff(l_1, p)

L = lambdify(p, l)
dL = lambdify(p, l_1)
d2L = lambdify(p,l_2)

print("OBJECTIVE : To find p for which L(p) = p\u2074\u2076(1-p\u00b2)\u2077\u2077 is maximum\n")

## Finding the MLE of p using Newton Raphson Method
print("Newton-Raphson iterations :")
x = Newt_iter(dL,d2L,float(input("x0 = ")))
print("\nMaximum likelihood estimator of p =", x)
print("Derivative at MLE =", dL(x))
print("Second derivative at MLE =", d2L(x))




