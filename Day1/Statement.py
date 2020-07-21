score = 90 


if score > 90 :
    print('A+')
elif score == 90 :
    print('A')
else :
    print('not A') 

a = 5
x = a *2 if a>5 else a/2 


# for 타깃 in 객채 :
#     state  1
# else :
#     state 2

L = ['cat','dog','bird','pig','spam']
for k, animal in enumerate(L):
    print(k, animal)


# while 조건식:
#     조건 
# else :
#     조건 

# with문
# with 문은 두 개의 관련된 연산들 사이에서 어떤 작업을 수행할 때 유용하다 
# open() - close() / save() restore() 

with open('output.txt', 'w') as f:
    f.write('hello~')

f0 = open('output.text', 'w')
f0.write('hello')
f.close


# try ~ except 문
# 자바의 try catch와 동일 

try :
    n = int (s)
except ValueError:
    n = 0 
    print('invalid string for integer')