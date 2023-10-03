def sort_array(arr):
    # Sort the array in ascending order
    ascending_order = sorted(arr)

    # Sort the array in descending order
    descending_order = sorted(arr, reverse=True)

    return ascending_order, descending_order

# Input array
input_array = [5, 8, 6, 2, 9, 7]

# Call the function to sort the array
ascending_result, descending_result = sort_array(input_array)

# Print the sorted arrays
print("Ascending Order:", ascending_result)
print("Descending Order:", descending_result)
