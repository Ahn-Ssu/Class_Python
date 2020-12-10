# 객체는 속성(property)과 기능(method)으로 구성 

# 객체를 만들기 위해 클래스(class)라는 도구 제공 

# 인스턴스 - 클래스를 할당 받은 친구 

# Class 변수, 속성, method를 포함한 데이터 형태를 정의 
# Instance : class 의 모든 내용을 사용하도록 상속받은 변수 
# Method : ','으로 시작하는 명령어, 함수랑 유사하나 class 내에서 상속받은 경우만 사용가능

# Class 예제
class Person: # 클래스 정의, 이름 
    name = "Default Name" # 멤버 변수 
    def Print(self): # method 정의 
        print("Hello, my name is", self.name)


p1 = Person() # instance 객체 생성 
p1.Print() # member 변수 값 출력 


# 메소드 
# 정의할때는 인수 self를 적어야 한다. 
# 정의 한 것을 사용할 때는 적지 않아도 됨
# 대소문자 구분합니더!

# 생성자 (Constructor)
# Class를 상속 받자마자 생성자 밑에 있는 내용 
# method __init__()

# 소멸자 (Destructor)
# 상속이 끝났을 때 밑에 있는 내용이 실행
# method __del__()

class MyClass:
    def __init__(self, value):
        self.value = value
        print("Class is created!, Value =", self.value)
    
    def __del__(self):
        print("Class is deleted!")

cla = MyClass(3)


class BankAccount:
    def __init__(self):
        self.balance =0
    
    def withdraw(self, amount):
        self.balance -= amount
        return self.balance
    
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
a = BankAccount()
b = BankAccount()

print(a.deposit(200))
print(b.deposit(400))

print(a.withdraw(10))
print(b.withdraw(200))

class Employee:
    empCount = 0 # 이거 이렇게 하면 static 처럼 생성이 됨 
    TotalSalary = 0
    MeanSalary = 0

    def __init__(self, name,salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
        Employee.TotalSalary += salary
        Employee.MeanSalary = Employee.TotalSalary / Employee.empCount
    
    def displayCount(self):
        print("Total E =", Employee.empCount)
    
    def displayEmployee(self):
        print("N : ", self.anme, " S : ", self.salary)
    
    def displayMeanSalary(self):
        print("MS :",Employee.MeanSalary)