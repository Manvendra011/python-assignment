def analyze_character(char):
    if char.isalpha():
        if char.isupper():
            print(f"The character '{char}' is an uppercase letter.")
        else:
            print(f"The character '{char}' is a lowercase letter.")
    elif char.isdigit():
        number_names = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
        digit_name = number_names[int(char)]
        print(f"The character '{char}' is a numeric digit, and its name is {digit_name}.")
    else:
        print(f"The character '{char}' is a special character.")

# Accepting a character from the user
user_input = input("Enter a character: ")

# Checking and printing the analysis
analyze_character(user_input)
