height = float(input("키를 m 단위로 입력해주세요 :"))
weight = float(input("몸무게를 kg 단위로 입력해주세요 : "))

bmi = weight / (height**2)

if bmi < 18.5:
    print("BMI 지수는 {}이며, 저체중 상태입니다.".format(bmi))
elif bmi < 23:
    print("BMI 지수는 {}이며, 정상 상태입니다.".format(bmi))
elif bmi < 25:
    print("BMI 지수는 {}이며, 과체중 상태입니다.".format(bmi))
elif bmi < 30:
    print("BMI 지수는 {}이며, 비만1 상태입니다.".format(bmi))
elif bmi < 40:
    print("BMI 지수는 {}이며, 비만2 상태입니다.".format(bmi))
else :
    print("BMI 지수는 {}이며, 심각한 비만3 상태입니다.".format(bmi))