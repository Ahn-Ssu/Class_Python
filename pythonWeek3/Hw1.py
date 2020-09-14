targetName = input("생일 축하 받는 사람의 이름을 입력해주세요")
Year = int(input("생일 축하 받는 분의 출생년도를 알려주세요"))
Food = input("이분은 어떤 음식을 좋아하시나요?")
userName = input("생일 축하 하는 분의 성함을 알려주세요")
decoText = input("카드의 앞과 끝을 꾸미려고 하는데, 어떤 모양으로 꾸밀까요?")



print(decoText*40)
print("      "+targetName+"님",str(2020-Year+1)+"살 생일을 축하해요" )
print("      우리 다음에", Food+"먹으러 같이가요!")
print("   "+targetName+"님을 만나서 너무 즐겁고 좋아요 \n     우리 앞으로도 잘 지내요")
print("              "+userName,"드림")
print(decoText*40)