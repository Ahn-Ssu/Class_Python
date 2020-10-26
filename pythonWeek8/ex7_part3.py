# list method 활용 - 삼행시
print("="*50, "삼행시")

# 삼행시를 반복적으로 입력 받는다 - 리스트 아이템을 만들기 위한 것 
allSamList = [] # 여러 개의 삼행시를 모두 모아놓을 변수 
samCount = 0 # 몇 번 째 삼행시인지 순서를 저장할 변수 
while True:
    goSam = input("\n삼행시에 도전하겠습니까? 네/아니오: ")
    # 아니오 라는 답이 들어오면 더이상 입력받지 않고 반복 종료
    if goSam == "아니오":
        break
    elif goSam != "네": # '아니오' 도 아니고 '네' 도 아니면 잘못된 입력 
        print("잘못된 입력입니다")
    # 네 라는 답이 들어오면 삼행시 단어 및 문구 입력 받고, 고유번호 생성하여 저장
    else:
        samList = [] # 지금 입력되는 삼행시를 저장할 리스트 변수 
        samList.append(samCount) # 몇번째 삼행시 인지 순서를 일단 저장
        samCount = samCount + 1 # 삼행시 순서를 1 증가 시켜 둠 - 다음 삼행시 받을 때 사용 
        samWord = input("삼행시 단어를 입력하세요:")
        samList.append(samWord) # 입력받은 삼행시 단어 저장                    
        for item in samWord: # 각 단어별로 
            samList.append(input(item + ": ")) # 삼행시 내용 입력 받아 저장 
        allSamList.append(samList) # 지금 입력된 삼행시 내용 [순서, 단어, 삼, 행, 시] 을 전체 삼행시 리스트에 저장
        # allSamList는 결과적으로 삼행시 내용 리스트의 리스트가 될 것임 

# 반복이 끝나면 생성된 모든 삼행시 출력
print("\n###모든 삼행시 목록입니다###")
for item in allSamList:
    print(item)

# 삼행시 중 지우고 싶은 것을 고유번호 혹은 삼행시 단어로 삭제
while True:
    rIndex = input("\n지우고 싶은 삼행시의 번호 혹은 단어를 적으세요 (없으면 엔터): ")
    if rIndex == "": # 입력 내용이 없으면 - 그냥 엔터를 쳤으면 - 삭제는 더 이상 안한다고 보고 loop을 끝냄 
        break
    # 고유번호로 지우기
    if rIndex.isdigit(): # 입력 내용이 숫자이면 삼행시 번호로 지운다
        for item in allSamList: # 전체 삼행시 리스트에서 
            if item[0] == int(rIndex): # 이 번호를 가진 삼행시를 찾음 
                allSamList.remove(item) # 지움 
    # 단어로 지우기
    else: # 입력 내용이 숫자가 아니라면 삼행시 단어로 지운다고 본다 
        for item in allSamList: # 전체 삼행시 리스트에서 
            if item[1] == rIndex: # 이 단어를 가진 삼행시를 찾음
                allSamList.remove(item) # 지움 
    # 매번 삭제할 때마다 결과 보여줌
    print("###삭제 후 삼행시 목록입니다###")
    for item in allSamList:
        print(item)

# 삼행시 리스트 재정렬
orderIndexStr = input("\n삼행시의 정렬순서를 , 를 이용하여 지정하세요: ")
# 정렬 순서를 ',' 를 이용해 받았으므로, 받은 텍스트를 ',' 로 split 하면 순서만 저장된 리스트가 생김
# (예) '3, 1, 2, 0' -> [3, 1, 2, 0]
orderIndexList = orderIndexStr.split(",")

orderedList = [] # 정렬된 결과를 저장할 변수 
for orderItem in orderIndexList: # 정렬 순서 리스트에 따라 
    for samItem in allSamList: # 원래 삼행시가 저장된 리스트에서 
        if samItem[0] == int(orderItem.strip()): # 해당 번호의 삼행시를 가져와서
            # strip() 은 split(',') 하고 나서 앞뒤에 있을 수 있는 공백을 없애는 method
            orderedList.append(samItem) # 새로운 정렬결과 리스트에 추가 
            
print("###정렬 후 삼행시 목록입니다###")
for item in orderedList:
    print(item)
