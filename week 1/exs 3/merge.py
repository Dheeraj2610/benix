def merge(arr1, arr2):
    temp = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            temp.append(arr1[i])
            i += 1
        else:
            temp.append(arr2[j])
            j += 1


print(merge([1, 3, 5], [2, 4, 6]))
