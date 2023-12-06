def swap_first_n_chars(str1, str2, n):
    if n <= 0:
        print("Please enter a positive value for n.")
        return

    if n > min(len(str1), len(str2)):
        print("Value of n exceeds the length of one or both strings.")
        return

    swapped_str1 = str2[:n] + str1[n:]
    swapped_str2 = str1[:n] + str2[n:]

    print(f"After swapping the first {n} characters:")
    print(f"String 1: {swapped_str1}")
    print(f"String 2: {swapped_str2}")

# Accepting input strings and n from the user
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
n_value = int(input("Enter the value of n: "))

# Performing the swap
swap_first_n_chars(string1, string2, n_value)
