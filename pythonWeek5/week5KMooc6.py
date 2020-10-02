start = int(input("2단부터 몇단까지 출력할까요? (숫자 입력) : "))


for i in range(2,start+1):
    for j in range(1,10):
        print(i,"X",j,"=",i*j)
    print("--------")