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

#-Functions ------------------------------------------------------------------
def get_input_type(type_, msg):
    while True:
        user_input = input(msg)
        try:
            type_(user_input)
            return type_(user_input)
        except:
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

def create_user():
    name = get_input_type(str, 'What is your name? ')
    xpos = get_input_type(float, 'Enter your xpos: ')
    zpos = get_input_type(float, 'Enter your zpos: ')
    needs = get_input_type(str, "Enter what products you're looking for: ").split(', ')
    phone_number = input('Enter your phone_number: ')
    tags = []
    if get_YesNo("Is there a general category of items you're looking for? (yes/no)"):
        while True:
            options = s.existing_tags.copy()
            options.append('cancel')
            new_tag = offer_options(options, 'message', 'error')
            del options
            if new_tag == 'cancel':
                break
            else:
                tags.append(new_tag)
    vars()[name] = u.User(name, xpos, zpos, needs, phone_number, tags)
    vars()[name].save()


#-Main -----------------------------------------------------------------------