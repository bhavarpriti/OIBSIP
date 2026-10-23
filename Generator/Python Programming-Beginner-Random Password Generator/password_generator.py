

import string
import secrets

print("===== RANDOM PASSWORD GENERATOR =====")

try:
    length = int(input("Enter password length (minimum 8): "))

    if length < 8:
        print("Error: Password length must be at least 8.")
    else:
        characters = string.ascii_letters + string.digits + string.punctuation
        password = "".join(
            secrets.choice(characters) for _ in range(length)
        )

        print("\nYour generated password is:", password)
        print("Password generated successfully!")

except ValueError:
    print("Error: Please enter a valid whole number.")
