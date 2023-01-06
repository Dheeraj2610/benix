max_stars = 3

# Print the upper half of the pattern
for i in range(1, max_stars + 1):
    print("*" * i)

# Print the lower half of the pattern
for i in range(max_stars - 1, 0, -1):
    print("*" * i)
