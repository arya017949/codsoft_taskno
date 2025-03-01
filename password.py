import string
import secrets

def generate_password(length=12, use_uppercase=True, use_numbers=True, use_special_chars=True):
    """Generate a random password."""
    chars = string.ascii_lowercase
    
    if use_uppercase:
        chars += string.ascii_uppercase
    if use_numbers:
        chars += string.digits
    if use_special_chars:
        chars += string.punctuation
    
    # Ensure at least one of each required character type is included
    password = []
    if use_uppercase:
        password.append(secrets.choice(string.ascii_uppercase))
    if use_numbers:
        password.append(secrets.choice(string.digits))
    if use_special_chars:
        password.append(secrets.choice(string.punctuation))
    
    # Fill the rest of the password length with random characters
    for _ in range(length - len(password)):
        password.append(secrets.choice(chars))
    
    # Shuffle the list to avoid the first characters always being in the same character type order
    secrets.SystemRandom().shuffle(password)
    
    return ''.join(password)

def password_generator():
    print("Password Generator")
    
    while True:
        try:
            length = int(input("Enter the password length (default=12): ") or 12)
            if length < 8:
                print("Password length should be at least 8 characters.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        use_uppercase = input("Include uppercase letters? (y/n, default=y): ").lower() != 'n'
        use_numbers = input("Include numbers? (y/n, default=y): ").lower() != 'n'
        use_special_chars = input("Include special characters? (y/n, default=y): ").lower() != 'n'
        
        # Ensure at least one character type is selected
        if not (use_uppercase or use_numbers or use_special_chars):
            print("Please select at least one character type.")
            continue
        
        password = generate_password(length, use_uppercase, use_numbers, use_special_chars)
        print(f"Generated Password: {password}")
        
        choice = input("Generate another password? (y/n): ").lower()
        if choice != 'y':
            break

if __name__ == "__main__":
    password_generator()
