import cmath  # Importing the complex math module for handling complex roots

def find_roots(a, b, c):
    # Calculate the discriminant
    d = cmath.sqrt(b**2 - 4*a*c)

    # Compute the roots using the quadratic formula
    root1 = (-b + d) / (2 * a)
    root2 = (-b - d) / (2 * a)

    return root1, root2

# Input coefficients from the user
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Find and display the roots
roots = find_roots(a, b, c)
print("Root 1:", roots[0])
print("Root 2:", roots[1])
