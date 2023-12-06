def file_statistics(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

        # a. Print the total number of characters, words, and lines in the file
        total_characters = len(content)
        total_words = len(content.split())
        total_lines = content.count('\n') + 1

        print(f"a. Total characters: {total_characters}")
        print(f"   Total words: {total_words}")
        print(f"   Total lines: {total_lines}")

        # b. Calculate the frequency of each character in the file
        character_frequency = {}
        for char in content:
            if char.isalnum():
                character_frequency[char] = character_frequency.get(char, 0) + 1

        print("\nb. Character frequency:")
        for char, frequency in character_frequency.items():
            print(f"   '{char}': {frequency}")

        # c. Print the words in reverse order
        words = content.split()
        reversed_words = ' '.join(words[::-1])
        print("\nc. Words in reverse order:")
        print(reversed_words)

        # d. Copy even lines to 'File1' and odd lines to 'File2'
        lines = content.splitlines()
        even_lines = [line for i, line in enumerate(lines, start=1) if i % 2 == 0]
        odd_lines = [line for i, line in enumerate(lines, start=1) if i % 2 != 0]

        with open('File1.txt', 'w') as file1:
            file1.write('\n'.join(even_lines))

        with open('File2.txt', 'w') as file2:
            file2.write('\n'.join(odd_lines))

# Example usage:
file_path = 'example.txt'  # Replace with the path to your file
file_statistics(file_path)
