def check_dictionary(password):

    with open("data/common_passwords.txt") as f:

        common = f.read().splitlines()

    if password.lower() in common:
        return True

    return False