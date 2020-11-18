# 21600402 전산전자공학부 안수현
# 파이썬 프로그래밍 HW_3

# 이 코드는 박지현교수님 파이썬 프로그래밍 수업의 세번째 과제로 "자가 진단 보조 프로그램" 입니다!


import datetime
import random

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

# 조건 6 - a 
# 연령과 측정부위에 따른 체온의 범위가 저장되어있는 딕셔너리이다. 
TemperatureTable = {
    "0-2세":{'귀': (36.4, 38), '항문': (36.8, 38), '겨드랑이':(34.7,37.3)},
    "3-10세":{'구강':(35.5, 37.5),'귀': (36.1, 37.8), '항문': (36.6, 38), '겨드랑이':(35.9,36.7)},
    "11-65세":{'구강':(36.4, 37.6),'귀': (35.9, 37.6), '항문': (36.6, 38), '겨드랑이':(35.2,36.9)},
    "65세이상":{'구강':(35.8, 36.9),'귀': (35.8, 37.5), '항문': (37.0, 38.1), '겨드랑이':(35.6,36.3)},
}

# TemperatureTable 사용 전, 사용자에게 어떠한 입력값이 있는지 보여주기 위한 라벨들 
ageLabel = ['0-2세','3-10세','11-65세','65세이상']
areaLabel = ['구강','귀','항문','겨드랑이']
processedInput =[]

# 조건 1
# 프로그램 시작시 간단한 인사와 사용방법을 출력한다. 
print(decoLine)
print(greetingMessage)
print(decoLine)
print(infoMessage)
print(decoLine)


# 조건 3 - b
# 빈 문자열과 공백 처리 하는 함수
def preprocessing(source):

    # 사용자에게 직접 입력을 받는 경우는 string으로 입력이 오고 
    # validation을 할때는 list로 입력이 오기 때문에 isinstance으로 수행을 나눔 
    if isinstance(source,str):
        # 조건 2 
        # 콤마(,) 단위로 유닛을 구분함 
        slist = source.split(",")
        validList = []
        for idx, element in enumerate(slist):
            # 조건 3 -  c
            # 빈 문자열이나 공백 등은 처리함 
            if len(element.strip()) != 0:
                validList.append(element.strip())
        return validList
    else:
        return source


# 조건 3 
# 사용자로부터 받은 입력이 유효한지 검증하는 함수를 정의하라
# checkType이 사용자에게 입력을 받을 때는 1이 오게하여 메세지가 출력되게하고
#  자체 validation을 수행할 땐 0을 전달하여 메세지가 출력되지 않게 한다
def validate_input(inputString, checkType):
    # 조건 3 - d 
    # 사용자로부터 받은 문장이 ,나누어 3개인지 판단한다.
    inputList = preprocessing(inputString)
    # 사용자로부터 받은 입력이 3개로 나누어지지 않은 경우 validate 함수 종료 
    if len(inputList) != 3 and checkType:
        print("','로 구분하여 3개의 입력을 하지 않았습니다!")
        return False,inputList.copy()

    # 조건 3 - b
    # float으로 변환 예외처리로 검증 

    try:
        inputList[2] = float(inputList[2])
    except ValueError as err:
        # 조건 3 - e 
        # 유효한 숫자가 입력되지 않았음을 출력해줌, type casting error
        print("!유효한 숫자의 형식으로 입력해주시지 않으셨습니다!\n [에러 메세지 : {}]".format(err))
        return False,inputList.copy()

    # 조건 3 - b
    # 변환된 값 또한 양의 숫자이여야 한다. 
    if inputList[2] <= 0 and checkType:
        # 조건 3 - e 
        # 0, 혹은 음수가 체온의 값으로 들어왔음을 나타냄
        print("!!0, 혹은 음수 값을 입력했습니다!!")
        return False,inputList.copy()

    # 조건 3 - a
    # 첫번째 입력 값, 연령대의 선택이 정상적으로 이루어져야한다.
    if not (inputList[0] in ageLabel) and checkType:
        # 조건 3 - e 
        # 연령대에 맞게 입력이 되지 않음
        print("유효한 연령대로 입력하지 않았습니다")
        print("입력 종류 :",ageLabel)
        return False,inputList.copy()
    
    # 조건 3 - a
    # 두번째 입력 값, 측정부위의 입력이 정상적으로 이루어져야한다.
    if not (inputList[1] in areaLabel) and checkType:
        # 조건 3 - e 
        # 측정부위에 해당하는 입력이 들어오지 않음 
        print("유효한 측정부위를 입력하지 않았습니다")
        print("입력 종류 :",areaLabel)
        return False,inputList.copy()
    
    if inputList[0] == '0-2세' and inputList[1] == '구강':
        print("0-2세는 구강 체온 측정 결과를 지원하지 않습니다.")
        print("다른 측정부위를 사용하여주세요")
        return False,inputList.copy()

    # 조건 3 - e 
    # 정상 입력인 경우에 Ture return 
    return True,inputList.copy()


# 조건 3 
userInput = input("콤마(,)로 구분하여 순서대로 연령대, 측정부위, 체온을 입력해주세요\n입력 : ")

# 조건 4 + 조건 5 
# 3번 조건을 위한 validate_input 함수를 사용하여 유효한 입력인지를 검증한다
# 4번 조건은, validate_input에서 true 값(정상입력 판정)이 나올때 까지 whlie을 통해 계속해서 반복한다. 
while not validate_input(userInput,1):
    print("연령대 보기", ageLabel)
    print("측정부위 보기",areaLabel)
    userInput =input("콤마(,)로 구분하여 순서대로 연령대, 측정부위, 체온을 입력해주세요\n입력 : ")
    
# 조건 4 
# 유효한 입력이 들어왔는지 확인을 한다. 
_, processedInput = validate_input(userInput,1)


# 조건 6
def checkHeat(soruceInfo):
    # 전달된 정보에 따라서 TemperatureTable 을 이용하여 각 카테고리에 맞게 체온 범위를 설정 
    theScopes = TemperatureTable.get(soruceInfo[0])
    theScope = theScopes.get(soruceInfo[1])

    diagnosis = ""
    # diagnosis 변수와 함께 scope의 범위보다 큰 경우에는 열이 있다고 진단한다.
    if soruceInfo[2] > max(theScope):
        diagnosis = "열이 있습니다."
     # scope의 범위 내에 있는 경우에는 정상체온이라고 진단한다.
    elif soruceInfo[2] > min(theScope):
        diagnosis = "정상체온 입니다."
    # scope의 범위 보다 작은 경우에는 저체온 혹은 측정 오류라고 진단한다.
    else :
        diagnosis = "저체온, 혹은 측정오류입니다."
    
    soruceInfo.append(diagnosis)
    return soruceInfo
    

# 조건 7 
# 발열 체크 함수를 이용하여 체온의 범위를 측정하고, 결과 메세지를 측정한 시각과 함께 출력 
result = checkHeat(processedInput)
print(datetime.datetime.now(), result[3])



#################################################################
################## self validation ##############################
#################################################################

# 조건 8 , 8 - a
# 랜덤하게 샘플 값을 만드는 함수
# 전달 받는 파라미터 없음 
def make_sample():
    # 조건 8 - b 
    # 리턴을 하기 위한 리스트 
    aSample = []


    # 조건 8 - b
    # 랜덤으로 선택되는 연령별 변수, 측정부위 
    aSample.append(random.choice(list(TemperatureTable.keys())))
    aSample.append(random.choice(list(TemperatureTable.get(aSample[0]).keys())))

    # 조건 8 - c 
    # 체온 랜덤, 오류 값을 넣기 위한 라인 
    # (-3,-2,-1) 30%
    # (0,1,2,3,4,5,6) 30% 
    sign = random.randrange(-3,7)
    # sing의 값이 음수이면 -1, 아닌 경우는 1로 두어 음수 노이즈를 추가함 
    if sign < 0 : 
        sign = -1 
    else:
        sign = 1 

    # 조건 8 - c
    # 체온 값 랜덤 생성 범위 |0-40|
    aSample.append(round(random.random()*40*sign,1))

    # 조건 8 - b 
    # 리턴 값은 랜덤하게 선택된 리스트
    return aSample

# 조건 9 , 9-a
# 10개의 자체 성능평가 모든 결과를 저장하기위한 리스트, key로 사용될 리스트.
totalLog = []
keyLabel = ["연령별","측정부위","체온","정상여부","측정일시"]

# 조건 9
# 무작위 샘플을 10개 만들고, 3번 함수로 입력값(샘플값)을 검증한 후, 발열 체크 함수를 수행한다. 
for i in range(10):

    # 무작위 샘플 생성
    sample = make_sample()

    # 생성된 샘플 유효값 검증
    # valid가 True 일때만 유효값이 입력된 것이다. 
    # validation 함수에서, 오류메세지는 필요 없기 때문에 두번째 인자로 0을 건네 메시지 출력을 비활성화시킴
    valid, result = validate_input(sample,0)
    # 조건 9 - b 
    # valid가 True 일때만 발열 체크를 수행한다. 
    if valid :
        result = checkHeat(result)
    # 그 외에는 정상여부에 대해서 오류값임을 설정한다. 
    # 발열체크 함수도 사용하지 않는다. 
    else :
        result.append("측정오류")
    
    # 조건 9 - a
    # 확인한 날짜를 포함시키는 코드 
    result.append(str(datetime.datetime.now()))

    sampleLog = {}
    # 조건 9 - a 
    # 하나의 샘플에 대한 결과를 딕셔너리 형식으로 저장하며
    # keyLabel과 result를 같이 저장한다. 
    for key,value in zip(keyLabel,result):
        sampleLog[key] = value
    
    # 조건 9 - c 
    # 총 10회 반복되며, 각 결과를 하나의 리스트 변수에 저장을 한다. 
    totalLog.append(sampleLog)

# 조건 10 
# 9 번 결과 출력  
print("\n")
print("*** Validation Result ***")
print()
print(totalLog)
print()