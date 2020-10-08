
majorList = ["GLS", "경영경제", "국제어문", "법학부", "언론정보", "상담복지",
             "생명과학", "공간환경", "전산전자", "콘융디","기계제어","ICT"]


print("="*85)
for indexNumber, major in zip(range(1,13),majorList):
    print("{:>2}) {:<}".format(indexNumber,major), end=" | ")
    if indexNumber == 6: print()
print()
print("="*85)

print("유라 막학기 화이티잉")