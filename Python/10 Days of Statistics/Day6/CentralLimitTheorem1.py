pounds = 9800
boxes = 49
mean = 205
sigma = 15

import math

def limitTheorem(x, mean, std):
    return round(0.5 * (1 + math.erf((x - mean)/ (std * math.sqrt(2)))), 4)

print (limitTheorem(pounds, boxes * mean, math.sqrt(boxes) * sigma))
