# import modules 
from tkinter import * 
import random 
import time


# create class Ball
class inst:
    def __init__(self, name):
        self.name = name
        self.state = 10
    
    def play(self):
        # 상태 값이 출력 후에 라고 하셨으니 그 조건 사항대로 코딩했습니다 ㅠㅠ
        if(self.state==0):
            print("{}가 고장나서 연주가 불가능합니다.".format(self.name))
            return

        
        print("{}를 연주합니다.".format(self.name))
        if(self.state>7):
            self.state -= 1
        elif(self.state>3): # 7이하 4이상일떄 출력 후 상태 값이 얼마이고 관리가 필요하다는 말
            self.state -= 1
            print("현재 악기의 연주 후 상태는 {}입니다.".format(self.state))
            print("관리가 필요합니다.")
        elif(self.state>0): # 1~3사이 상태 값이 얼마이고 수리가 필요하다
            self.state -= 1
            print("현재 악기의 연주 후 상태는 {}입니다.".format(self.state))
            print("수리가 필요합니다.")

        
 

        

    def care(self):
        print("악기의 상태를 관리합니다")
        print("관리 전 상태 : {}".format(self.state))
        self.state += 1
        print("관리 후 상태 : {}".format(self.state))
    
    def fix(self, level):
        print("악기 {} 수리합니다".format(self.name))
        self.state += level
        print("수리 후 상태 : {}".format(self.state))
        

piano = inst("Piano")

for i in range(12):
    piano.play()

piano.fix(3)
piano.care()
piano.care()
piano.play()



class stringInst(inst):
    def __init__(self,name,stringNum):
        super().__init__(name)
        self.stringNum = stringNum
    
    def __add__(self, aString):
        return self.stringNum + aString.stringNum
    
    def fix(self, level):
        super().fix(level)
        print("{}의 현 {}개를 모두 교체했습니다.".format(self.name, self.stringNum))


vio = stringInst("바이올린", 4)
cel = stringInst("첼로", 4)
gui = stringInst("기타", 6)

for i in range(13):
    gui.play()

gui.fix(5)

print("첼로와 바이올린의 현의 합은 {} 입니다.".format(cel+vio))