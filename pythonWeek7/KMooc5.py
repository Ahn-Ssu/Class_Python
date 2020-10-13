# 연습문제 1,2 Method 활용하기 2번 코드

qq = []
one = []

for i in range(2,17):
    for j in range(1,10):
        print("{:>2} * {:>2} = {:>3} ".format(i,j,i*j))
        one.append(i*j)
       
    print(" ",one)
    temp = one.copy()
    qq.append(temp)
    one.clear()
print(qq)