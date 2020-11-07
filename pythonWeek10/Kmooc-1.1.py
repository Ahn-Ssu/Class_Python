input_str = input("30글자 이상 영어 문장 입력 : ")
alpha = 0
upper = 0
lower = 0


for letter in input_str:
    alpha = alpha + letter.isalpha()
    upper = upper + letter.isupper()
    lower = lower + letter.islower()

print("알파벳 개수 : ", alpha,",대문자 개수: ", upper,",소문자 개수 : ",lower)

# As we have already used the term module