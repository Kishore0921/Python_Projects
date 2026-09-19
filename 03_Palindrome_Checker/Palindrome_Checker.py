import colorama
from colorama import Fore, Style

# Initialize colorama (required for Windows support)
colorama.init(autoreset=True)

print("Palindrome checker for both word and numbers\n")

str1 = input("Enter a word or number to check if it is a palindrome: ")
str2 = str1[::-1]

if str1 == str2:
    # Prints in green text
    print(f"{Fore.GREEN}{str1} is a palindrome!{Style.RESET_ALL}")
else:
    # Prints in red text
    print(f"{Fore.RED}{str1} is not a palindrome.{Style.RESET_ALL}")


"""Key Additions:
colorama.init(autoreset=True): Initializes the library. 
Setting autoreset=True automatically resets the color back to normal after 
every print statement so your terminal doesn't stay colored permanently.
Fore.GREEN and Fore.RED: Changes the foreground text color.
Style.RESET_ALL: Explicitly turns off the coloring (acts as a backup safeguard)."""