# 함수나 변수 또는 클래스를 모아 놓은 파일

# import 불러올 모듈 이름 
import mod1 as m1 
print(m1.add(3,4))

# form 모듈 이름 import 모듈 함수
from mod1 import sub
from mod1 import *      # 걍 다가져옴 ㅋㅋ 

print(sub(4,3))

if __name__ == "__main__":
    print("메인스레드는 modul.py 에 할당 되어 있당께롱")
    print(m1.add(3,4))
    print(sub(4,3))
