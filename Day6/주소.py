from copy import copy

# 리스트
a = [1,2,3]
b = a

print(id(a)) # 17563592
print(id(b)) # 17563592
print(a is b) # True 

# list deep Copy
b = a[:]

print(id(a)) # 17563592
print(id(b)) # 62066344
print(a is b) # False 

# from copy import copy
c = [4,5,6]
d = copy(c)

print(id(c)) # 58433480
print(id(d)) # 58433512
print(c is b) # False