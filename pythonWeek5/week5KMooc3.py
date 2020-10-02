
sourceString = input("입력 : ")
count = 0 

for char in sourceString:
    if char == "a":
        count = count + 1
    
print("a의 갯수 :",count)