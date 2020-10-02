userName ='홍길동'
retryCount = 1 



while userName[0]!="김" and userName[0]!="최" and userName[0]!="이" and retryCount <= 5:
    userName = input("이름을 입력해주세요")
    retryCount = retryCount+1


if userName[0]!="김" and userName[0]!="최" and userName[0]!="이" and retryCount>5:
    print("5번 이상 실패하셔서 더이상 입력받지 않습니다")
else :
    print("통과")