# 21600402 전산전자공학부 안수현
# 파이썬 프로그래밍 HW_1

# 이 코드는 박지현교수님 파이썬 프로그래밍 수업의 두번째 과제로 "롤 플레잉 미션수행 게임 만들기" 입니다!
# 해당 프로그램의 테마는 한국 수험생입니다. 플레이 가능한 캐릭터는 이과수험생, 문과수험생, 예체능입니다.

# 조건 2) 게임 캐릭터 3가지를 저장한 playClass 리스트이다.
#         user 변수는 사용자가 선택한 class의 index 값을 저장할 변수이다.
playClass = ["이과", "문과", "예체능"]
user = ""

# 게임을 수행할 때 필요한 점수이다. 점수의 종류는 4종류로 각 요소들은 statList에 저장이 되어있다.
# userStat는 기본으로 설정되어 있는 유저의 점수이다. 
# requireStat는 게임을 할때 미션의 성공 여부를 판가름 짓기 위한 기준이 저장되어 있다.
statList = ["지능", "감성", "체력", "매력"]
userStat = [3, 1, 7, 2]
requireStat = [16, 14, 15]

# 조건 4) 본게임은 roundList에 저장되어 있는 각 stage의 이름으로 4단계가 구성되어있다.
#        actionList를 통해서 각 이벤트에서 선택할 수 있는 조건을 다양하게 제공한다.
# 조건 4-b) confirm을 통해 선택한 이벤트의 최종 수행여부를 묻기 위한 리스트이다.
#           finalConfirm은 예/아니오 를 받기 위한 변수이다. 
roundList = ["2월", "3월", "6월", "9월"]
actionList = ["공부", "대외활동", "운동", "여가"]
confirm = ["예", "아니오"]
finalConfirm = ""

# 조건 4) stageNumber 변수는 4번의 이벤트를 제공하기 위한 통제변수이다. 
stageNumber = 0

# 각 result array는 단계별로 값이 변하는 score를 포함하고 있으며, 선택에 따라 각각 다른 점수를 제공한다. 
studyResult = [
    [1, 1, -1, 0],
    [2, 2, -2, 0],
    [4, 2, -2, 0],
    [8, 2, -2, 0]
]
activityResult = [
    [1, 1, -1, 2],
    [1, 2, -2, 2],
    [1, 4, -2, 2],
    [1, 8, -2, 2]
]
exerciseResult = [
    [1, 1, 2, 2],
    [1, 1, 2, 2],
    [1, 1, 2, 2],
    [1, 1, 2, 2]
]
restResult = [
    [1, 1, -1, 2],
    [1, 2, -1, 3],
    [1, 4, -1, 4],
    [1, 8, -1, 5]
]

# 조건 1) 게임 소개글 출력 
print()
print("***************수험생 키우기***************")
print("[알림] 당신의 수험생의 꿈을 이룰 수 있도록 도와주세요!")
print("       적절한 휴식, 적절한 노력을 통해 당신의 수험생을 이끌어가면 됩니다.")

# 조건 2) 게임 캐릭터 선택 코드
# 조건 2-b) 범위 안의 정상적인 입력을 받기 위한 무한 반복문 
while 1:
    print("="*100)
    print("[알림] 플레이할 직업을 선택해주세요 >>>>>>>>>> | ", end=" ")
    # 조건 2-a) 캐릭터는 번호로 고를 수 있도록 번호와 함께 콘솔에 제공된다 
    for indexNumber, userClass in zip(range(1, 4), playClass):
        print("{}) {}".format(indexNumber, userClass), end=" | ")
    # 숫자로 입력받기 위한 표시 
    user = input("\n       입력 (숫자) : ")
    # 조건 2-b) 조건검사: 1,2,3 중에 입력된 값이 없으면 잘못된 입력임을 나타내고 무한루프내의 코드를 다시 수행한다.
    # 유저가 1,2,3 을 입력한 경우 무한 loop를 탈출
    if user in ["1", "2", "3"]:
        break
    print("!경고! 잘못입력하셨어요, 범위 내의 숫자로 입력해주세요. 입력한 값 = {}".format(user))

# 조건 2-b) 정상적인 입력을 받은 후 정보를 사용하기 위한 int convert 
user = int(user)-1


print("="*100)
# 조건 3) 본 게임을 시작하는 안내 메세지를 출력
# 조건 2-c) 제대로 선택한 경우, 어떤 캐릭터를 선택했는지 출력
#           게임을 플레이할 때 어떤 조건 이상이 충족되어야 게임을 끝낼 수 있는지에 대한 가이드도 제공한다.
print("[알림] 축하합니다. 당신의 ⋆⁺₊⋆{}⋆⁺₊⋆ 수험생이 생성되었습니다!".format(playClass[user]))
print("       수험생들은 각각 중요한 능력치가 다릅니다. ⋆⁺₊⋆{}⋆⁺₊⋆ 수험생은 {}이 가장 중요합니다.".format(playClass[user], statList[user]))
print("       성공적인 {} 생활의 마무리는 {}이 {} 이상 되어야 합니다.".format(playClass[user], statList[user], requireStat[user]))
print("       각 시기마다 있는 이벤트를 통해서 당신의 수험생을 키워주세요!")


# 조건 4) 본 게임은 4개의 이벤트로 구성되어 있다.
#        이벤트를 4번 반복하기 위해서 반복횟수를 기록하는 변수 하나와 무한루프문으로 코드를 구성하였고, 4회를 수행한 뒤에는 무한 루프를 탈출한다.
while 1:
    print("="*100)
    # 조건 4-d) 사용자에게 현재 점수가 무엇인지 제공하여 목표와 거리가 얼마인지 알 수 있게 한다.
    #          각각 상태(점수)가 있으며 각 직업마다 미션 성공을 위한 상태의 요구 값이 다르다. 
    #          상태는 statList에 저장되어 있으며 각각 지능, 감성, 체력, 매력이다. 
    print("[알림] 현재 {} 수험생 상태 >>>  | ".format(playClass[user]), end="")
    for stat, users in zip(statList, userStat):
        print("{} : {}".format(stat, users), end=" | ")
    print()
    # 남은 이벤트가 얼마나 있는지 표시를 해준다. 모두 총 4라운드이다. 
    # 각 라운드 별로 stageNumber의 값이 증가하여 출력되는 갯수가 감소한다.
    print("       남은 기간 {}".format(roundList[stageNumber:]))

    # 조건 4-e) 3,4 라운드일때 해당 클래스의 점수가 기준치 이하이면 경고메세지를 제공한다.
    if (stageNumber>1 and userStat[user]<8) or (stageNumber>2 and userStat[user]<13)  :
        print("[알림] !주의! 성공적인 {} 생활의 마무리는 {}이 {} 이상 되어야 합니다.".format(playClass[user], statList[user], requireStat[user]))
    
    print("="*100)
    # 조건 4-a) 해당 스테이지가 몇번째 스테이지 인지 표기를 해주고, 해당 캐릭터의 이름을 출력한다.
    print("[알림] {}입니다. 당신의 {} 수험생은 무엇을 할까요?".format(
        roundList[stageNumber], playClass[user]), end=" | ")

    # 조건 4-b-2) 잘못된 입력이거나 번호가 범위를 벗어나면 어떤 입력을 했는지 보여주고, 다시 출력하게 한다.
    #            해당 조건을 수행하기 위한 무한 반복문이다. 이벤트를 선택하는 1,2,3,4 이외의 입력을 하면 계속해서 반복한다.
    while 1:
        # 조건 4-a) 현재 이벤트들을 출력하는 코드이다.
        #          이벤트들은 actionList에 저장되어 있으며 그 요소들은 각각 공부, 대외활동, 운동, 여가이다. 
        # 조건 4-b-1) 옵션은 번호로 고를 수 있도록 이름 앞에 번호를 붙여서 보여준다.
        #             zip과 range 함수를 사용하여 for문에서 번호와 함게 출력하는 코드이다.
        for indexNumber, act in zip(range(1, 5), actionList):
            print("{}) {}".format(indexNumber, act), end=" | ")
        
        # 입력값은 숫자로 입력해야하기 때문에 입력받을 때 숫자로 입력하라고 안내한다.
        select = input("\n       입력 (숫자) : ")

        # 조건 4-b-1) 정상적으로 입력한 경우에 무한 반복문을 탈출한다.
        if select in ["1", "2", "3", "4"]:
            break
        # 조건 4-b-2) while 문을 탈출하지 못하면 잘못 입력한 것이기 때문에 에러메세지 출력 
        print("!경고! 잘못입력하셨어요, 범위 내의 숫자로 입력해주세요. 입력한 값 = {}".format(select))

    # 입력받은 값을 리스트에 활용하기 위해서 캐스팅할 때 값을 -1 시킴 
    select = int(select) - 1

    # 조건 4-b) 현재 이벤트에서 선택가능한 옵션을 보여주고 고르라고 한다. 옵션은 2개 
    #           무엇을 선택했는지 표시를 먼저 수행한다.
    print("[알림] {0}을 선택하셨습니다. 다음과 같은 능력치를 얻습니다.".format(actionList[select]), end=" | ")

    # 입력받은 값에 따라서 현재 수행될 이벤트를 설정한다. 각각 공부, 대외활동, 운동, 여가이며 nowEvent는 선택된 이벤트로 설정이 된다. 
    if select == 0:
        nowEvent = studyResult
    elif select == 1:
        nowEvent = activityResult
    elif select == 2:
        nowEvent = exerciseResult
    elif select == 3:
        nowEvent = restResult

    # 조건 4-b) 이벤트를 수행할 것인지 말것인지를 2가지 선택지로 제공한다
    #           해당이벤트를 수행하게되면 어떠한 점수를 얻는지 표기를 한다. 
    for stat, statValue in zip(statList, nowEvent[stageNumber]):
        print("{} {}".format(stat, statValue), end=" | ")
    
    # 조건 4-b) 수행할 것인지의 여부를 물어본다 (양자택일)
    print("\n       수행하시겠습니까?  ", end="")

    # 조건 4-b-2) 잘못된 입력을 하는 경우 제대로 된 입력을 받기 위한 강제를 걸기 위한 whlie 반복문이다.
    #            예/아니오의 1,2를 입력하지 않으면 계속해서 반복한다.
    while 1:
        # confirm이라는 list에 저장된 예/아니오를 번호를 붙여서 출력하는 코드 
        for indexNumber, answer in zip(range(1, 3), confirm):
            print("{}) {}.".format(indexNumber, answer), end=" ")
        
        # finalConfimr을 통해서 이벤트 수행의 최종 의사를 결정받는다. 
        finalConfirm = input("\n       입력 (숫자) : ")

        # 조건 4-b-2) 정상적으로 입력이 이루어지는 경우 해당 while 반복문을 탈출한다. 
        if finalConfirm in ["1", "2"]:
            break
        print("!경고! 잘못입력하셨어요, 범위 내의 숫자로 입력해주세요. 입력한 값 = {}".format(finalConfirm))

    # finalConfirm을 '예'로 선택한 경우 해당 이벤트의 점수를 현재 유저의 score에 더하여 저장을 한다.
    # 조건 4-c) 이때 4가지 이벤트 중 각각의 class가 보너스 점수를 얻을 수 있는 이벤트가 다르고 특정 수행을 한 경우 보너스 점수를 얻게 됨을 표시한다.
    #           또한, stage 별로 이벤트의 점수가 다르다. 
    # finalConfirm이 '아니오'인 경우 점수 합산을 수행하지 않으며 stageNumber 또한 증가하지 않아 해당 이벤트가 무효가 되고 맨 처음으로 돌아가 다시 반복을 한다. 
    if finalConfirm == "1":
        print("="*100)
        # 이전 수험생 상태(스코어)를 출력하여 변화를 용이하게 알아 볼 수 있도록 하였다.
        print("[알림] 이전 수험생 상태 >>>  | ", end="")
        for stat, users in zip(statList, userStat):
            print("{} : {}".format(stat, users), end=" | ")
        print()

        # 해당 스테이지의 각 스코어를 현재 수험생 상태:유저의 스코어에 더한다. 
        for indexNumber, stat in zip(range(0, 4), nowEvent[stageNumber]):
            userStat[indexNumber] = userStat[indexNumber] + stat

        # 합산되고난 수험생 상태(스코어)를 제공하여 변화된 값을 바로 확인할 수 있게 한다. 
        print("[알림] 현재 수험생 상태 >>>  | ", end="")
        for stat, users in zip(statList, userStat):
            print("{} : {}".format(stat, users), end=" | ")
        print()

        # 조건 4-c) 캐릭터 별로 선택한 옵션에 대해 다른 점수를 부여한다. 
        #           공부와, 대외활동은 문과와 이과의 주 스코어를 증가시킨다.
        #           운동과 여가는 예체능의 주 스코어를 증가시킨다. 
        if user == 0 and (select == 0 or select == 1):
            print("       이과 직업 보너스로 <지능>이 +1 증가합니다")
            userStat[0] = userStat[0]+1
        elif user == 1 and (select == 0 or select == 1):
            print("       문과 직업 보너스로 <감성>이 +1 증가합니다")
            userStat[1] = userStat[1]+1
        elif user == 2 and (select == 2 or select == 3):
            print("       예체능 직업 보너스 <체력>이 +1 증가합니다")
            userStat[2] = userStat[2]+1
        
        # 이벤트를 최종 수행하는데에 '예"를 선택한 경우 다음 스테이지로 넘어가기 위하여 통제 변수를 1 증가 시킨다. 
        stageNumber = stageNumber + 1
    
    #  모든 이벤트 (4개)가 수행된 경우 break를 통해서 이벤트 수행 반복문을 탈출한다. 
    if stageNumber > 3:
        break

print("="*100)
# 유저에게 최종 스코어를 알아볼 수 있게 제공한다. 
print("[알림] 최종 수험생 상태 >>>  | ", end="")
for stat, users in zip(statList, userStat):
    print("{} : {}".format(stat, users), end=" | ")
print()

# 조건 5) 모든 이벤트가 끝나면 점수를 평가하여 미션에 성공했는지 실패했는지 출력한다. 
if requireStat[user]<=userStat[user] :
    print("축하합니다 당신의 ⋆⁺₊⋆{}⋆⁺₊⋆수험생은 {}이 {} 이상 되어 수험생활을 성공적으로 마쳤습니다".format(playClass[user], statList[user], requireStat[user]))
else:
    print("ㅠㅠ 당신의 {}수험생은 {}이 {} 이상이 되지 못해 이번 수험생활을 아쉽게 마쳤습니다".format(playClass[user], statList[user], requireStat[user]))

# 조건 5) 엔터 입력을 통해 프로그램을 종료한다.
input("\n\n                       종료를 위해 엔터를 입력해주세요.\n")