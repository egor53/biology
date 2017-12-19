from PYCHARM import A, fnc
import random

def crossing():
    return


def diheterocytozed():
    return 'AaBb'


def homozygoted(value):
    if value == 'a' or value == 'A':
        return 'AAbb'
    elif value == 'b' or value == 'B':
        return 'aaBB'
    else: raise Exception('Введите А или В')

print(A)
print(int(random.random()*10))
print(random.randint(1,27))
List = [1,2,3,4,5,6,7,8,9]
random.shuffle(List)
print(List)