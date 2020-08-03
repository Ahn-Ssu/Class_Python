#튜플 
# 리스트와 동일하지만, 튜플은 변경이 불가능 함 
listEx = [1,2,3]
tupleEx = (1,2,3)  # lock이 걸려 있음 | 길이 고정, 값 고정

#del tupleEx[0] # TypeError: 'tuple' object doesn't support item deletion


print(tupleEx[0:2]*2)

#------------------------------------------#
#딕셔너리(사전)
#루비에선 Hash, 자바에선 Map, JS에선 Object, JSON(JavaScript Object Notation) 으로 불림 
#키-값 쌍의 패턴을 가짐 | Key-Value 
dicEx = {'nane':'AhnSsu','age':24}
print(dicEx)

dicEx['major'] = "CSEE"
print(dicEx)

print(dicEx.keys())
print(dicEx.values())
print(dicEx.items())

for item in dicEx.items():
    print(item)

#------------------------------------------#
#집합 | 진짜 집합 성질을 그냥 파이썬으로 만든 거임 
#데이터를 다룰 때 사용하게 됨 
#중복제거 예시 
dupleList = [1,222,222,3,3,4,5,5,6]
newList = list(set(dupleList))
print(newList)

strSet = set("BABO")
print(strSet) # B, O, A | 순서 없음, 실행시킬 때 마다 다름 

set1 = set([1,2,3,4,5,6])
set2 = set([4,5,6,7,8,9])
print(set1 & set2)
print(set1.intersection(set2))

print(set1 | set2)
print(set1.union(set2))

#print(set1 + set2) # 지원 안함 
print(set1 - set2)
print(set1.difference(set2))


#------------------------------------------#
#불, 대문자로 찍어주세용
print(type(True))
if []:
    print("True")
    print(strSet)

lineUp = [1,2,3,4,5]
while lineUp:
    print(lineUp)
    lineUp.pop()
    


#------------------------------------------#
#변수 
#메모리에서 실제로 값을 저장한 곳의 주소를 가지는 것

#변수는 초기화 시 주소 값을 할당 받음 
#주소 값은 메모리의 상의 주소 값
#value(객체)를 해당 주소 메모리에 위치 시키고 메모리 주소를 변수가 가지고 있는 것
#http://pythontutor.com/live.html#mode=edit 
# 위 사이트는 메모리의 관계를 직관적으로 볼 수 있는 사이트이다. 
intNum = 1

listEx = [1,2,3,4]
copyListEx = listEx
deepCopyListEx = list(listEx)

listEx[2] = 9
slicListEx = listEx[:]


k = [1,2,3]
l = k 
ks = k[:]
print(id(k))
print(k is l)