def generate_cubes_dictionary():
    cubes_dict = {key: key**3 for key in range(1, 49)}
    print("Generated Dictionary:")
    print(cubes_dict)

# Example usage:
generate_cubes_dictionary()
