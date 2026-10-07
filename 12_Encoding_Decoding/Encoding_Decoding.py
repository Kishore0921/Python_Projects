import random
import string

def generate_key_map():
    """Generates a completely unique 2-character map for each alphanumeric character and space."""
    source_chars = (
        "abcdefghijklmnopqrstuvwxyz"
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "0123456789 "
    )
    
    # Pool containing letters, digits, and basic keyboard punctuation
    symbols = list(string.ascii_lowercase + string.ascii_uppercase + string.digits + "!?@#$%^&*_-")
    
    # Generate all possible 2-character permutations
    all_combinations = []
    for char1 in symbols:
        for char2 in symbols:
            all_combinations.append(char1 + char2)
            
    # Shuffle the combinations to ensure randomness every time
    random.shuffle(all_combinations)
    
    # Map each source character to a unique 2-character combination
    encode_map = {}
    decode_map = {}
    for i, char in enumerate(source_chars):
        pair = all_combinations[i]
        encode_map[char] = pair
        decode_map[pair] = char
        
    return encode_map, decode_map


def encode_text(text, encode_map):
    """Encodes the text by replacing each character with its unique 2-character code."""
    encoded_result = ""
    for char in text:
        # Use the mapped 2-char code if it exists, otherwise leave the character as is
        encoded_result += encode_map.get(char, char)
    return encoded_result


def decode_text(text, decode_map):
    """Decodes the text by reading it in 2-character blocks."""
    decoded_result = ""
    i = 0
    while i < len(text):
        # Grab a 2-character chunk
        pair = text[i:i+2]
        
        # If the chunk matches a code in our map, decode it and advance by 2
        if pair in decode_map:
            decoded_result += decode_map[pair]
            i += 2
        else:
            # If it's an unmapped symbol (like punctuation that wasn't encoded), leave it and advance by 1
            decoded_result += text[i]
            i += 1
            
    return decoded_result


def main():
    print("--- Dynamic Character-Pair Encoder & Decoder ---")
    
    # Persistent dictionary to tie each specific encoded string to its unique decoding map
    active_keys = {}

    while True:
        print("\nChoose an option:")
        print("1. Encode Text (Generates a new random code map)")
        print("2. Decode Text")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == '1':
            user_input = input("Enter the text to encode: ")
            
            # Generate a fresh, random map for this specific string
            encode_map, decode_map = generate_key_map()
            result = encode_text(user_input, encode_map)
            
            # Store the decoding map tied to this specific output string
            active_keys[result] = decode_map
            
            print(f"\nEncoded Result: {result}")
            print("(Note: Save this exact output string to decode it later in this session!)")
            
        elif choice == '2':
            user_input = input("Enter the encoded text to decode: ")
            
            # Look up the specific decoding map for this exact text
            if user_input in active_keys:
                specific_decode_map = active_keys[user_input]
                result = decode_text(user_input, specific_decode_map)
                print(f"\nDecoded Result: {result}")
            else:
                print("\n[Error] Could not decode. That specific encoded text was not generated in this session.")
            
        elif choice == '3':
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
