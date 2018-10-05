import random
import _csv
import csv

character_options_list = [0]
special_character_list = ['!', '@', '#', '$', '%', '^', '&', '*', '?']
password = []

lowercase_status = []
uppercase_status = []
special_character_status = []

def get_int_sanitised(prompt, range):
    while True:
        try:
            entry = int(input(prompt))
        except ValueError:
            print("That is not a valid entry.")
            continue
        if entry not in range:
            print("Out of range!.")
            continue
        else:
            return entry
            break

def get_string_sanitised(prompt, options):
    while True:
        entry = (input(prompt)).upper()
        if entry not in options:
            print("That is not a valid entry.")
            continue
        else:
            return entry
            break

def create_character_options(lowercase_status, uppcase_status, special_character_status):
    if lowercase_status == 'YES':
        character_options_list.append(1)
        if uppcase_status == 'YES':
            character_options_list.append(2)
            if special_character_status == 'YES':
                character_options_list.append(3)
    else:
        if uppercase_status == 'YES':
            character_options_list.append(2)
            if special_character_status == 'YES':
                character_options_list.append(3)
        else:
            if special_character_status == 'YES':
                character_options_list.append(3)


def random_integer(): #default
    character = chr(random.randint(48, 57))
    return character

def random_lowercase(): #function 1
    character = chr(random.randint(97, 122))
    return character

def random_uppercase(): #function 2
    character = chr(random.randint(65, 90))
    return character

def random_special_character(): #function 3
    character = random.choice(special_character_list)
    return character

def build_password(length, character_options):
    for i in range(0, length):
        character_type = random.choice(character_options)
        if character_type == 0:
            character = random_integer()
            password.append(character)
        elif character_type == 1:
            character = random_lowercase()
            password.append(character)
        elif character_type == 2:
            character = random_uppercase()
            password.append(character)
        else:
            character = random_special_character()
            password.append(character)
    return password

length = get_int_sanitised("How long do you want your new password to be? Enter a number: ", range(0,100))
lowercase_status = (get_string_sanitised("Do you want your password to include lowercase letters? Type YES or NO: ", ['YES', 'NO'])).upper()
uppercase_status = (get_string_sanitised("Do you want your password to include uppcase letters? Type YES or NO: ", ['YES', 'NO'])).upper()
special_character_status = (get_string_sanitised("Do you want your password to include special characters? Type YES or NO: ", ['YES', 'NO'])).upper()

create_character_options(lowercase_status, uppercase_status, special_character_status)

password = "".join(build_password(length, character_options_list))
print("Your new password is: " + password)