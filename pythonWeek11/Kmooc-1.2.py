#연습하기 3번
import random

s = 'abcdefghijklmnopqrstuvwxyz'
base_s = random.sample(s, 26)

password = []
password_hint = list(zip(s, base_s))
print(password_hint)


input_str = input("문자열 입력: ")
for letter in input_str:
    for i in range(26):
        if letter == password_hint[i][0]:
            password.append(password_hint[i][1])  
          
print(password)
