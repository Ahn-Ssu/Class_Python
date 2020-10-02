numofnum = 0
count = 1
sum = 0


while numofnum<=0:
    numofnum = int(input("정수를 몇개 입력 받을까요?"))

while count<=numofnum:
    num = float(input("숫자를 입력하세요 : "))
    count = count + 1
    sum = sum + num 


print("입력받은 수의 평균은 = ", sum/numofnum)