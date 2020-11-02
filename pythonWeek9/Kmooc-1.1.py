import random

def random_picker(lists, number):
    for i in range(number):
        print(random.choice(lists))


num_list = [3,1,7,11,25,5,4,9]


random_picker(num_list, 3)
