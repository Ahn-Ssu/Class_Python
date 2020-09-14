# 오프셋이 아닌 키를 사용하여 값을 얻는 자료형 

d1 = {'one':'일', 'two':'이', 'three':'삼'}
d2 = dict(one='하나', two = '둘', three = '셋')

print(d1['one']) # key -> value 추출 

d1['four'] = '넷' 
# 새 항목 삽입, 기존에 항목이 없으면 추가됨
# 기존에 항목이 있으면 값이 변경 됨 
print(d1)

# 딕셔너리 요소 삭제하기 
print(d2)
del d2["one"] # 이렇게 딕셔너리는 Key로 지정해서 key - value 셋을 날려줌 
print(d2)

# 주의사항 
# 딕셔너리에 Key 값으로 list는 안되고 Tuple 가능함 : 이유 Key는 변경하면 Hash를 못찾기 때문에 
print(d1.keys())
print(d1.values())
print(d1.items())

# 집합은 중복되지 않은 데이터를 순서 없이 저장하는 자료형 
s1 = {1,2,3}
s2 = set() # 공집합 

s1.union(s2) # 합집합
s1.intersection(s2) # 교집힙
s1 - s2 # 차집합
s1 | s2 # 합집합
s1 & s2 # 합집합 