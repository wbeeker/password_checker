"""
William Beeker
Fall 2023

Password checker program

Takes in password from client, checks password for complexity, and writes encrypted passwords
to a file. Also, can open file of encrypted passwords and decrypt them.

"""
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from encrypter import dict_encrypt, dict_decrypt

UPPERCASE = ascii_uppercase
LOWERCASE = ascii_lowercase
DIGITS = digits
SYMBOLS = punctuation

HELP_PROMPT = """Enter one of the following commands:
    pw - enter password and app or service
    current - prints current password dictionary
    encrypt - encrypts current password dictionary and writes to file
    decrypt - decrypts encrypted password dictionary
    remove - removes an item from the current password dictionary
    reset - clear current password dictionary
    help - displays command options
    quit - quits program
    """

WELCOME_PROMPT = "Welcome to Password Checker!"


def enter_password():
    """
    Take in password from client. Returns password with spaces removed.

    Args:
        None.

    Returns:
        user_password: str
    """
    user_password = str(input("Enter a password: "))
    if " " in user_password:
        print("Spaces have been removed. ")
    return user_password.replace(" ", "")


def enter_service():
    """
    Takes in app name or service name corresponding to password (e.g. Netflix, PayPal, etc.)

    Args:
         None.

    Returns:
        service: str
    """
    service = str(input("What app or service is this password for: "))
    return service


def counter_score(counter: int):
    """
    Returns score based on "counter" argument.

    Args:
        counter: int

    Returns:
        int
    """
    if counter >= 2:
        return 2
    elif counter == 1:
        return 1
    else:
        return 0


def check_uppercase(user_password: str):
    """
    Checks user_password for use of uppercase. Returns score using counter_score.
    """
    counter = 0
    for i in user_password:
        if i in UPPERCASE:
            counter += 1
    return counter_score(counter)


def check_lowercase(user_password):
    """
    Checks user_password for use of lowercase. Returns score.
    """
    counter = 0
    for i in user_password:
        if i in LOWERCASE:
            counter += 1
    if counter >= 2:
        return 1
    else:
        return 0


def check_digits(user_password):
    """
    Checks user_password for use of digits. Returns score using counter_score.
    """
    counter = 0
    for i in user_password:
        if i in DIGITS:
            counter += 1
    return counter_score(counter)


def check_symbols(user_password):
    """
    Checks user_password for use of symbols. Returns score using counter_score.
    """
    counter = 0
    for i in user_password:
        if i in SYMBOLS:
            counter += 1
    return counter_score(counter)


def check_length(user_password):
    """
    Checks user_password for length and returns a corresponding score.

    Args:
        user_password: str

    Returns:
        counter: int
    """
    counter = 0
    if len(user_password) >= 10:
        counter += 1
    if len(user_password) >= 15:
        counter += 1
    if len(user_password) >= 20:
        counter += 1
    return counter


def check_common(user_password):
    """
    Checks user_password against a list of one million common passwords.

    Args:
        user_password: str

    Returns:
        True if password is found in common list
    """
    try:
        with open("common_pw_list.txt", "r") as file:
            common_list = file.read().splitlines()
        if user_password in common_list:
            print("Password found in common list.")
            return True
    except FileNotFoundError:
        print("common_pw_list.txt not found!")
    except IOError as io:
        print(io)


def score_total(user_password):
    """
    Checks user_password for various character requirements and against a list of common passwords,
    and returns a corresponding score of the password's strength.

    Args:
        user_password: str

    Returns:
        score: int
    """
    if check_common(user_password) is True:
        return 0
    else:
        score = 0
        score += check_uppercase(user_password)
        score += check_lowercase(user_password)
        score += check_digits(user_password)
        score += check_symbols(user_password)
        score += check_length(user_password)
        return score


def score_print(score: int):
    """
    Takes in score integer and prints the score out of 10 and a message about the password's strength.

    Args:
        score: int

    Returns:
        Nothing.
    """
    if score < 3:
        print(f"{score} / 10 — Password is very weak!")
    elif 3 <= score <= 5:
        print(f"{score} / 10 — Password is pretty weak.")
    elif 5 < score < 7:
        print(f"{score} / 10 — Password is ok.")
    elif 7 <= score <= 9:
        print(f"{score} / 10 — Password is strong.")
    elif score == 10:
        print(f"{score} / 10 — Password is very strong!")


def get_command():
    """
    Prompts user for command and returns command:

        pw - enter password and app or service
        current - prints current password dictionary
        encrypt - encrypts current password dictionary and writes to file
        decrypt - decrypts encrypted password dictionary
        remove - removes an item from the current password dictionary
        reset - clear current password dictionary
        help - displays command options
        quit - quits program

    Args:
        None.

    Returns:
        command: str
    """
    command = input("What would you like to do? ").strip().casefold()
    return command


def score_run(user_password: str):
    """
    Runs score_total and score_print to calculate and
    display score of password strength.

    Args:
        user_password: str

    Returns:
        Nothing.
    """
    score = score_total(user_password)
    score_print(score)


def main():
    """
    Main driver for the program.

    Prints welcome message, gets command from the client,
    and runs while the command is not "quit."
   """
    print(WELCOME_PROMPT)
    current_dict = {}
    loop = True
    while loop:
        option = get_command()
        if option == "pw":
            service = enter_service()
            user_password = enter_password()
            score_run(user_password)
            add = input("Would you like to add password to list? (y/n) ").strip().casefold()
            if add == "y" or add == "yes":
                current_dict[service] = user_password
                print("Password has been added to current list.")
        elif option == "current":
            if current_dict == {}:
                print("List is empty.")
            else:
                for key, value in current_dict.items():
                    print("\t", key + ":", value)
        elif option == "encrypt":
            dict_encrypt(current_dict)
        elif option == "decrypt":
            current_dict = dict_decrypt()
        elif option == "remove":
            key_remove = str(input("Which app or service password would you like to remove: ")).strip()
            if key_remove in current_dict:
                del current_dict[key_remove]
                print(f"{key_remove} password has been removed from list.")
            else:
                print(f"{key_remove} not found in list.")
        elif option == "reset":
            current_dict = {}
            print("List has been cleared.")
        elif option == "help":
            print(HELP_PROMPT)
        elif option == "quit":
            print("Thanks for using password checker! Closing program...goodbye!")
            break
        else:
            print("Invalid command.", "\n", HELP_PROMPT)


if __name__ == "__main__":
    main()
