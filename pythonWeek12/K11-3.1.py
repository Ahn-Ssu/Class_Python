#연습하기 2번

try:
    f = open('./pythonWeek12/poem.txt','r')
    outf = open('./pythonWeek12/numpoem.txt','w')
except IOError as err:
    print("unabel to handel files", err)

Numword = []
count = len(f.readlines())
f.close()

f = open('./pythonWeek12/poem.txt','r')
for i in range(count):
    fline = f.readline()
    flist = fline.split()
    outf.write(str(len(flist)) + "\n")

f.close()
outf.close()
f = open('./pythonWeek12/numpoem.txt','r')
print(f.readlines())