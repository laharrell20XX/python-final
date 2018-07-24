import core


def read_inventory(inventory_file):
    '''(file) -> list of str

    reads the inventory and returns it as a list with each line being a new item
    '''
    with open(inventory_file) as file:
        inventory_list = file.readlines()
    return inventory_list


def rewrite_inventory(inventory_file, inventory_list):
    '''(list of dict) -> file

    Takes the inventory_list and turns it back into its original file format
    '''
    with open(inventory_file, 'w') as file:
        for item in inventory_list:
            file.write(item)