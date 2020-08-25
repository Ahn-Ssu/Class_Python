initValue = int(input(""))
rationValue = int(input(""))
turn = int(input(""))



a0 = initValue
for r in range(1,turn):

    a0 *= rationValue


    if r == turn:
        print(a0)
