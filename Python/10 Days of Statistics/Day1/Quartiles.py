import math

def quartiles(size, values):
    if(size%2 != 0):
    
        split = math.floor(size/2)
        firstHalf = []
        secondHalf = []
    
        for i in range(split):
            firstHalf.append(values[i])
        
        for i in range(split+1, size):
            secondHalf.append(values[i])
        
        firstHalf.sort()
        meanFH = 0

        if(len(firstHalf)%2==0):
            meanFH+=(firstHalf[int(len(firstHalf)/2)] + firstHalf[int((len(firstHalf)/2))-1])
            meanFH = meanFH/2
        else:
            meanFH+=firstHalf[math.floor(len(firstHalf)/2)]

        secondHalf.sort()
        meanSH = 0
        if(len(secondHalf)%2 == 0):
            meanSH+=(secondHalf[int(len(secondHalf)/2)] + secondHalf[int(len(secondHalf)/2)-1])
            meanSH = meanSH/2        
        else:
            meanSH += secondHalf[math.floor(int(len(secondHalf)/2))]
        print(int(meanFH))
        print(values[math.floor(size/2)])
        print(int(meanSH))

    else:
        mean+=(values[size/2]+values[(size/2)-1])
        mean = mean/2
        split = math.floor(size/2)
        firstHalf = []
        secondHalf = []
    
        for i in range(split):
            firstHalf.append(values[i])
        
        for i in range(split+1, size):
            secondHalf.append(values[i])
        
        firstHalf.sort()
        meanFH = 0
        if(len(firstHalf)%2==0):
            meanFH+=(firstHalf[int(len(firstHalf)/2)] + firstHalf[(int(len(firstHalf)/2))-1])
            meanFH = meanFH/2
        else:
            meanFH+=firstHalf[math.floor(int(len(firstHalf))/2)]

        secondHalf.sort()
        meanSH = 0
        if(len(secondHalf)%2 == 0):
            meanSH+=(secondHalf[int(len(secondHalf)/2)] + secondHalf[(int(len(secondHalf)/2))-1])
            meanSH = meanSH/2        
        else:
            meanSH += secondHalf[math.floor(int(len(secondHalf)/2))]
        print(int(meanFH))
        print(values[math.floor(size/2)])
        print(int(meanSH))

                     
size = input()
inputVal = input().split()

values = []
for val in inputVal:
    values.append(int(val))
size = int(size)
quartiles(size, values)
