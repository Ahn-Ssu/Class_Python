#연습하기 1번

infile = open('./pythonWeek12/number.txt','r')

numbers = infile.readlines()

sum =0
ave =0 
for number in numbers:
    sum += int(number)

ave = sum / len(numbers)
print("Sum :",sum)
print("Ave :",ave)