import math

def b(k, n, p):
    return ((math.factorial(n)/(math.factorial(k)*math.factorial(n-k))) * p**k * (1-p)**(n-k))

s = input().split()

p = int(s[0])
n = int(s[1])

print(round(sum([b(i, n, p/100) for i in range(3)]), 3))
print(round(1-sum([b(i, n, p/100) for i in range(0, 2)]), 3))
