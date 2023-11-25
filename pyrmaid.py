def print_pyramid(rows):
    for i in range(1, rows + 1):
        # Print spaces
        print(" " * (rows - i), end="")
        # Print '*' characters
        print("* " * i)

def print_reverse_pyramid(rows):
    for i in range(rows, 0, -1):
        # Print spaces
        print(" " * (rows - i), end="")
        # Print '*' characters
        print("* " * i)

# Input the number of rows for the pyramid
num_rows = int(input("Enter the number of rows for the pyramid: "))

# Print the pyramid
print("Pyramid:")
print_pyramid(num_rows)

# Print a separator line between the two patterns
print("\n" + "-" * 20 + "\n")

# Print the reverse pyramid
print("Reverse Pyramid:")
print_reverse_pyramid(num_rows)
