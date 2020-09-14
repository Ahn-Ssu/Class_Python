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

#리스트 정렬, 정렬 기준자 전달 
L = [123, 34, 56, 2345]
L.sort() # 문자열 정렬됨
L.sort(key = str) # 숫자 기준 정렬ㄹ 됨  

def myKey(a):
    return a%3 

L.sort(key = myKey)

#리스트 전달, 저장된 객체의 순서를 건드리지 않는 sorted()
#리스트 뿐만 아니라 사전에도 사용 가능  
newList = sorted(L)
newList1 = sorted(L, key = int)
for element in sorted(L):
    print(element, end = ' ')

#리스트 내장, 알아서 만드는 거임 
LI = [k*k for k in range(10)] # [] 를 사용하면 리스트를 만들고 내부룰 수행함 
print(LI)
#리스트 내장 -> 발생자 내장, 호출할때마다 생성해서 넘겨줌 메모리 절약
LG = (k*k for k in range(10)) # () 를 사용하면 리스트를 만들지 않고 내부를 구성 
sum(k*k for k in range(10))
sum([x*x for x in range(10)])

#range () 함수 
# for문과 같이 사용하는데, list를 줌 
# 리스트를 생성하지 않고 반복자를 통해 필요할 떄 동작하여 작동  
range(10) # (0, 10)
range(10,20) # (10, 20) 1간격
range(15,25,2) # (15, 25) 2씩 증가
range(25,15,-1) # 1씩 변화를 줌 
# 우리가 자바나 c에서 for문 사용하던 것처럼 (초기, 끝, 반복) 처럼 사용하면 될듯 

#range() 함수는 발생자로 작동하기때문에 list나 tuple처럼 수행하려면 형 변환을 요구하면 된다 
list(range(10))
tuple(range(123))
# 순차적 할당 가능 
A,B,C,D,F = range(4,-1,-1) 
print(A)
print(F)
print(dir()) # 현재 사용가능한(선언된) 변수나 메소드 라인 업 
print(dir(sys)) # import 후 그쪽에서 무엇을 사용할 수 있는지도 체크 가능 