# 연습문제 3

str = input("문자열 입력")

uppercount = 0
lowercount = 0
etccount = 0

swapstr = str.swapcase()
print("대소문자를 바꾼 결과 = ", swapstr)

for ch in swapstr :
    if ch.isupper():
        uppercount += 1 
    elif ch.islower():
        lowercount += 1
    else:
        etccount += 1 

print("대문자 갯수는 ", uppercount)
print("소문자 갯수는 ", lowercount)
print("대소문자 아닌 문자 갯수는 ", etccount)
