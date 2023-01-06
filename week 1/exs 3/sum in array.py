def sum_array(arr):
    # Initialize a variable to store the sum
    total = 0

    # Iterate through the array and add each element to the total
    for num in arr:
        total += num

    return total


# Test the function
arr = [1, 2, 3, 4, 5]
print(sum_array(arr))
