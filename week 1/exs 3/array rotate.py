def rotate_right(arr):
    # Save the last 2 elements of the array
    temp1 = arr[-1]
    temp2 = arr[-2]

    # Shift all elements in the array to the right by 2 positions
    for i in range(len(arr)-2, 0, -1):
        arr[i+2] = arr[i]

    # Insert the saved elements at the beginning of the array
    arr[0] = temp1
    arr[1] = temp2

    return arr


# Test the function
arr = [1, 2, 3, 4, 5]
print(rotate_right(arr))
