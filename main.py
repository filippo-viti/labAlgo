import random

from OrderedList import OrderedList

if __name__ == '__main__':
    l = OrderedList()
    for i in range(1,10):
        l.insert(random.randint(1,30))
    print(l)
