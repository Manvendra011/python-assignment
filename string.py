def find_frequency(char, input_string):
    frequency = input_string.count(char)
    print(f"The frequency of '{char}' in the string is: {frequency}")

def replace_character(old_char, new_char, input_string):
    new_string = input_string.replace(old_char, new_char)
    print(f"The string after replacing '{old_char}' with '{new_char}': {new_string}")

def remove_first_occurrence(char, input_string):
    new_string = input_string.replace(char, '', 1)
    print(f"The string after removing the first occurrence of '{char}': {new_string}")

def remove_all_occurrences(char, input_string):
    new_string = input_string.replace(char, '')
    print(f"The string after removing all occurrences of '{char}': {new_string}")

# Accepting input string from the user
user_string = input("Enter a string: ")

# Operations
char_to_find = input("Enter a character to find its frequency: ")
find_frequency(char_to_find, user_string)

char_to_replace = input("Enter the character to replace: ")
new_char = input("Enter the new character: ")
replace_character(char_to_replace, new_char, user_string)

char_to_remove_first = input("Enter the character to remove (first occurrence): ")
remove_first_occurrence(char_to_remove_first, user_string)

char_to_remove_all = input("Enter the character to remove (all occurrences): ")
remove_all_occurrences(char_to_remove_all, user_string)
