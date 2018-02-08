import math

mean = 70
std = 10

cdf = lambda x: 0.5 * (1 + math.erf((x - mean) / (std * (2 ** 0.5))))
print(round(100 - cdf(80) * 100,2))
print(round(100 - cdf(60) * 100,2)) 
print(round(cdf(60) * 100,2))
