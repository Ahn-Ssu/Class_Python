class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y
    
    def perimeter(self):
        return 2 * self.x + 2 * self.y

    def describe(self, text):
        self.description = text
    
    def authorName(self, text):
        self.author = text

    def scaleSize(self, scale):
        self.x = self.x * scale
        self.y = self.y * scale

rectangle = Shape(100,45)
print(rectangle.area())
# 단일 상속은 뭐 무난,,, 

# 연산자 중복 정의
# 사용자가 정의하는 객체 내에서 필요한 연산자를 정의할때
# 기존에 사용하는 내장형 연산자의 데이터 타입과 형태와 동작이 유사하도록 재정의
# 연산자 중복 선언은 벡터, 행렬 등 수치연산에서 자주 사용 

class GString:
    def __init__(self, init=None):
        self.content = init

    def __sub__(self, str):
        for i in str:
            self.content = self.content.replace(i, ' ')
        return GString(self.content)

    def __abs__(self):
        return GString(self.content.upper())
    
    def __mul__(self, int):
        return GString(self.content *int)
    def Print(self):
        print(self.content)

g = GString("ABcdefg")
g.Print()
g = g - "df"
g.Print()
g = abs(g)
g.Print()
g= g*3
g.Print()

# 상속
# class가 여러 개 정의 되었을때, 부모클래스가 자식클래로 부모클래스의 모든 속성을 물려주는 것

class Person:
    def speak(self):
        print("I can speajk")

class Man(Person):
    def wear(self):
        print("I wear pants")

class Woman(Person):
    def wear(self):
        print("I wear skirt")

man = Man()
man.speak()