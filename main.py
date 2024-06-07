#-----------------------------------------------------------------------------
# Title: User-service matcher
# Name: Drew McGregor
# Class: CS30
# Assignment: Capstone Coding Project
# Version: 0.3
#-----------------------------------------------------------------------------
'''
   Here is the headers docString 
   this is where you explain what the program does
'''
#-----------------------------------------------------------------------------
#-Imports and Global Variables------------------------------------------------
import math as m
import services as s
import user as u
import Users
import Services
current_user = None
#-Functions ------------------------------------------------------------------
def get_input_type(type_, msg):
    while True:
        user_input = input(msg)
        try:
            type_(user_input)
            return type_(user_input)
        except:
            print(f'Please input a {type_}')
            return get_input_type(type_, msg)


def get_YesNo(msg):
    '''Asks user yes no question, outputs true for yes, false for no,
    checks formatting.
    msg = yes/no question'''
    answer = input(msg).lower()
    if answer == 'yes' or answer == 'y':
        return True
    elif answer == 'no' or answer == 'n':
        return False
    else:
        print("Please input either 'yes' or 'no'")
        get_YesNo(msg)


def get_choice(valid_inputs, msg, error_msg):
    ''' asks user question until a valid input is given, presenting error
    msg on bad input
    valid_inputs = list of valid items
    msg = message given to user on run
    error_msg = msg on bad input
    '''
    letter = input(msg).lower()
    if letter not in valid_inputs:
        print(error_msg)
        get_choice(valid_inputs, msg, error_msg)
    return letter


def offer_options(original_options, msg, error_msg):
    """Assign and print numerical values to items in a list"""
    print('\n')
    for item in original_options:
        print(f"{original_options.index(item)+1}. {item}")
    numbers = [str(number+1) for number in range(len(original_options))]
    full_options = original_options.copy()
    full_options.extend(numbers)
    choice = get_choice(full_options, msg, error_msg)
    if choice not in full_options:
        print(error_msg)
        choice = get_choice(full_options, msg, error_msg)
    elif choice.isnumeric():
        choice = full_options[int(choice)-1]
    return choice

def create_service():
    name = get_input_type(str, 'What is your name? ')
    xpos = get_input_type(float, 'Enter your xpos: ')
    zpos = get_input_type(float, 'Enter your zpos: ')
    needs = get_input_type(str, "Enter what products you provide: ").split(', ')
    phone_number = input('Enter your phone_number: ')
    tags = []
    if get_YesNo("Is there a general category of items you provide?(yes/no)"):
        tags = get_input_type(str, "Enter what categories you provide: ").split(', ')
    globals()[name] = s.Service(name, xpos, zpos, needs, phone_number, tags)
    for service in s.master_service_list[:-1]:
        if globals()[name].summary == service.summary:
            del globals()[name]
            s.master_service_list.pop(-1)
            print("It appears you're already in the system.")
            break
    print(globals()[name])

def create_user():
    name = get_input_type(str, 'What is your name? ')
    xpos = get_input_type(float, 'Enter your xpos: ')
    zpos = get_input_type(float, 'Enter your zpos: ')
    needs = get_input_type(str, "Enter what products you're looking for: \
    ").split(', ')
    phone_number = input('Enter your phone_number: ')
    tags = []
    if get_YesNo("Is there a general category of items you're looking for? \
                (yes/no)"):
        while True:
            options = s.existing_tags.copy()
            options.append('cancel')
            new_tag = offer_options(options, 'message', 'error')
            del options
            if new_tag == 'cancel':
                break
            else:
                tags.append(new_tag)
    globals()[name] = u.User(name, xpos, zpos, needs, phone_number, tags)
    for user in u.master_user_list[:-1]:
        if globals()[name].summary == user.summary:
            del globals()[name]
            u.master_user_list.pop(-1)

def change_current_user(name):
    global current_user
    for user in u.master_user_list:
        if user.name == name.lower():
            current_user = user
            print(current_user)
            return None
    print("That user doesn't seem to exist.")
#-Main -----------------------------------------------------------------------
print(u.master_user_list)
print(s.master_service_list)
while True:
    user_options = ['Change current user', 'Get relevant services',
                    'create user', 'create service']
    choice = offer_options(user_options, 
                 'What would you like to do?', 
                 "That's not an option, please try again")
    if choice == user_options[0]:
        new_user_name = get_input_type(str, 'Enter your name: ')
        change_current_user(new_user_name)
    elif choice == user_options[1]:
        if current_user == None:
            print('User not selected')
            new_user_name = get_input_type(str, 'Enter your name: ')
            change_current_user(new_user_name)
        else:
            current_user.get_services()
    elif choice == user_options[2]:
        create_user()
    elif choice == user_options[3]:
        create_service()