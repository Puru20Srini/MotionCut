def count_words(input):
    try:
        if not input.strip():
            raise ValueError("Input cannot be empty or just spaces.")
        words = input.split()
        return len(words)
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

input = input("Enter a word or sentence: ")

word_count = count_words(input)

if word_count is not None:
    print(f"Number of words: {word_count}")