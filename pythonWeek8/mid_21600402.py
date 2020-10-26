info ="안녕하세요, 문장 속 문자 검색기입니다."
manual = """--------------------------------------------------------
사용 방법
    1) 탐색할 전체 글(문자열)을 입력합니다. (문장 단위의 구분은 마침표로 수행합니다.)
    2) 찾아낼 단어를 입력하시면 본문 속 해당 단어가 포함된 문장을 모두 출력해드립니다!
    3) 입력할 전체 글의 원본을 보고 싶으면 본문보기라고 입력해주세요.
    4) 양수를 입력하면 해당 번호에 해당하는 문장을 출력해드립니다.
    5) 프로그램 종료는 '바이', '끝', '종료' 중 아무거나 입력해주세요.
    6) '도움말'이라고 입력하시면 해당 메세지를 다시 출력해드립니다.
--------------------------------------------------------"""
exitCommand = ["바이", "끝", "종료"]


print(info)
print(manual)
inputStr = ""

while not inputStr:
    inputStr = input("\n검색 대상 본문을 입력하시오: ")
    if not inputStr :
        print("공백을 입력하셨어요, 다시 입력해주세요")
    if inputStr in exitCommand:
        break
    if inputStr =="도움말":
        print(manual)


temp = ""
inputList = []
splitStr = inputStr.split()

if not (inputStr in exitCommand):
    for word in splitStr:
        if "." in word:
            temp = temp + word
            temp.strip()
            if(temp != ""):
                inputList.append(temp)
            temp = ""
            continue
            
        temp = temp + word + " "




    target = ""
    while not (target in exitCommand) :
        target = input("\n본문에서 검색하고 싶은 단어를 입력하시오 : ")
        target = target.strip()

        if target in exitCommand :
            break
        
        if( target == ""):
            print("공백을 입력하셨어요, 다시 입력해주세요")
        elif (target == "도움말"):
            print(manual)
        elif target == "본문보기":
            for sentence in inputList:
                print(sentence.replace(".","").strip())
        elif target.isdecimal():
            inputNumber = False
            for sentence in inputList:
                tempList = sentence.split()
                if target in tempList:
                    print(sentence.replace(".",""))
                    inputNumber=True
            if not inputNumber:
                print("입력하신 숫자에 해당하는 문장을 찾지 못했습니다.")
        else:
            isin = False
            for element in inputList:
                if target in element:
                    print(element.replace(".",""))
                    isin = True

            if not isin :
                print("찾으시는 단어 '{}' 가 본문에 없습니다".format(target))


print(" \n\n*서비스를 사용해주셔서 감사합니다*")
input("\n                    엔터를 입력하시면 사용이 종료됩니다.")
