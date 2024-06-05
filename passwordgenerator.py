import random
import string

def generate_password(length, use_uppercase=True, use_digits=True, use_special_chars=True):
    # Define the character sets to use in the password
    character_set = string.ascii_lowercase  # Start with lowercase letters

    if use_uppercase:
        character_set += string.ascii_uppercase

    if use_digits:
        character_set += string.digits

    if use_special_chars:
        character_set += string.punctuation

    # Generate the password
    password = ''.join(random.choice(character_set) for _ in range(length))

    return password

def main():
    # Prompt the user to specify the desired length of the password
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Please enter a positive integer.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Prompt the user to specify the complexity of the password
    use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
    use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
    use_special_chars = input("Include special characters? (y/n): ").strip().lower() == 'y'

    # Generate and display the password
    password = generate_password(length, use_uppercase, use_digits, use_special_chars)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
