def find_occurrences(main_string, sub_string):
    indices = []
    start_index = 0

    while start_index < len(main_string):
        index = main_string.find(sub_string, start_index)
        if index == -1:
            break
        indices.append(index)
        start_index = index + 1

    return indices if indices else -1

# Example usage:
main_str = input("Enter the main string: ")
sub_str = input("Enter the sub string: ")

result = find_occurrences(main_str, sub_str)

if result == -1:
    print(f"The sub string '{sub_str}' is not present in the main string '{main_str}'.")
else:
    print(f"The sub string '{sub_str}' occurs at indices: {result}")
