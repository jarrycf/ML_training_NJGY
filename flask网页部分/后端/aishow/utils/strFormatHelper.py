def toUp(lis):
    lis=list(map(lambda x:x.upper(),lis))
    return lis
def isNone(*lis):
    for i in lis:
        if not i:
            return True
    return False
