#-----------------------------------------------------------------------------
# Title: User-service matcher
# Name: Drew McGregor
# Class: CS30
# Assignment: Capstone Coding Project
# Version: 0.4
#-----------------------------------------------------------------------------
'''
   This is an interactable database that allows a user to input 
   either services or users. The database can then search 
   itself to find services that best match a users needs.
'''
#-----------------------------------------------------------------------------
#-Imports and Global Variables------------------------------------------------
from tabulate import tabulate
import math as m
import services as s
import user as u
import service_objects
import user_objects
current_user = None
start_msg = ('This will match a user to services that fit their preferences ' 
+ 'and location. All users and services are saved across sessions.')
#-Functions ------------------------------------------------------------------
def get_input_type(type_, msg):
    '''Gets an input a verifies that it can be converted to type_
    returns type_(input)
    msg = message printed to user
    '''
    while True:
        user_input = input(msg)
        try:
            type_(user_input)
            return type_(user_input)
        except:
            print(f'Please input a {str(type_)[8:-2]}')
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
        return get_YesNo(msg)


def get_choice(valid_inputs, msg, error_msg):
    ''' asks user question until a valid input is given, presenting error
    msg on bad input
    valid_inputs = list of valid items
    msg = message given to user on run
    error_msg = msg on bad input
    '''
    choice = input(msg).lower()
    if choice not in valid_inputs:
        print(error_msg)
        choice = get_choice(valid_inputs, msg, error_msg)
    return choice


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
    '''Gets required info to create a service from the user, then
    creates the service if not already in the system.
    '''
    taken_names = [service.name.lower() for service in s.master_service_list]
    name = get_input_type(str, 'What is your name? ')
    while name.lower() in taken_names:
        name = get_input_type(str, f'It appears that the name {name} is '
                              + 'taken, please use a different one: ')
    xpos = get_input_type(float, 'Enter your x coordinate: ')
    zpos = get_input_type(float, 'Enter your z coordinate: ')
    products = get_input_type(str, "Enter what products you provide(product1"
                              + ", product2, etc): ").replace('"', '')
    products = products.replace("'", '')
    products = products.split(', ')
    phone_number = get_input_type(int, 'Enter your phone_number (no digit '
                                + 'separators, such as "-" or "."): ')
    tags = []
    if get_YesNo("Is there a general category of items you provide?"
                 + "(yes/no)"):
        tags = get_input_type(str, "Enter what categories you provide(cate"
                            + "gory1, category2, etc): ").replace('"', '')
        tags = tags.replace("'", '')
        tags = tags.split(', ')
    # Verification that submitted info is correct.
    print(tabulate([[name], 
            [f'Location : ({xpos}, {zpos})'], 
            ['Services: ' + str(', '.join(map(str, products)))], 
            [f'Phone Number: {phone_number}'], 
            ['Tags: ' + str(', '.join(map(str, tags)))]]))
    if not get_YesNo('is this the correct information? (Yes/No)'):
        if get_YesNo('do you still want to create a service?'):
            create_service()
        return None
    globals()[name] = s.Service(name, xpos, zpos, products, phone_number, 
                                tags)
    # Remove newly created object if it's already in master_list.
    for service in s.master_service_list[:-1]:
        if globals()[name].summary == service.summary:
            del globals()[name]
            s.master_service_list.pop(-1)
            break
    try:
        globals()[name].save()
        print(globals()[name])
    except KeyError:
        print("\nIt appears you're already in the system.")


def create_user():
    '''Gets required info to create a user from the user, then
    creates the user if not already in the system.
    '''
    taken_names = [user.name.lower() for user in u.master_user_list]
    name = get_input_type(str, 'What is your name? ')
    while name.lower() in taken_names:
        name = get_input_type(str, f'It appears that the name {name} is '
                              + 'taken, please use a different one: ')
    xpos = get_input_type(float, 'Enter your x coordinate: ')
    zpos = get_input_type(float, 'Enter your z coordinate: ')
    needs = get_input_type(str, "Enter what products you're looking "
                           + "for: ").replace('"', '')
    needs = needs.replace("'", '')
    needs = needs.split(', ')
    phone_number = get_input_type(int, 'Enter your phone_number (no '
                                  + 'digit separators, such as "-" or "."): ')
    tags = []
    if get_YesNo("Is there a general category of items you're looking for? "
                 + "(yes/no)"):
        options = s.existing_tags.copy()
        options.append('Exit Menu')
        while True:
            new_tag = offer_options(options, "Choose a tag from the options "
                                    + "or choose cancel after you've "
                                    + "selected all relevant tags. ", 'error')
            if new_tag == 'Exit Menu':
                break
            else:
                tags.append(new_tag)
                options.remove(new_tag)
    # Verification of submitted info.
    print(tabulate([[name], 
        [f'Location : ({xpos}, {zpos})'], 
        ['Needs: ' + str(', '.join(map(str, needs)))], 
        [f'Phone Number: {phone_number}'], 
        ['Tags: ' + str(', '.join(map(str, tags)))]]))
    if not get_YesNo('is this the correct information? (Yes/No)'):
        if get_YesNo('do you still want to create a new user?'):
            create_user()
        return None
    globals()[name] = u.User(name, xpos, zpos, needs, phone_number, tags)
    # Remove newly created object if it's already in master_list
    for user in u.master_user_list[:-1]:
        if globals()[name].summary == user.summary:
            del globals()[name]
            u.master_user_list.pop(-1)
            break
    try:
        globals()[name].save()
        print(globals()[name])
    except KeyError:
        print("\nIt appears you're already in the system.")


def change_current_user(name):
    '''Changes current_user to name if name is in the system'''
    global current_user
    for user in u.master_user_list:
        if user.name.lower() == name.lower():
            current_user = user
            print(current_user)
            return None
    print("That user doesn't seem to exist.")
#-Main -----------------------------------------------------------------------
while True:
    user_options = ['Change current user', 'Get relevant services',
                    'Create a user', 'Create a service', 'Quit']
    choice = offer_options(user_options, 
                 'What would you like to do? ', 
                 "That's not an option, please try again.")
    if choice == user_options[0]:
        new_user_name = get_input_type(str, 'Enter your name: ')
        change_current_user(new_user_name)
    elif choice == user_options[1]:
        while current_user == None:
            print('User not selected')
            new_user_name = get_input_type(str, 'Enter your name: ')
            change_current_user(new_user_name)
        current_user.get_services()
    elif choice == user_options[2]:
        create_user()
    elif choice == user_options[3]:
        create_service()
    elif choice == user_options[4]:
        if get_YesNo('Are you sure you want to quit?'):
            break
        else:
            pass
