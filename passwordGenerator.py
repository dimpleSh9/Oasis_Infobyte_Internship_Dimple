import random
import string

def generate_password(length, digits, letters, symbols):
    #Function to generate a random password

    # Define characters to choose from5
    charPick = ""
    if digits == "yes":
        charPick += string.digits
    
    if letters == "yes":
        charPick += string.ascii_letters
    
    if symbols == "yes":
        charPick += string.punctuation

    if digits == "no" and letters == "no" and symbols == "no":
        print("Error: you did not pick any character.")
        return 0
    
    # Generate password
    password = ''.join(random.choice(charPick) for _ in range(length))
    
    return password

def main():
    length = int(input("Enter the length of the password: "))
    digits = input("Do want digits(yes/no): ")
    letters = input("Do want letters(yes/no): ")
    symbols = input("Do want special symbols(yes/no): ")
    digits = digits.lower()
    letters = letters.lower()
    symbols = symbols.lower()
    password = generate_password(length, digits, letters, symbols)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
