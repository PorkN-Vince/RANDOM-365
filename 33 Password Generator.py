
import string
import secrets

def generate_strong_passwords(length=16):
    if length < 4:
        raise ValueError(">4 digits")
    
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    guaranteed = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(digits),
        secrets.choice(special)
    ]

    pool = lowercase + uppercase + digits + special
    rest = [secrets.choice(pool) for _ in range(length - 4)]
    password_chars = guaranteed + rest
    secrets.SystemRandom().shuffle(password_chars)

    return "".join(password_chars)

print(generate_strong_passwords(20))