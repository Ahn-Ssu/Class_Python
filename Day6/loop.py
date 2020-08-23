x = 1 

while 0:
    print(x,"ctrl + c  -----> escape")
    x += 1


for i in range(2, 10):
    for j in range(1, 10):
        print("%2d"%(i*j), end=" | ")
    print(' ')

# 리스트 내포
# [표현식 for 항목 in 반복 가능 객체 if 조건]
a = [1,2,3,4]

result = [ num * 3 for num in a]
print( result)

result = [ num * 3 for num in a if num % 2 == 0 ]

# 2중 내포
# [표현식 for 항목 in 반복 가능 객체 if 조건
    #  for 항목 2 in 반복 가능 객체 if 조건]
result = [ "%2d"%(x*y) for x in range (2,10)
        for y in range (1,10)]
print(result)