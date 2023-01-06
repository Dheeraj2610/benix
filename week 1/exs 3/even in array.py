def print_even(arr):
    # Iterate through the array
    for num in arr:
        # Check if the number is even
        if num % 2 == 0:
            print(num)


# Test the function
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print_even(arr)
