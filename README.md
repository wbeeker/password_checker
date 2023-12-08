# Final Project Report

* Student Name: William Beeker
* Github Username: wbeeker
* Semester: Fall 2023
* Course: 5001 Intensive Foundations of CS



## Description

This program takes in passwords from the user and the name of the application or service the password is used for. The program stores a list of passwords and service names, and can encrypt the list into a text file. The text file, and its key, can then be decrypted by the program.

I have trouble keeping track of all my passwords, but to keep a list of them together seems risky — if someone were to find that list, they'd have access to all of my passwords. Encrypting the list allows me to keep them all in one place, but also keeps them safe until I need to access them.


## Key Features

The encryption/decryption features are something I'm proud of. It was not easy to maintain dictionary formatting from the encrypted text file to the decrypted list. This took a lot of trial and error but I ended up getting the exact formatting I was hoping for.

## Guide

First, the program will ask you what you want to do:

<img src="https://github.com/wbeeker/password_checker/blob/main/Readme%20photos/screenshot.png" height="55" width="300">

Type 'help' for the program to display valid command options:

<img src="https://github.com/wbeeker/password_checker/blob/main/Readme%20photos/screenshot2.png" height="225" width="550">

Typing 'pw' will allow you to add a password and corresponding app or service name to the current dictionary. The program will then display the strength of the password and ask if you'd like to add it to the current dictionary or not:

<img src="https://github.com/wbeeker/password_checker/blob/main/Readme%20photos/Screen%20Shot%202023-12-03%20at%208.35.28%20AM.png" height="80" width="425">
<img src="https://github.com/wbeeker/password_checker/blob/main/Readme%20photos/Screen%20Shot%202023-12-03%20at%208.36.19%20AM.png" height="125" width="450">

Typing 'y' or 'yes' will add the password to the current list. Type 'current' to display the current list:

<img src="https://github.com/wbeeker/password_checker/blob/main/Readme%20photos/Screen%20Shot%202023-12-03%20at%208.37.17%20AM.png" height="100" width="400">

When you have your list of passwords ready to save, you can type 'encrypt' and the list will be encrypted based on a random key and saved in a text file in your working directory:

<img src="https://github.com/wbeeker/password_checker/blob/main/Readme%20photos/Screen%20Shot%202023-12-03%20at%208.38.36%20AM.png" height="70" width="525">
<img src="https://github.com/wbeeker/password_checker/blob/main/Readme%20photos/Screen%20Shot%202023-12-03%20at%208.39.26%20AM.png" height="115" width="450">

You can then decrypt the list by typing 'decrypt' into the program and entering the name of the file you'd like to decrypt along with its key:

<img src="https://github.com/wbeeker/password_checker/blob/main/Readme%20photos/Screen%20Shot%202023-12-03%20at%208.41.15%20AM.png" height="120" width="420">

By typing 'current' you'll see that the current list has been updated to include the decrypted passwords:

<img src="https://github.com/wbeeker/password_checker/blob/main/Readme%20photos/Screen%20Shot%202023-12-03%20at%208.41.56%20AM.png" height="175" width="400">

To end the program, simply type 'quit':

<img src="https://github.com/wbeeker/password_checker/blob/main/Readme%20photos/Screen%20Shot%202023-12-03%20at%208.42.47%20AM.png" height="50" width="525">


## Installation Instructions

To install, download password_checker.py, ecnrypter.py, and the common_pw_list.txt file. Open password_checker.py with your favorite IDE and hit run. Make sure to have all three files in the same directory.


## Code Review

Here is the function used to check the user_password against a list of 10 million common passwords (credit to Github user danielmiessler for this list). The function simply reads in the common password list and checks to see if the user_password matches any line of the common password list:

```python
def check_common(user_password):
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
```

Because the program relies on lots of user_input, the largest function is the main() function, which runs the while loop used to take in and interpret user commands. This is also where the current dictionary list is stored and updated:

```python
def main():
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
```

Here is the dictionary encrypter function. This takes in the current_dictionary as stored in the main() function above, converts the dictionary to a string (using json.dumps() to maintain formatting), and then encrypts the string using a randomly generated key string. The program then writes the encrypted string to a text file named encrypted_file.txt and writes the random key to a text file named key.txt:

```python
def dict_encrypt(current_dict: dict, key=RANDOM_KEY):
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
```

Here is the decryption function. This takes in the encrypted file and key file based on user input and decrypts the encrypted file based on the key file. The decrypted string from the encrypted file is then printed in dictionary format using json.loads(). The main() function also updates the current_list with the decrypted dictionary:

```python
def dict_decrypt():
    decrypted = ""
    filename = input("Enter filename to decrypt: ")
    key_filename = input("Enter key filename: ")
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
```

### Major Challenges

Coming up with a way to score the complexity of the user_password was a major challenge. For example, coming up with a password made entirely of symbols and numbers would probably be much harder for a human to guess than a password made up of 2 capital letters, 2 lowercase letters, 2 symbols, and 2 numbers. Yet, the latter will get a higher score in this program. There's a logic to password complexity than simply: does it meet certain requirements? A more advanced version of this program might be able to recognize words from an actual dictionary. The less resemblance the password has to dictionary words, the less likely it will be guessed by a human, probably. There's a lot more that could be taken into consideration regarding complexity than is used here.


## Example Runs

Here is what a full run looks like:

<img src="https://github.com/wbeeker/password_checker/blob/main/Readme%20photos/Screen%20Shot%202023-12-07%20at%207.39.42%20AM.png" height="700" width="500">

And here are the encrypted_file.txt and key.txt outputted by the run:

<img src="https://github.com/wbeeker/password_checker/blob/main/Readme%20photos/Screen%20Shot%202023-12-06%20at%208.22.51%20AM.png" height="100" width="450">
<img src="https://github.com/wbeeker/password_checker/blob/main/Readme%20photos/Screen%20Shot%202023-12-06%20at%208.22.54%20AM.png" height="100" width="450">


## Testing

I wrote unit tests for most of the functions in the password_checker program: [tests](https://github.com/wbeeker/password_checker/blob/main/test_password_checker.py)

I also have output files from the encrypter program: [test_encrypted_file](https://github.com/wbeeker/password_checker/blob/main/test_encrypted_file.txt) [test_key](https://github.com/wbeeker/password_checker/blob/main/test_key.txt)


Because the program relies heavily on user input, I simply had to use the program myself, trying lots of different inputs, doing my best to break the program.



## Missing Features / What's Next

I would've liked to have used a GUI. I have no experience with with GUI, but it would've made the program easier and nicer to use.

I also would've liked to utilize command line arguments. Using the command line is something I've struggled with this semester and it was something I failed to incorporate into this program.

As I mentioned above, I would've liked to explore more sophisticated ways to calculate the complexity of a password.


## Final Reflection

This has been a challenging, rewarding semester. My programming skills have developed quickly and I've learned more in such a short span of time than I thought was possible. I want to use the time between this semester and next to go back and gain a deeper understanding of some of the concepts of the course. I often was so focused on just getting things done that my only concern was: do I understand this concept or technique enough to use it in practice? Often, the answer to that question was yes, even if I didn't fully understand what was happening under the hood, or the 'why' and 'how' behind certain techniques. I also think I was a little too focused on grades, scoring, deadlines, etc. In the second half of the semester, I tried to simply focus on the learning and understanding parts, and let the grades/assignments  take care of themselves. This was a much better approach and I'll try to take that knowledge with me going forward.  
