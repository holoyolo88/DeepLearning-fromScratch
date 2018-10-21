def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1*w1 + x2*w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1

def OR(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.2
    tmp = x1*w1 + x2*w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1

def NAND(x1, x2):
    w1, w2, theta = -0.5, -0.5, -0.7
    tmp = x1*w1 + x2*w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1

def printResult(func, strFuncName):
    for i in range(4):
        print('{} {} {} : {}'.format(x1[i],strFuncName, x2[i], func(x1[i], x2[i])))
    print('-'*15)


x1 = [0, 0, 1, 1]
x2 = [0, 1, 0, 1]

printResult(AND, 'AND')
printResult(OR, 'OR')
printResult(NAND, 'NAND')