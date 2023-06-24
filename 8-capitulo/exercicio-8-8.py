def mdc(a, b):
    if a > b:
        if b == 0:
            return a
        else:
            return mdc(b, a % b)
    else:
        return a

def mmc(a, b):
    return abs(a*b) / mdc(a,b)

print(mmc(12, 9))