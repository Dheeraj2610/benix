def add(a, b):
    if (b == 0):
        return a
    else:
        return add(a, b-1)+1


a = int(input("enter the 1st no"))
b = int(input("enter 2the 2nd no"))
print("sum is", add(a, b))
