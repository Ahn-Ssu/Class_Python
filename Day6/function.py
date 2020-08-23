#입력 값의 갯수를 예측할 수없을 때
def sum_up(*args):
    result = 0
    for i in args:
        result = result + i
    
    return result 


values = [2,3,4,5,6,7,8]
print(sum_up(values[0],values[4],values[2]))

# 매개변수 초기값 설정하기
# 초기 값을 설정한 매개변수는 뒤에서부터 순서대로 앞으로 채워져야함 
def introduce(name, old, man = Ture):
    print("이름 %s" % name)
    print("나이 %s" %old)
    if man:
        print("남자임")
    else :
        print("여자임")
    

