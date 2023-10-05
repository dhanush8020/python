n = int(input("Enter the number of elements: "))
arr = list(map(int, input("Enter the elements separated by space: ").split()))

# Split the input array into two halves
middle = n // 2
first_half = arr[:middle]
second_half = arr[middle:]

# Sort the first half in ascending order
first_half.sort()

# Sort the second half in descending order
second_half.sort(reverse=True)

# Concatenate the two halves
result = first_half + second_half

# Print the result
for num in result:
    print(num, end=" ")
