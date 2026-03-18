from entropy import calculate_entropy
from brute_force import brute_force_time
from dictionary_attack import check_dictionary
from hashing import sha256_hash
from password_generator import generate_secure_password


password = input("Enter password: ")

entropy, charset = calculate_entropy(password)

print("\nEntropy:", entropy)

dict_check = check_dictionary(password)

if dict_check:
    print("Password found in dictionary list")

times = brute_force_time(len(password), charset)

print("\nBrute Force Simulation:")

for attack, seconds in times.items():
    print(attack, ":", seconds, "seconds")

print("\nSHA256 Hash:")
print(sha256_hash(password))

print("\nSuggested strong password:")
print(generate_secure_password())