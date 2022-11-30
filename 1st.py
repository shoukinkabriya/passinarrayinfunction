def decor(num):
    def innr():
        add=num()
        a=add + 12
        return a
    return innr


@decor
def num():
    return 10
ad=num()
print(ad)