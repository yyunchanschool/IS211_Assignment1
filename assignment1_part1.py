def listDivide (numbers, divide = 2):
    d = 0
    for x in numbers:
        if x % divide == 0:
            d += 1
    return d

class ListDivideException (Exception):
    pass

def testListDivide ():
    if listDivide ([1, 2, 3, 4, 5]) != 2:
        raise ListDivideException ()
    elif listDivide ([2, 4, 6, 8, 10]) != 5:
        raise ListDivideException ()
    elif listDivide ([30, 54, 63, 98, 100], divide = 10) != 2:
        raise ListDivideException ()
    elif listDivide ([]) != 0:
        raise ListDivideException ()
    elif listDivide ([1, 2, 3, 4, 5], 1) != 5:
        raise ListDivideException ()

testListDivide()