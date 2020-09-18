myName = input("당신의 이름을 입력하세요; ")
myBelong = input("당신의 소속기관을 입력하세요; ")
myBirhyear = int(input("당신의 출생년도를 입력하세요; "))


print()
print("당신의 이름은 {}".format(myName))
print("{}에 소속되어 있으시군요".format(myBelong))
print("당신의 나이는 {}세 맞죠?".format(2020-myBirhyear+1))
