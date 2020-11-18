#연습하기 3번
import os
import shutil

shutil.copy('./pythonWeek12/numpoem.txt','./pythonWeek12/nump.txt')
os.remove("./pythonWeek12/numpoem.txt")

try:
    inf = open('nump.txt', 'r')
    s = inf.readlines()
    sum  = 0
    for i in range(len(s)):
        sum += sum + int(s[i])
    print("평균 =", sum/len(s))
except IOError as err:
    print("I/O error: {}".format(err))
else:
    inf.close()
