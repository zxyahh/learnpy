def normalize(name):
    n = map(lambda s:s[0].upper() + s[1:].lower(),name)
    return list(n)
L1 = ['adma','LISA','barT']
print(normalize(L1))

