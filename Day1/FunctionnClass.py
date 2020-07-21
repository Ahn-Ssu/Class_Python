# 함수
# def 함수이름 (함수매개변수):
#     state 1

def add(a,b):
    return a+b

add(3,4) #7
add([1,2,3], [4,5,6]) #[1,2,3,4,5,6]
# 파이썬은 동적으로 인수를 저달하므로 함수를 선언할 대 인수의 자료형을 지정할 필요 없다. 

def defaultAdd(a=0,b=0):
    return a+b


