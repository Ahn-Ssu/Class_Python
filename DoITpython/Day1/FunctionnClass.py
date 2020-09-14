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


#클래스 변수를 멤버, 함수를 메소드라고 함  메소드는 클래스에 있는 것만 말하는 듯
class A:
    scale = 10
    def area(self, width, height):
        return self.scale * width * height 
    def seta(self, a):
        self.a =a
    def geta(self):
        return self.a

a = A() # 객체생성
a.area(2,3)
a.seta(5)
a.geta()
