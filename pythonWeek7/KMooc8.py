# 연습하기 3번

List01 = ['apple','banana','quiz','hi','bye']
List01_modified =List01
List02 =['Korea','hi','LOL','Python','apple']


for i in range(len(List01)):
    if List01[i] in List02:
        List02.remove(List01[i])

List03 = List01 + List02
print("List01: ",List01)
print("List02: ",List02)
print("합친 후: ",List03)

List03.sort()
print("정렬 후: ",List03)
