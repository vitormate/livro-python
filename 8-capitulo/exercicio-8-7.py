def mdc(a, b):
    if a > b:
        if b == 0:
            return a
        else:
            return mdc(b, a % b)
    else:
        return a

print(mdc(100, 60))