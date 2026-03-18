import random
import string

def generate_secure_password(length=14):

    chars = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(chars) for _ in range(length))

    return password