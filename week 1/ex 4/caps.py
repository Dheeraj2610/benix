def word_both_cap(str):
    return ' '.join(map(lambda s: s[:-1]+s[-1].upper(),
                        s.title().split()))


s = "hellow world"
print("String before:", s)
print("String after:", word_both_cap(str))
