import core
from datetime import datetime


def read_inventory(inventory_file):
    '''(file) -> list of str

    reads the inventory and returns it as a list with each line being a new item
    '''
    inventory_list = []
    with open(inventory_file) as file:
        for line in file.readlines():
            inventory_list.append(line)
    return inventory_list


def rewrite_inventory(inventory_file, inventory):
    '''(file, list of dict) -> NoneType

    Takes the inventory_list and turns it back into its original file format
    '''
    with open(inventory_file, 'w') as file:
        for item in inventory:
            file.write(
                f"{item['item_name']},{item['base_rental_price']},{item['replacement_cost']},{item['in_stock']},{item['initial_stock']}\n"
            )


def update_history(history_file, customer, total):
    ''' (file, str, float) -> NoneType

    Updates the transaction history in for: customer, timestamp, total
    '''
    with open(history_file, 'a') as file:
        file.write(
            f"{customer}, {datetime.now().strftime('%m/%d/%y @ %I:%M:%S %p')}, ${total}"
        )


def login(manifesto_file, username):
    ''' (file, str) -> NoneType, bool

    Checks to see if the provided username is in the file
    '''
    with open(manifesto_file) as file:
        list_of_usernames = file.readlines()
    if list_of_usernames:  #checks if there are any customers at all
        for name in list_of_usernames:
            if username == name.split(', ')[0]:  #checks if the username exists
                return True  #stops iterations if the name is found
            return False
    else:
        return False


def new_user(manifesto_file, username):
    ''' (file, str) -> NoneType

    Adds the provided username to the manifesto_file
    '''
    with open(manifesto_file, 'a') as file:
        file.write(f'{username}, ()\n')


def read_manifesto(manifesto_file):
    ''' (file) -> list of str

    Reads the manifesto_file and returns
    what was read as data to be further processed
    '''
    with open(manifesto_file, 'r') as file:
        return file.readlines()


def process_user_items(list_of_usernames):
    ''' (list of str) -> dict

    takes the user and any items that they have rented and turns it into a dictionary
    '''
    list_of_users = []
    for user in list_of_usernames:
        user = user.strip().split(', ')
        username = user[0]
        rented_items = user[1].strip('()').split(',')
        user_dict = dict([[username, rented_items]])
        list_of_users.append(user_dict)
    return list_of_users


def rewrite_manifesto_file(manifesto_file, customer_manifesto):
    ''' (file, list) -> file
    
    rewrites the manifesto_file with any changes that occurred after a transaction.
    '''
    user_list = []
    for user in customer_manifesto:
        for username in user.keys():
            user_list.append(f"{username}, ({(',').join(user[username])})")
    with open('manifesto.txt', 'w') as file:
        file.write(('\n').join(user_list))
