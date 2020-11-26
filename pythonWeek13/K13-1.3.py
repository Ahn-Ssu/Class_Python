#연습하기 2번

inf = open('./pythonWeek12/poem.txt', 'r')
sm = inf.readlines()

for i in range(len(sm)):
    s = sm[i].strip()
    slist = s.split()
    print(slist)

inf.close() 