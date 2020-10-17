# 연습하기 1번 
inputString = input("문자열 입력")

stringList = inputString.split()

removeTarget = input("입력한 문자열 중 삭제할 단어 입력")
if removeTarget in stringList:
    stringList.remove(removeTarget)

appendSource = input("추가할 단어 입력")
stringList.append(appendSource)

convertString = ' '.join(stringList)
print(convertString)