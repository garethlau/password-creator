from selenium import webdriver

import random

class Password():

    length = 0
    lowercase_status = 0
    uppercase_status = 0
    special_character_status = 0
    character_options_list = [0]
    special_character_list = ['!', '@', '#', '$', '%', '^', '&', '*', '?']

    def __init__(self, name):

        self.name = name

    @classmethod
    def set_length(cls, status):
        Password.length = status

    @classmethod
    def set_lowercase_status(cls, status):
        Password.lowercase_status = status

    @classmethod
    def set_uppercase_status(cls, status):
        Password.uppercase_status = status

    @classmethod
    def set_special_character_status(cls, status):
        Password.special_character_status = status

    @classmethod
    def create_character_options(cls, lowercase_status, uppercase_status, special_character_status):
        if lowercase_status == 'YES':
            Password.character_options_list.append(1)
            if uppercase_status == 'YES':
                Password.character_options_list.append(2)
                if special_character_status == 'YES':
                    Password.character_options_list.append(3)
        else:
            if uppercase_status == 'YES':
                Password.character_options_list.append(2)
                if special_character_status == 'YES':
                    Password.character_options_list.append(3)
            else:
                if special_character_status == 'YES':
                    Password.character_options_list.append(3)

#Prompt user for integer in allowed range
def get_int_sanitised(prompt, allow_range):
    while True:
        try:
            entry = int(input(prompt))
        except ValueError:
            print("That is not a valid entry.")
            continue
        if entry not in allow_range:
            print("Out of range.")
            continue
        else:
            return entry
        break

#Prompt user for string in available options
def get_string_sanitised(prompt, options):
    while True:
        entry = (input(prompt)).upper()
        if entry not in options:
            print("That is not a valid entry.")
            continue
        else:
            return entry
            break

#Default function
def random_integer():
    character = chr(random.randint(48, 57))
    return character

#Function 1
def random_lowercase():
    character = chr(random.randint(97, 122))
    return character

#Function 2
def random_uppercase():
    character = chr(random.randint(65, 90))
    return character

#Function 3
def random_special_character(special_character_list):
    character = random.choice(special_character_list)
    return character

def build_password(name):
    for i in range(0, Password.length):

        character_type = random.choice(Password.character_options_list)
        if character_type == 0:
            character = random_integer()
            name.append(character)
        elif character_type == 1:
            character = random_lowercase()
            name.append(character)
        elif character_type == 2:
            character = random_uppercase()
            name.append(character)
        else:
            character = random_special_character(Password.special_character_list)
            name.append(character)

    password = "".join(name)
    return password


if __name__=='__main__':

    number_of_passwords = get_int_sanitised("Number of passwords: ", range(0, 1000000000))  #number of passwords to be created

    #Set class variables
    Password.set_length(get_int_sanitised("Length: ", range(0,100)))
    Password.set_lowercase_status(get_string_sanitised("Lowercase (YES/NO): ", ['YES', 'NO']))
    Password.set_uppercase_status(get_string_sanitised("Uppercase (YES/NO): ", ['YES', 'NO']))
    Password.set_special_character_status(get_string_sanitised("Special characters (YES/NO): ", ['YES', 'NO']))
    Password.create_character_options(Password.lowercase_status, Password.uppercase_status, Password.special_character_status)

    #Create and write passwords to file
    file = open("passwords", "a")
    for i in range (0, number_of_passwords):
        pass_list = []
        pass_string = build_password(pass_list)
        file.write(pass_string + "\n")
    file.close()

    driver = webdriver.Chrome(r"C:\Users\garet\.PyCharmCE2018.2\chromedriver")
    driver.get('http://www.passwordmeter.com/')

    readfile = open('passwords', 'r')
    writefile = open('passwords,score', 'a')

    #Test passwords using: http://www.passwordmeter.com/
    for i in range(0, number_of_passwords):
        password = readfile.readline()

        input_box = driver.find_element_by_name('passwordPwd')  #find input box
        input_box.send_keys(password)  #write to input box

        score = driver.find_element_by_id('score').text
        writefile.write(password[:-2])
        writefile.write(',')
        writefile.write(score + '\n')
        print(password[:-2] + ': ' + score)
        input_box.clear()  #clear input box

    readfile.close()
    writefile.close()


