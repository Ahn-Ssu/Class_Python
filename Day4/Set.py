#집합(set)은 여러 값을 순서 없이 그리고 중복 없이 모아 놓은 자료형이다.
# 집합의 자료형은 2가지 종류가 있는데 변경이 가능한 set, 변경이 불가능한 frozenset이 있다.

a = set() # empty set 
d = {} # 이렇게 생성하면 '빈 사전'으로 인식을 하기 때문에 안된다. 
b = {1,2,3}
a = b.copy()

#set() 함수
set((1,2,3)) # 튜플로 집합 생성
set('abcd') # 문자열로 집합을 만든다 ; {'a', 'b', 'c', 'd'}
set([11,2,3]) # 리스트로 집합 생성 
#그러나 리스트를 집합 안에 원소로 줄 순 없음 Hash를 사용하기 위해서인데, 리스트는 그 내부의 key가 변경이 가능하기 때문에 불가능.
set((123,123,123)) #; {123} 중복은 한번만 들어옴 

#원소 추가
# add(), update(), copy()
a.add(4)
a.update([5,6,7,8]) # 기존 A U {4,5,6} ; 합집합 생성 
a.update([9,10,11],[-1,-2,-3])
b = a.copy()

#원소 제거
#clear(), discard(), pop(), remove()
a.clear()
a.discard(4) # 하나 제거 
a.discard(4) # 없으면 그냥 지나감
a.remove(5) # 하나 제거
a.remove(5) # 없으면 ! 예외 발생 ! 
a.pop() # 제거하면서 리턴 

#집합 단위 연산
# 진짜 우리가 아는 집합처럼 
a.union(b) # 합집합
a.intersection(b) #교집합
a.difference(b) #차집합
a.symmetric_difference(b) #대칭차집합  

#원소 검사
2 in a
2 not in a
a.issuperset(b)
a.issubset(b)   
a.isdisjoint(b) #공집합임??

#frozenset
f = frozenset([1,2,3,4,5])
f = frozenset(a) 
#연산은 값을 변경하지 않는 연산만 허용, set 객체와 동일하게 동작함 
