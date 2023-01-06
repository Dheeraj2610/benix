def converttobin(n):
    if (n > 1):
        converttobin(n//2)
    print(n % 2, end='')


dec = 24
converttobin(dec)
print()
