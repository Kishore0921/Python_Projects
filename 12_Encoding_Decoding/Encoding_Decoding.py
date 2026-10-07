def encode_text(text, shift):
    """Encodes the text by shifting characters forward."""
    encoded_result = ""
    for char in text:
        if char.isalpha():
            # Determine if the character is uppercase or lowercase
            start = ord('A') if char.isupper() else ord('a')
            # Shift the character and wrap around the alphabet
            new_char = chr(start + (ord(char) - start + shift) % 26)
            encoded_result += new_char
        else:
            # Leave spaces and punctuation as they are
            encoded_result += char
    return encoded_result


def decode_text(text, shift):
    """Decodes the text by shifting characters backward."""
    # Decoding is simply encoding with a negative shift
    return encode_text(text, -shift)


def main():
    print("--- Text Encoder & Decoder ---")
    shift_value = 4  # The key used for shifting the alphabet

    while True:
        print("\nChoose an option:")
        print("1. Encode Text")
        print("2. Decode Text")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == '1':
            user_input = input("Enter the text to encode: ")
            result = encode_text(user_input, shift_value)
            print(f"\nEncoded Result: {result}")
            
        elif choice == '2':
            user_input = input("Enter the text to decode: ")
            result = decode_text(user_input, shift_value)
            print(f"\nDecoded Result: {result}")
            
        elif choice == '3':
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

# Run the program
if __name__ == "__main__":
    main()
