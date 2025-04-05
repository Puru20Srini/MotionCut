def reverse_characters(text):
    """Reverse the character order of the input text."""
    return text[::-1]

def reverse_words(text):
    """Reverse the order of words in the input text."""
    words = text.split()  
    reversed_words = ' '.join(words[::-1])  
    return reversed_words

def get_user_input():
    """Get user input and handle empty strings."""
    while True:
        text = input("Enter a sentence: ").strip()
        if text:
            return text
        else:
            print("Input cannot be empty. Please try again.")

def main():
    while True:
        print("\nText Reverser Menu:")
        print("1. Reverse Character Order")
        print("2. Reverse Word Order")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ").strip()

        if choice == '1':
            text = get_user_input()
            reversed_text = reverse_characters(text)
            print(f"Reversed Characters: {reversed_text}")
        elif choice == '2':
            text = get_user_input()
            reversed_text = reverse_words(text)
            print(f"Reversed Words: {reversed_text}")
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()