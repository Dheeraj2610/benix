def sum(num):
    if num == 0:
        return 0
    else:
        return (num % 10 + sum(num//10))


n = 12345
result = sum(n)
print("sum of ", n, "is", result)
