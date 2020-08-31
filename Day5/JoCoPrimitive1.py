#-*-coding: utf-8-*-
# 자료형 
# 숫자, 문자열, 불 / 자료에 대한 타입
# 변수, 리스트, 튜플, 딕셔너리, 집합 / 어떤 값을 담는 자료구조

#변수 -> 어떠한 값을 담는 '상자' 
a = 1 # int
f = 1.0 #float 


print(3/4)   # 실제 계산 처럼 값이 정확하게 나옴 
print(4//3)  # 자바에서 하는 것처럼 '몫'만 나옴
print(4%3)   # 자바에서 하는 것처럼 '나머지'만 나옴
print(4**3)  # 제곱 

#문자열 포맷
number = 10
day = "three"
strEx = "I ate %d apples, so I was sick for %s days." % (number, day)
print(strEx)
# 자바 동일 %d 정수, %f 실수, %s 문자열
# 근데 %s로 쓰면 알아서 다 문자열로 바뀌어서 들어감 ( 자동 캐스팅 )
# +) 포매팅 연산자 %d와 %를 같이 사용할 때는 % -> %% 로 사용한다
strFormatEx = "Erro is %d%%." % 98
print(strFormatEx)

strEx2 = "who are you? {}".format("??")
strEx3 = "I am {name}, I'm {age}".format(age="sixteen",name="수현")

dayCount = day.count("r")
print(dayCount)
print(day.find("a")) # none : -1 return 