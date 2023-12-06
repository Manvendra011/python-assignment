def cubes_of_even_numbers_list_comprehension(input_list):
    return [element**3 for element in input_list if isinstance(element, int) and element % 2 == 0]

# Example usage:
input_list = [1, 2, 3, 4, 5,  6, 9, 8]
result_list_comprehension = cubes_of_even_numbers_list_comprehension(input_list)
print("Result using list comprehension:", result_list_comprehension)
