# str method 활용 - 단어 쪼개기 
# 원 문장 
mystr = "내가 사람의 방언과 천사의   말을 할지라도 사랑이 없으면 소리 나는 구리와 울리는 꽹과리가 되고 내가 예언하는 능력이 있어 모든 비밀과 모든 지식을 알고 또 산을 옮길 만한 모든 믿음이 있을지라도 사랑이 없으면 내가 아무 것도 아니요 내가 내게 있는 모든 것으로 구제하고 또 내 몸을 불사르게 내줄지라도 사랑이 없으면 내게 아무 유익이 없느니라 사랑은 오래 참고 사랑은 온유하며 시기하지 아니하며 사랑은 자랑하지 아니하며 교만하지 아니하며 무례히 행하지 아니하며 자기의 유익을 구하지 아니하며 성내지 아니하며 악한 것을 생각하지 아니하며 불의를 기뻐하지 아니하며 진리와 함께 기뻐하고 모든 것을 참으며 모든 것을 믿으며 모든 것을 바라며 모든 것을 견디느니라 사랑은 언제까지나 떨어지지 아니하되 예언도 폐하고 방언도 그치고 지식도 폐하리라"
print("="*50, "원래 문장")
print(mystr)

# 원 문장을 공백을 이용하여 단어 단위로 나눈다
print("="*50, "공백 기준 분해된 단어로 변환한 것")
wList = mystr.split()
print(wList)

# 각 단어가 나타난 횟수를 센다
# 이번에는 part1 과 약간 다르게 단어만 리스트, 횟수만 리스트 이렇게 리스를 2개로 만들고, 아이템들끼리 서로 대응되게 한다. 
uWList = [] # 문장에서 unique한 단어만 리스트
uCList = [] # unique한 단어에 대응하는 횟수 리스트 
for item in wList: # 전체 단어 리스트에서 개별 단어 하나하나를 처음부터 끝까지 본다
    if item in uWList: # 이 단어가 unique 단어 리스트에 있다면 
        uWIndex = uWList.index(item) # 그 단어의 위치를 찾아서 
        uCList[uWIndex] = uCList[uWIndex] +1 # 횟수리스트에 해당 위치 값을 1 증가
    else: # 이 단어가 unique 단어 리스트에 없는 새 단어라면 
        uWList.append(item) # 이 단어를 unique 단어 리스트에 추가
        uCList.append(1) # 대응되는 횟수리스트 값은 1 을 넣어줌 

print("="*50, "unique 단어와 그 등장횟수 1대1 대응")
print(uWList)
print(uCList)

# 가장 적은 횟수, 가장 많은 횟수를 센다
# 이번에는 part1 과 달리 리스트 정렬을 하지 않고, 횟수리스트 값에서 min, max를 찾는다.
minN = 1000 # min 값을 저장할 변수 - 아주 큰 값에서 시작 
maxN = 0 # max 값을 저장할 변수 - 아주 작은 값에서 시작 
for item in uCList: # 횟수리스트의 내용을 처음부터 끝까지 본다.
    if minN >= item: # 횟수가 minN 에 들어있는 내용보다 작으면 
        minN = item # 이게 새로운 min
    if maxN <= item: # 횟수가 maxN 에 들어있는 내용보다 작으면 
        maxN = item # 이게 새로운 max 

# 가장 적게 사용된 단어, 가장 많이 사용된 단어를 찾는다
minWList = []
maxWList = []
for i in range(len(uCList)): 
    if uCList[i] == minN: # 횟수리스트에서 현재 위치 값을 확인하여 min 과 같은 값이면 
        minWList.append(uWList[i]) # 대응되는 단어리스트에서 단어를 가져와서 minList에 추가
    if uCList[i] == maxN: # 횟수리스트에서 현재 위치 값이 max 와 같은 값이라면 
        maxWList.append(uWList[i]) # 대응되는 단어리스트에서 단어를 가져와서 maxList에 추가 

# 분석 결과 출력
print("="*50, "단어 분석 결과")
print("가장 적게 사용된 단어는 ", minN, "회 이며, 다음과 같다")
print(minWList)
print("가장 많이 사용된 단어는 ", maxN, "회 이며, 다음과 같다")
print(maxWList)

# 가장 많이 사용된 단어 1개와 사용자 입력을 교환하여 출력
userInput = input("\n'"+maxWList[0]+"'와 교환하여 출력할 단어를 쓰세요: ")
# 이번에는 두 개를 서로 교환하는 게 아니라 사용자로부터 받은 걸 본문의 가장 많은 단어에 바꿔 넣으면 됨 
rstr = mystr.replace(maxWList[0], userInput)
print("="*50, maxWList[0], "과", userInput, "단어 교환")
print(rstr)
