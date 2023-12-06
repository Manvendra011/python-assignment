def validate_name(name):
    try:
        # Check if the name contains digits
        if any(char.isdigit() for char in name):
            raise ValueError("Name should not contain digits.")

        # Check if the name contains special characters
        if not name.isalpha():
            raise ValueError("Name should only contain alphabetic characters.")

        # If no exception is raised, print the valid name
        print(f"Entered name: {name}")

    except ValueError as e:
        print(f"Error: {e}")

# Example usage:
user_name = input("Enter your name: ")
validate_name(user_name)
