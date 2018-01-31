def median(arr):
    if len(arr) % 2 == 0:
        temp = arr[(len(arr) // 2) - 1]
        return (temp + arr[(len(arr) // 2)]) / 2
    return arr[(len(arr) // 2)]


size = int(input())
x = [int(val) for val in input().split()]
x = sorted(x)

#print the mean of the values before the middle value
print(int(median(x[:(size // 2)])))

#print the mean
print(int(median(x)))

#check the lenght of the 
if size % 2 == 0:
    print(int(median(x[(size // 2):])))
else:
    print(int(median(x[(size // 2) + 1:])))
