rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

# Print the top half of the pattern
for i in range(1, rows + 1):
    for j in range(i):
        print(i, end="")
    print()

# Print the bottom half of the pattern
for i in range(rows - 1, 0, -1):
    for j in range(i):
        print(i, end="")
    print()
