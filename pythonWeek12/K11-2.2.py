#연습하기 3번

inf = open('./pythonWeek12/poem.txt', 'r')
count = 0 

countlist = inf.readlines()
count = len(countlist)
inf.close()

inf = open('./pythonWeek12/poem.txt', 'r')
NumWord = []
for i in range(count):
    fline = inf.readline()
    flist = fline.split()
    NumWord.append(len(flist))
    
print(NumWord)
inf.close()