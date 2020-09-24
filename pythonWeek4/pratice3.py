# 국어 영어 수학 시험 성적을 입력받음
#  평균을 구하고 3과목  중 한과목이라도 50미만이면 '과락' 과락이 없고 평균이 60점 이상이면 합격
#  아니면 불합격 

koreanScore = float(input("국어 성적을 입력해주세욥 : "))
englishScore = float(input("영어 성적을 입력해주세욥 : "))
mathScore = float(input("수학 성적을 입력해주세요 : "))

average = (koreanScore+englishScore+mathScore)/3.0
# print("3개 과목의 평균은 {:>4}입니다".format(average))

if koreanScore<50 or englishScore<50 or mathScore <50:
    print("과락")
elif average >= 60:
    print("합격")
else:
    print("불합격")
