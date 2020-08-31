# 콘솔로부터 입력 받기 -> input()
# input( " 질문 내용 " )
# a = input()
inputNumber = input("숫자를 입력해라 애송이 : ")
print("애송이가 입력한 숫자는 : ", inputNumber)


# 파일 열고 닫기
# with 키워드를 사용한 자동 닫기 
with open("foo.txt", "w") as f:
    f.write("Life is too short, you need python")
    f.write("and I need U")
