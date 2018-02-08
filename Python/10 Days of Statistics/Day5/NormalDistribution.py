import math

mean = 20
std = 2
q1 = 19.5
q2_1 = 20
q2_2 = 22

cdf = lambda x: 0.5 * (1 + math.erf((x - mean) / (std * (2 ** 0.5))))
print(round(cdf(19.5),3))
print(round(cdf(22)-cdf(20),3))
