targetNumber = int(input())


totalMax = 0 
for i in range(1,targetNumber+1):
    totalMax += i
    if(totalMax>targetNumber):
        break

print(totalMax)