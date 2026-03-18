import hashlib

def sha256_hash(password):

    hash_value = hashlib.sha256(password.encode()).hexdigest()

    return hash_value