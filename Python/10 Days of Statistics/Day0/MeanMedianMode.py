from statistics import mode

def mean(arrSize, arr):
    sum = 0
    for i in arr:
        sum+=int(i)
    print(sum/int(arrSize))
    
def median(arrSize, arr):
    size = int(arrSize)
    if(size%2 == 0):
        var1 = (arr[int(size/2)])
        var2 = (arr[int(size/2)-1])
        print((var1+var2)/2)
    else:
        print((arr[size/2]))
    
def mode(lis):
    dictionary = {}
    lis.sort()
    for val in lis:
        dictionary[val] = 0
    
    for val in lis:
        if(dictionary[val] >=0):
            dictionary[val] += 1
        
        else:
            dictionary[val] = 1
    sorted(dictionary.keys())
    count = 0
    index = 0
    for val in lis:
        if dictionary[val]>count:
            count = dictionary[val]
            index = val
    print(index)

size = input()
array = input().split()
lis = []
for a in array:
    lis.append(int(a))
lis.sort()
mean(size, lis)
median(size, lis)
(mode(lis))

