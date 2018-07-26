import core


def read_inventory(inventory_file):
    '''(file) -> list of str

    reads the inventory and returns it as a list with each line being a new item
    '''
    inventory_list = []
    with open(inventory_file) as file:
        for line in file.readlines():
            inventory_list.append(line)
    return inventory_list


def rewrite_inventory(inventory_file, inventory_list):
    '''(list of dict) -> file

    Takes the inventory_list and turns it back into its original file format
    '''
    with open(inventory_file, 'w') as file:
        for item in inventory_list:
            file.write(item)


def login(manifesto_file, username):
    ''' (file, str) -> NoneType, bool

    Checks to see if the provided username is in the file
    already otherwise it creates a new user
    '''
    with open(manifesto_file) as file:
        usernames = file.readlines()
    if usernames:  #checks if there is something in the file
        for name in usernames:
            if username == name.split(',')[0]:  #checks if the username exists
                return True  #stops iterations if the name is found
            new_user(manifesto_file, username)
            return False
    else:  #first customer gets added since there are no other names
        new_user(manifesto_file, username)
        return False


def new_user(manifesto_file, username):
    ''' (file, str) -> NoneType

    Adds the provided username to the manifesto_file
    '''
    with open(manifesto_file, 'a') as file:
        file.write(f'{username},(item)\n')