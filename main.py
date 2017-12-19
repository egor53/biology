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
