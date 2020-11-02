import random

def gen_random(a,b):

    r = random.randrange(a,b)
    c=chr(65+r)
    print(r, c)

for i in range(10):
    gen_random(i+1, i+10)