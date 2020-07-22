# 시퀀스 자료형이면서 변경 가능한 자료형 
# 파이썬 특성과 결합하여 데이터의 크기를 동적으로 관리 가능 

#리스트 값 일부 삭제 예시 
# del a[0] 로 인덱스 단위로 접근해도 상관 없음 
a = [1, 12, 123, 1234]
a[0:2] = []
print(a)  #[123, 1234]

#리스트 값 추가 예시
b = [123, 1234]
b[1:1] = ['spam', 'ham']
print(b) #[123, 'spam', 'ham', 1234]

# 중첩 리스트
# java의 2중 배열 구조처럼 주소 참조만 함, 규격 자율 
t = [22, a, b, 33]
print(t) # [22, [123, 1234], [123, 'spam', 'ham', 1234], 33]

#리스트 -> 스택으로 사용 
myStack = [10,20,30,40,50]
myStack.append(60) # push of stack 
myStack.pop()  # pop, return top element  
myStack.pop(2) # 인덱스 지정 가능 

#리스트 -> 큐로 사용 
myQueue = [9,8,7,6,5]
myQueue.append(60)
myQueue.pop(0) # queue 의 pop 연산, 인덱스 지정으로 기능을 수행하게 끔 해줌 