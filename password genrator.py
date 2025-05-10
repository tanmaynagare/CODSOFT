import random
import string

def generate_password(length, use_digits=True, use_special=True):
    characters = string.ascii_letters  # A-Z and a-z
    if use_digits:
        characters += string.digits     # 0-9
    if use_special:
        characters += string.punctuation  # !@#$%^&*() etc.

    if length < 4:
        return "Password length should be at least 4 characters."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("🔐 Password Generator 🔐")
    try:
        length = int(input("Enter desired password length: "))
        digits = input("Include numbers? (y/n): ").strip().lower() == 'y'
        special = input("Include special characters? (y/n): ").strip().lower() == 'y'

        password = generate_password(length, use_digits=digits, use_special=special)
        print(f"\nGenerated Password: {password}\n")
    except ValueError:
        print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    main()
