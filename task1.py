import string
import random

def generate_random_password(length=12, use_uppercase=True, use_digits=True, use_special_chars=True):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    if length < 1:
        raise ValueError("Password length must be at least 1.")
    
    return ''.join(random.choice(characters) for _ in range(length))

# Example usage
password = generate_random_password()
print(password)
