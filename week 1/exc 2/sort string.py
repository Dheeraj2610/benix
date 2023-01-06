string = input("Enter String: ")
lst = [string[i] for i in range(0, len(string))]
lst.sort()
for i in lst:
    print(i, end="")
