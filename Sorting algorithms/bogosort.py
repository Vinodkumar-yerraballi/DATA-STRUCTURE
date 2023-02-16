import random
def bogo_sort(L):
    while not sorted(L):
        random.shuffle(L)

L=[1,2,4,5]
print(bogo_sort(L))