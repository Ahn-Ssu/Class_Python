L = [1,2,3]
print(L + L )
print("L :",L)
# 출력하는 다른 방법 
print("L[-1] :",L[-1])
print(L*4)

L = list(range(10))
print(L)

L.append(10)
print(L)

L.reverse()
print(L)

L.sort()
print(L)

# 리스트랑 거의 동일 소괄호 사용함
t = (1,2,3)
 # 괄호를 안쳐도 튜플임
tupleEx = 1,2,3,4
print(type(tupleEx)) # <class 'tuple'>
# 근데 튜플은 값을 변경할 수 없음 
