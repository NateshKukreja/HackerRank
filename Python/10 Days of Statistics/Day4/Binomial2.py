import math

def fact(n):
    return 1 if n == 0 else n*fact(n-1)

def comb(n, x):
    return fact(n) / (fact(x) * fact(n-x))

def b(k, n, p):
    return (math.factorial(n)/(math.factorial(k)*math.factorial(n-k))) * p**x * (1-p)**(n-x)
