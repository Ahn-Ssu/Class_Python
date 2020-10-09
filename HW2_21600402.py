# 21600402 전산전자공학부 안수현
# 파이썬 프로그래밍 HW_1 

# 이 코드는 박지현교수님 파이썬 프로그래밍 수업의 두번째 과제로 "롤 플레잉 미션수행 게임 만들기" 입니다!
# 해당 프로그램의 테마는 한국 수험생입니다. 플레이 가능한 캐릭터는 이과수험생, 문과수험생, 예체능입니다. 



playClass = ["이과","문과","예체능"]
stageNumber = 0 
statList = ["지능","감성","체력","매력"]
userStat = [3,1,7,2]
requireStat = [15,10,15]
roundList = ["2월","3월","6월","9월"]
actionList = ["공부","대외활동","운동","여가"]
studyResult = [
    [1,1,-1,0],
    [2,2,-2,0],
    [4,2,-2,0],
    [8,2,-2,0]    
]
activityResult = [
    [1,1,-1,2],
    [1,2,-2,2],
    [1,4,-2,2],
    [1,8,-2,2]
]
exerciseResult =[
    [1,1,2,2],
    [1,1,2,2],
    [1,1,2,2],
    [1,1,2,2]
]
restResult =[
    [1,1,-1,2],
    [1,2,-1,3],
    [1,4,-1,4],
    [1,8,-1,5]
]

confirm =["예","아니오"]
finalConfirm = ""
user = ""

print()
print("***************수험생 키우기***************")
print("[알림] 당신의 수험생의 꿈을 이룰 수 있도록 도와주세요!")
print("       적절한 휴식, 적절한 노력을 통해 당신의 수험생을 이끌어가면 됩니다.")



while 1:
    print("="*100)
    print("[알림] 플레이할 직업을 선택해주세요 >>>>>>>>>> | ", end=" ")
    for indexNumber, userClass in zip (range(1,4),playClass):
        print("{}) {}".format(indexNumber,userClass), end=" | ")
    user = input("\n       입력 (숫자) : ")
    if user in ["1","2","3"]:
        break
    print("!경고! 잘못입력하셨어요, 범위 내의 숫자로 입력해주세요. 입력한 값 = {}".format(user))
user = int(user)-1



print("="*100)
print("[알림] 축하합니다. 당신의 ⋆⁺₊⋆{}⋆⁺₊⋆ 수험생이 생성되었습니다!".format(playClass[user]))
print("      수험생들은 각각 중요한 능력치가 다릅니다. ⋆⁺₊⋆{}⋆⁺₊⋆ 수험생은 {}이 가장 중요합니다.".format(playClass[user],statList[user]))
print("      성공적인 {} 생활의 마무리는 {}이 {} 이상 되어야 합니다.".format(playClass[user],statList[user],requireStat[user]))

while 1:
    print("="*100)
    print("[알림] 현재 수험생 상태 >>>  | ", end="")
    for stat, users in zip (statList,userStat):
        print("{} : {}".format(stat,users), end=" | ")

    print()
    print("="*100)
    print("[알림] {}입니다. 당신의 수험생은 무엇을 할까요?".format(roundList[stageNumber]), end=" | ")


    while 1:
        for indexNumber, act in zip(range(1,5),actionList):
            print("{}) {}".format(indexNumber,act), end=" | ")
        select =  input("\n      입력 (숫자) : ")
        if select in ["1","2","3","4"]:
            break
        print("!경고! 잘못입력하셨어요, 범위 내의 숫자로 입력해주세요. 입력한 값 = {}".format(select))

    select = int(select) - 1
    print("[알림] {0}을 선택하셨습니다. 다음과 같은 능력치를 얻습니다.".format(actionList[select]),end=" | ")
    if select == 0 :
        nowEvent = studyResult
    elif select == 1 :
        nowEvent = activityResult
    elif select == 2 :
        nowEvent = exerciseResult
    elif select == 3 :
        nowEvent = restResult

    for stat, statValue in zip (statList,nowEvent[stageNumber]):
        print("{} {}".format(stat,statValue), end=" | ")
    print("\n       수행하시겠습니까?  ",end="")
    while 1:
        for indexNumber, answer in zip(range(1,3),confirm):
            print("{}) {}.".format(indexNumber,answer),end=" ")
        finalConfirm =  input("\n       입력 (숫자) : ")
        if finalConfirm in ["1","2"]:
            break
        print("!경고! 잘못입력하셨어요, 범위 내의 숫자로 입력해주세요. 입력한 값 = {}".format(finalConfirm))

    if finalConfirm == "1":
        print("="*100)
        print("[알림] 이전 수험생 상태 >>>  | ", end="")
        for stat, users in zip (statList,userStat):
            print("{} : {}".format(stat,users), end=" | ")
        print()
        for indexNumber, stat in zip(range(0,4),nowEvent[stageNumber]):
            userStat[indexNumber] = userStat[indexNumber] + stat
        print("[알림] 현재 수험생 상태 >>>  | ", end="")
        for stat, users in zip (statList,userStat):
            print("{} : {}".format(stat,users), end=" | ")
        print()
        if user == 0 :
            
        elif user == 1:
        elif user == 2: 
        stageNumber = stageNumber + 1
    if stageNumber > 3:
        break





