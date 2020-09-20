koreanScore = float(input("국어 성적을 입력해주세욥 : "))
englishScore = float(input("영어 성적을 입력해주세욥 : "))
mathScore = float(input("수학 성적을 입력해주세요 : "))

average = (koreanScore+englishScore+mathScore)/3.0
print("3개 과목의 평균은 {}입니다".format(average))
# print()
# if average>= 60 and koreanScore >= 50 and englishScore >= 50 and mathScore >= 50 :
#     print("성적평균은 {}이며, 과락과목도 없기 때문에 합격입니다.".format(average))
# else :
#     if average >= 60:
#         print("성적평균은 {}이지만 50점 미안 과락이 있어서 불합격 입니다.".format(average))
#     else :
#         print("성적평균은 {}, 불합격 입니다.".format(average))
