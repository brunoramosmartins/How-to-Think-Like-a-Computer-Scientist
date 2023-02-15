def eDivisivel(x, y):
    if x % y == 0:
        return True
    else:
        return False

if eDivisivel(10, 5):
    print('That works!')
else:
    print('Those values are no good.')
