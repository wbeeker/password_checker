"""
William Beeker
Fall 2023

Encrypts and decrypts file of passwords.
"""

import json
from string import digits, ascii_letters
from random import sample

ALL_LETTERS_DIGITS = digits + ascii_letters
RANDOM_KEY = "".join(sample(list(ALL_LETTERS_DIGITS), len(ALL_LETTERS_DIGITS)))


def dict_encrypt(current_dict: dict, key=RANDOM_KEY):
    """Coverts a dictionary to a string, encrypts the string with the key
    needed to decipher the message, and writes the encrypted to a file. Key is written to separate file.
    If no key provided, defaults to RANDOM_KEY.

    Args:
        current_dict: dictionary
        key: str, defaults to RANDOM_KEY

    Return:
        Nothing
    """
    string_dict = json.dumps(current_dict)
    encrypted = ""
    for x in string_dict:
        if x in ALL_LETTERS_DIGITS:
            encrypted += key[(ALL_LETTERS_DIGITS.find(x))]
        else:
            encrypted += x
    with open("encrypted_file.txt", "w") as file:
        file.write(encrypted)
    with open("key.txt", "w") as key_file:
        key_file.write(key)
    print("List has been encrypted as encrypted_file.txt. Key is key.txt.")


def dict_decrypt():
    """Takes in filename and key_filename from user and decrypts an encrypted message using a provided key
    and prints the decrypted message
    to the screen.

    Args:
        Nothing.

    Returns:
        Nothing
    """
    decrypted = ""
    filename = str(input("Enter filename to decrypt: "))
    key_filename = str(input("Enter key filename: "))
    try:
        with open(filename, "r") as encrypted_file:
            encrypted_lines = encrypted_file.read()
    except FileNotFoundError:
        print(f"Encrypted file {filename} not found!")
        return dict_decrypt()
    except IOError as io:
        print(io)
        return dict_decrypt()
    try:
        with open(key_filename, "r") as key_file:
            key = key_file.read()
    except FileNotFoundError:
        print(f"Key file {key_filename} not found!")
        return dict_decrypt()
    except IOError as io:
        print(io)
        return dict_decrypt()
    for x in encrypted_lines:
        if x in key:
            decrypted += ALL_LETTERS_DIGITS[(key.find(x))]
        else:
            decrypted += x
    new = json.loads(decrypted)
    for key, value in new.items():
        print("\t", key + ":", value)
    return new
