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


def transaction_tax(cart):
    ''' (list of lists [dict, str]) -> float

    Finds the tax of the rented items in the cart
    '''
    grand_total = 0
    for item in cart:
        if 'rent' in item:
            grand_total += item[0]['base_rental_price']
    return float(f'{grand_total * .07:.2f}')


def checkout(cart):
    ''' (list of lists [dict, str]) -> float

    Items in the cart are totalled and the total and tax is returned
    '''
    grand_total = 0
    replacement_deposit = 0
    for item in cart:
        if 'rent' in item:
            grand_total += item[0]['base_rental_price']
            replacement_deposit += (item[0]['replacement_cost'] * .1)
        if 'return' in item:
            replacement_deposit -= item[0]['replacement_cost'] * .1
    return float(f'{(grand_total * 1.07) + replacement_deposit:.2f}')


def check_full_stock(inventory):
    ''' (list of dict) -> bool

    Checks the inventory to see if the entire stock is full.
    '''
    full_stock = False
    for item in inventory:
        if item['in_stock'] == item['initial_stock']:
            full_stock += True
    return full_stock == len(inventory)


def can_return(customer, customer_manifesto):
    ''' (str, list of dict) -> bool,list, None

    checks the manifesto to see if the person has rented anything already
    '''
    for user in customer_manifesto:
        for username in user.keys():  #iterates over each username
            if customer == username:  #checks to see who the user is in relation to the manifesto
                if list(user[username].strip('()')
                        ):  #checks to see if they had rented something before
                    return True
                else:
                    return False


def get_rented_items(customer, customer_manifesto):
    ''' (str, list of dict) -> list

    gets the list of items that have been rented by the customer
    '''
    for user in customer_manifesto:
        for username in user.keys():
            if customer == username:
                rented_items = user[username].strip('()').split(',')
                return rented_items