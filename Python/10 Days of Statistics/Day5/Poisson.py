# Dependencies
from math import factorial
from math import exp

# Define Poisson distribution
def Poisson(k, lam):
    return (lam**k * exp(-lam))/(factorial(k))

# Input from stdin
average = float(input())
variable = float(input())

# Probability
print(round(Poisson(variable, average), 3))
