import math

def binomial(n, k, p, q):
    
    choose = math.factorial(n)/(math.factorial(k)*math.factorial(n-k))
    return choose*(p**k)*(q**(n-k))

inputVal = input().split()
boys = float(inputVal[0])
girls = float(inputVal[1])

probability = 0
for i in range(3, 7):
    probability+=binomial(6, i, boys/(boys+girls), girls/(boys+girls))

print(round(probability, 3))
