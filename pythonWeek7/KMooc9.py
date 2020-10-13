# 연습하기 4번 
f1 = ['apple', 'blueberry','melon','tomato']
f2 = ['strawberry', 'lemon', 'banana']
f3 = f1 + f2
print(f3)

index = len(f3)
i = 0

while i < index :
    if f3[i][0] == "b":
        f3.remove(f3[i])
        i = i - 1
        index = index -1 # 삭제하면 전체길이가 줄어들음 
    i = i + 1

print("remove all 'b' elements = ", f3)