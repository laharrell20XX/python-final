def process_inventory(unprocessed_inventory):
    '''(list of str) -> list of dict

    Returns a list of inventory items as a list of item dictionaries
    '''
    inventory_list = []
    for item in unprocessed_inventory:
        if item:
            item = item.strip().split(',')
            item_dict = dict(
                item_name=item[0],
                base_rental_price=int(item[1]),
                replacement_cost=int(item[2]),
                in_stock=int(item[3]),
                initial_stock=int(item[4]))
            inventory_list.append(item_dict)
    return inventory_list


def convert_inventory(inventory_list):
    '''(list of dict) -> list of str

    Returns a list of item dictionaries as a list of item strings
    '''
    unprocessed_inventory = []
    for item in inventory_list:
        item_str = f'{item["item_name"]},{item["base_rental_price"]},{item["replacement_cost"]},{item["in_stock"]},{item["initial_stock"]}\n'
        unprocessed_inventory.append(item_str)
    return unprocessed_inventory


def rent_item(item):
    '''(dict) -> NoneType

    decreases the in-stock number of the item being asked for by 1
    '''
    item['in_stock'] -= 1


def return_item(item):
    '''(dict) -> NoneType

    increases the in_stock number of the item being asked for by 1
    '''
    item['in_stock'] += 1


def add_item_to_cart(cart, item, choice):
    ''' (list, dict, str) -> list of lists

    Adds an item to the cart; can either be an item to rent or an item to return
    '''
    cart.append([item, choice])
    return cart


def check_full_stock(inventory):
    ''' (list of dict) -> bool

    Checks the inventory to see if the entire stock is full.
    '''
    full_stock = False
    for item in inventory:
        if item['in_stock'] == item['initial_stock']:
            full_stock += True
    return full_stock == len(inventory)