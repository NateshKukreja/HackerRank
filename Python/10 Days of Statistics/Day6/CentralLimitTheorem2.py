tickets = 250
students = 100
mean = 2.4
sigma = 2.0

import math

def limitTheorem(x, mean, std):
    return round(0.5 * (1 + math.erf((x - mean)/ (std * math.sqrt(2)))), 4)

print (limitTheorem(tickets, students * mean, math.sqrt(students) * sigma))
