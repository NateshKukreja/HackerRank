import math 
n = 100
u = 500
r = 80
p = .95
z = 1.96

#Margin of Error
error = ( z * r )/ math.sqrt(n)
#Range
A = u - error
B = u + error
#Output
print(round(A, 2))
print(round(B, 2))
