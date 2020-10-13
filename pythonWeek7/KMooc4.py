# 연습문제 1

num = int(input("List element 개수 입력: ")) 
NewList = []
tempList = [0]

for i in range(num):
    print(i+1, "번째")
    t = input( "추가할 element 입력 :")
    tempList = [t]
    NewList = NewList + tempList 

print(NewList)