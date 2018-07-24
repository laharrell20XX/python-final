def read_inventory(inventory_file):
    '''(file) -> list of str

    reads the inventory and returns it as a list with each line being a new item
    '''
    with open(inventory_file) as file:
        inventory_list = file.readlines()
    return inventory_list
