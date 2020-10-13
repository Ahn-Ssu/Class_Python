import sys


try:
    inf = open('myfile.txt', 'r')
    s = freadline()

except IOError as err:
    print("I/O error :{}".format(err))