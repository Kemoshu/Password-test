import random
import string

# Function to evaluate password strength
def evaluate_password(password):
    length = len(password)  # Get password length
    has_upper = any(c.isupper() for c in password)  # Check for uppercase letters
    has_lower = any(c.islower() for c in password)  # Check for lowercase letters
    has_digit = any(c.isdigit() for c in password)  # Check for digits
    has_special = any(c in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/" for c in password)  # Check for special characters
    
    score = length + has_upper + has_lower + has_digit + has_special  # Calculate score

    if score < 6:
        return "Weak"
    elif score < 10:
        return "Medium"
    else:
        return "Strong"

# Function to generate a strong password
def generate_strong_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))