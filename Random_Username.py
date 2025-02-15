import random
import string

def generate_username(adjectives, nouns, include_numbers, include_specials, length=None):
    adj = random.choice(adjectives)
    noun = random.choice(nouns)
    username = adj + noun

    if include_numbers:
        username += str(random.randint(0, 9999))

    if include_specials:
        special_char = random.choice("!@#$%^&*")
        username += special_char

    if length and len(username) > length:
        username = username[:length]

    return username

def save_to_file(usernames, filename="usernames.txt"):
    try:
        with open(filename, "w") as file:
            file.write("\n".join(usernames))
        print(f"Usernames saved to {filename}")
    except IOError as e:
        print(f"Error saving to file: {e}")

def get_yes_no_input(prompt):
    while True:
        try:
            user_input = input(prompt).strip().lower()
            if user_input not in ["y", "n"]:
                raise ValueError("Invalid input. Please enter 'y' for yes or 'n' for no.")
            return user_input == "y"
        except ValueError as e:
            print(e)

def get_maximum_length():
    while True:
        try:
            length_input = input("Enter maximum username length (press Enter to skip): ").strip()
            if length_input == "":
                return None  
            length = int(length_input)
            if length <= 0:
                raise ValueError("Length must be a positive integer.")
            return length
        except ValueError as e:
            print(f"Invalid input for length: {e}")
            print("Please enter a valid positive integer for the length.")

def main():
    adjectives = ["Tiger", "Dragon", "Eagle", "Fox", "Lion", "Wolf", "Panda", "Bear","Happy", "Cool", "Brave", "Smart", "Quick", "Silly", "Bright", "Strong","Legend","Hercules","Enigma","Orion","Cygnus","Hero"]
    nouns = ["Tiger", "Dragon", "Eagle", "Fox", "Lion", "Wolf", "Panda", "Bear","Happy", "Cool", "Brave", "Smart", "Quick", "Silly", "Bright", "Strong","Legend","Hercules","Enigma","Orion","Cygnus","Hero"]

    print("Welcome to the Random Username Generator!")
    
    try:
        num_usernames = int(input("How many usernames would you like to generate?: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    include_numbers = get_yes_no_input("Include numbers? (Y/N): ")
    include_specials = get_yes_no_input("Include special characters? (Y/N): ")
    
    max_length = get_maximum_length()

    usernames = [
        generate_username(adjectives, nouns, include_numbers, include_specials, max_length)
        for _ in range(num_usernames)
    ]

    print("\nGenerated Usernames:")
    print("\n".join(usernames))

    save = get_yes_no_input("\nWould you like to save these usernames to a file? (Y/N): ")
    if save:
        save_to_file(usernames)

if __name__ == "__main__":
    main()
