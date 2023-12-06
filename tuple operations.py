def tuple_operations(t1):
    # a. Print half the values of the tuple in one line and the other half in the next line.
    half_length = len(t1) // 2
    print("a. Half the values of the tuple:")
    print(t1[:half_length])
    print(t1[half_length:])

    # b. Print another tuple whose values are even numbers in the given tuple.
    even_numbers_tuple = tuple(num for num in t1 if num % 2 == 0)
    print("\nb. Tuple of even numbers:")
    print(even_numbers_tuple)

    # c. Concatenate a tuple t2=(11,13,15) with t1.
    t2 = (11, 13, 15)
    concatenated_tuple = t1 + t2
    print("\nc. Concatenated tuple:")
    print(concatenated_tuple)

    # d. Return maximum and minimum value from this tuple.
    max_value = max(concatenated_tuple)
    min_value = min(concatenated_tuple)
    return max_value, min_value

# Example usage:
t1 = (1, 2, 5, 7, 9, 2, 4, 6, 8, 10)
result = tuple_operations(t1)
print("\nd. Maximum and minimum values:")
print("Maximum:", result[0])
print("Minimum:", result[1])
