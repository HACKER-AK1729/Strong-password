import re

def password_strength(password):
    # Scoring system
    score = 0
    feedback = []

    # Length check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 12 characters long.")

    # Uppercase
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Lowercase
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Numbers
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Add at least one digit.")

    # Special characters
    if re.search(r'[^A-Za-z0-9]', password):
        score += 1
    else:
        feedback.append("Add at least one special character (!@#$%^&* etc.).")

    # Strength rating
    if score >= 6:
        strength = "Very Strong"
    elif score >= 4:
        strength = "Strong"
    elif score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"

    return strength, feedback

# Example usage
password = input("Enter your password: ")
strength, suggestions = password_strength(password)

print(f"Password Strength: {strength}")
if suggestions:
    print("Suggestions:")
    for s in suggestions:
        print(f" - {s}")
