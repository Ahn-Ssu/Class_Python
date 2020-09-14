#-*-coding: utf-8-*-
import keyword
print(keyword.kwlist)

횟수 = 1 
while 횟수 < 10 :
    print(횟수)
    횟수 += 1 

def 더하기(a,b):
    return a+b

print(더하기(2,3)) #메소드가 먼저 선언 되어야 함 
print(type(횟수))

#연속 치환 가능
a,b,c,d,f  = 4,3,2,1,0
# swap 
a,f=f,a
print(a)
print(f)

print(1,2, end= 'kk\n')
print(1,2, sep= ', ')

s= 'hello python!'

s[-1] # ! 
s[-2] # n

s[1:3] # el
s[1:] # 처음부터 끝까지
s[:3] # 처음부터 3 전까지
s[:] 

# start:stop:step
s[::2] # 2칸 단위로
s[::-1] # 거꾸로

print(len(s))

a = 500
b = 500
print(id(a))
print(id(b))