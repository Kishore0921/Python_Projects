import random
import string

print("Welcome to the Random Password Generator!")


def get_password_length():
    """Prompts the user for a valid password length between 8 and 20."""
    while True:
        try:
            length = int(input("Enter desired password length (8-20): "))
            if length < 8:
                print("Password length should be at least 8 characters.")
                continue
            if length > 20:
                print("Password length cannot be more than 20 characters.")
                continue
            return length
        except ValueError:
            print("Please enter a valid number.")


def generate_password(length):
    """Generates a random password ensuring a mix of all character types."""
    # 1. Define the separate pools
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

    # 2. Combine them into one full pool
    all_characters = letters + numbers + symbols

    # 3. Guarantee at least one of each type is present
    password_list = [
        random.choice(letters),
        random.choice(numbers),
        random.choice(symbols),
    ]

    # 4. Fill the remaining length randomly from the combined pool
    remaining_length = length - len(password_list)
    password_list += [
        random.choice(all_characters) for _ in range(remaining_length)
    ]

    # 5. Shuffle to randomize the positions of the guaranteed characters
    random.shuffle(password_list)

    # 6. Join into a single string
    return "".join(password_list)


def main():
    print("--- Random Password Generator --- \n")

    # Get length from the user
    length = get_password_length()

    # Generate the password
    password = generate_password(length)

    print(f"\nGenerated Password: {password}")


if __name__ == "__main__":
    main()
