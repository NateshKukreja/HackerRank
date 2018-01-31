def weightedMean(size, values, occurances):
    val_sum = 0;
    occ_sum = 0
    for i in range(size):
        occ_sum+=occurances[i]
        val_sum += values[i]*occurances[i]
    return (round(val_sum/occ_sum, 1))

size = input()
value = input().split()
occurance = input().split()
values = []
occurances=[]
for i in value:
    values.append(int(i))

for i in occurance:
    occurances.append(int(i))


    
print(weightedMean(int(size), values, occurances))
