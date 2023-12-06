def cubes_of_even_numbers_for_loop(input_list):
    result = []
    for element in input_list:
        if isinstance(element, int) and element % 2 == 0:
            result.append(element**3)
    return result

# Example usage:
input_list = [1, 2, 3, 4, 5, 7, 6, 100, 8]
result_for_loop = cubes_of_even_numbers_for_loop(input_list)
print("Result using 'for' loop:", result_for_loop)
