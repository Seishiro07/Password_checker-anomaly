"""
password_checker.py - Password Strength Checker (beginner project)

Checks length, uppercase, lowercase, numbers, special characters,
and a few common-password mistakes. Rates it Weak / Medium / Strong
and gives suggestions.

Usage:  python password_checker.py
"""
import getpass
import string

# A tiny list of very common passwords (real lists have millions)
COMMON_PASSWORDS = {
    "password", "123456", "12345678", "qwerty", "abc123", "letmein",
    "admin", "welcome", "iloveyou", "monkey", "dragon", "password1",
    "111111", "123123", "football", "login",
}


def check_password(password):
    score = 0
    tips = []

    # Length
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
        tips.append("Make it 12+ characters for better security.")
    else:
        tips.append("Too short! Use at least 8 characters (12+ is better).")

    # Character types
    if any(c.islower() for c in password):
        score += 1
    else:
        tips.append("Add lowercase letters.")

    if any(c.isupper() for c in password):
        score += 1
    else:
        tips.append("Add uppercase letters.")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        tips.append("Add numbers.")

    if any(c in string.punctuation for c in password):
        score += 1
    else:
        tips.append("Add special characters like ! @ # $ %.")

    # Common mistakes
    if password.lower() in COMMON_PASSWORDS:
        score = 0
        tips.append("This is a very common password. Attackers try these first!")

    if len(set(password)) <= len(password) // 2:
        score -= 1
        tips.append("Too many repeated characters (like 'aaaa1111').")

    sequences = ["1234", "abcd", "qwer", "0000"]
    if any(seq in password.lower() for seq in sequences):
        score -= 1
        tips.append("Avoid simple sequences like 1234 or abcd.")

    # Classification (max score is 6)
    if score <= 2:
        rating = "WEAK"
    elif score <= 4:
        rating = "MEDIUM"
    else:
        rating = "STRONG"

    return rating, max(score, 0), tips


def main():
    print("=== Password Strength Checker ===")
    print("(Your typing is hidden. Type 'quit' to exit.)\n")
    while True:
        password = getpass.getpass("Enter a password to check: ")
        if password.lower() == "quit":
            print("Bye!")
            break
        if not password:
            print("Please enter something.\n")
            continue

        rating, score, tips = check_password(password)
        print(f"\nStrength: {rating}  (score {score}/6)")
        if tips:
            print("Suggestions:")
            for t in tips:
                print(f"  - {t}")
        else:
            print("Great password! No suggestions.")
        print()


if __name__ == "__main__":
    main()
