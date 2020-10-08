
majorList = ["GLS", "경영경제", "국제어문", "법학부", "언론정보", "상담복지", "생명과학", "공간환경", "전산전자", "콘융디","기계제어","ICT"]


for indexNumber, major in zip(range(1,13),majorList):
    print("{:>2} {:<}".format(indexNumber,major), end=" | ")
print()

    