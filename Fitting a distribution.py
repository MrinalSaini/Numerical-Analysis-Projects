# PROJECT - 4

## Importing Libraries
import numpy as np
import pandas as pd
from scipy.special import digamma, gamma
from math import log, exp
import matplotlib.pyplot as plt

## Importing the dataset
data=np.array([])
with open("data.txt","r") as f:
    for line in f.readlines():
        f_list=[float(i) for i in line.split(" ") if i.strip()]
        data=np.append(data,f_list)
f.close()

def f(x):
    return digamma(x) - log(np.prod(data))/996 - log(996/sum(data)) - log(x)

## Bisection Method Iterations
def bisection(a,b):
    if f(a)*f(b)>0:
        print("Both f(a\u2080) and f(b\u2080) are of same sign, give different input")
    else:
        tab = pd.DataFrame(columns = ['ai', 'bi', '(ai+bi)/2', 'f(ai+bi)/2'])
        tab = tab.append({'ai':a, 'bi':b, '(ai+bi)/2':(a+b)/2, 'f(ai+bi)/2':f((a+b)/2)}, ignore_index=True)
        while f((a+b)/2)!=0:
            if f((a+b)/2)*f(a)>0:
                a=(a+b)/2
            else:
                b=(a+b)/2
            tab = tab.append({'ai':a, 'bi':b, '(ai+bi)/2':(a+b)/2, 'f(ai+bi)/2':f((a+b)/2)}, ignore_index=True)
        print(tab)
        return (a+b)/2

## Finding the maximum likelihood estimators of a and p
c = float(input("a\u2080 = "))
d = float(input("b\u2080 = "))
if f(c)==0:
    p = c
    print("\np =",p)
    a = 996*p/sum(data)
    print("a =",a)
elif f(d)==0:
    p = d
    print("\np =",p)
    a = 996*p/sum(data)
    print("a =", a)
else:
    p = bisection(c,d)
    if p!=None:
        print("\np =",p)
        a = 996*p/sum(data)
        print("a =", a)

## Visualizing the Results
t = np.linspace(0,3,100)
ft = np.array([])
for i in t:
    ft = np.append(ft, [(a**p)*exp(-a*i)*(i**(p-1))/gamma(p)])
plt.plot(t, ft, color = 'blue')
plt.hist(data, bins = 20, color = 'orange', density = True)
plt.show()
