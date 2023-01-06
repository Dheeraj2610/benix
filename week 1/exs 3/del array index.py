def delete_at_index(arr, index):
    # Check if the index is valid
    if index < 0 or index >= len(arr):
        return "Invalid index"

    # Delete the element at the given index
    del arr[index]

    return arr


# Test the function
arr = [1, 2, 3, 4, 5]
print(delete_at_index(arr, 2))
