def interquartile(s):
    if(len(s)%2==0):
        return(((s[len(s)//2-1])+(s[len(s)//2]))/2)
    else:
        return s[len(s)//2]

size = int(input())
values = [int(val) for val in input().split()]
occurances = [int(occ) for occ in input().split()]

s = []
for index in range(size):
    for i in range(occurances[index]):
        s.append(values[index])
s.sort()

if len(s)%2==0:
    print(round((interquartile(s[len(s)//2:])-interquartile(s[:len(s)//2])),1))

else:
    print(round((interquartile(s[len(s)//2+1:])-interquartile(s[:len(s)//2-1])),1))

