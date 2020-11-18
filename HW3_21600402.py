# 21600402 전산전자공학부 안수현
# 파이썬 프로그래밍 HW_3

# 이 코드는 박지현교수님 파이썬 프로그래밍 수업의 세번째 과제로 "자가 진단 보조 프로그램" 입니다!

decoLine = "="*80
# 조건 1
# 이 프로그램에 대한 안내문구 만든다
greetingMessage = """안녕하세요, 체온으로 입장 전 진단을 도와드리는 프로그램입니다. 
    1) 사용자의 연령대
    2) 체온의 측정 부위
    3) 측정된 체온 
                -- 을 통해 측정을 도와드립니다. 
    프로그램은 사용자의 측정 시간과 정상체온 여부를 기록합니다."""
# 조건 1 + 조건 2 
# 이프로그램에 대한 안내문구(사용방법)을 만든다 
# 사용자로부터 제대로 된 입력을 받을 수 있도록 적절한 가이드라인 제시 
infoMessage='''[사용방법]
    콘솔 입력창에 *한꺼번에* 1)연령대, 2)측정부위, 3)체온을 입력받습니다.
    이때 각 구분은 공백(스페이스)가 아닌 ,(콤마)로 구분을 합니다. 
    때문에 유효한 입력은 3개의 값과 그 사이에 콤마가 2개가 존재해야합니다. 
        입력 예시)
            11-65세, 귀, 36.4 '''

# 조건 1
# 프로그램 시작시 간단한 인사와 사용방법을 출력한다. 
print(decoLine)
print(greetingMessage)
print(decoLine)
print(infoMessage)
print(decoLine)


# 조건 3 - b
# 빈 문자열과 공백 처리 
def preprocessing(sourceString):
    slist = sourceString.split(",")
    validList = []
    for idx, element in enumerate(slist):
        print(element)
        if len(element.strip()) != 0:
            validList.append(element.strip())
    return validList


# 조건 3 
# 사용자로부터 받은 입력이 유효한지 검증하는 함수를 정의하라
def validate_input(inputString):
    # 조건 3 - d 
    # 사용자로부터 받은 문장이 ,나누어 3개인지 판단한다.
    inputList = preprocessing(inputString)
    # 사용자로부터 받은 입력이 3개로 나누어지지 않은 경우 validate 함수 종료 
    if len(inputList) != 3:
        return False

    try:
        inputList[2] = float(inputList[2])
    except ValueError as err:
        print("!유효한 숫자의 형식으로 입력해주시지 않으셨습니다!\n [에러 메세지 : {}]".format(err))
        return False
    return True




test = "안녕,dkssud,dkssud"

print(validate_input(test))