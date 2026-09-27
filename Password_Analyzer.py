import re

def analyze_password(password):

    score = 0
    suggestions = []

    # Check password length
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    # Check uppercase letter
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add an uppercase letter.")

    # Check lowercase letter
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add a lowercase letter.")

    # Check number
    if re.search(r"[0-9]", password):
        score += 1
    else:
        suggestions.append("Add a number.")

    # Check special character
    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        suggestions.append("Add a special character.")

    # Decide password strength
    if score <= 2:
        strength = "WEAK"
    elif score <= 4:
        strength = "MEDIUM"
    else:
        strength = "STRONG"

    return score, strength, suggestions


print("====================================")
print("      PASSWORD STRENGTH ANALYZER")
print("====================================")

password = input("Enter your password: ")

score, strength, suggestions = analyze_password(password)

print("\nPassword Strength:", strength)
print("Score:", score, "/ 5")

if suggestions:
    print("\nSuggestions:")
    for suggestion in suggestions:
        print("-", suggestion)
else:
    print("\nYour password satisfies based on all given suggestions.")
