# 연습하기 4번 
from copy import *

numList = [1,3,5,7,9]
numshallow = numList
numdeep = deepcopy(numList)


print("numList =", numList)
print("numshallow = ", numshallow)
print("numdeep = ", numdeep)

numshallow.append(222)
numdeep.append(999)

print("numList =", numList)
print("numshallow = ", numshallow)
print("numdeep = ", numdeep)