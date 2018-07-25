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
