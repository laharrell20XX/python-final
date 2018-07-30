import core, disk


def greeting():
    ''' -> NoneType
    Greets the user
    '''
    print('Hi!  Welcome to the Costumes n Props rental agency\n\n')


def show_inventory(inventory, identity):
    ''' (list of dict) -> NoneType

    Shows the inventory in a user friendly way depending on the identity of the user
    '''
    inventory_str = ''
    if identity == 'c':  #what customer sees
        for item in inventory:
            if item['in_stock']:
                inventory_str += f'{item["item_name"]}: ${item["base_rental_price"]:.2f} to rent (${item["replacement_cost"]:.2f} to replace), {item["in_stock"]} left in stock\n'
        print(inventory_str)
    if identity == 'e':  #what employee sees
        for item in inventory:
            inventory_str += f'{item["item_name"]}: ${item["base_rental_price"]:.2f} to rent (${item["replacement_cost"]:.2f} to replace), {item["in_stock"]} left in stock (initial stock: {item["initial_stock"]})\n'
        print(inventory_str)


def rent_or_return():
    ''' (str) -> str

    Asks customer whether they want to rent or return 
    '''
    while True:
        choice = input(
            "Hi!  Type 'rent' to rent an item, or type 'return' to return an item.\n>>> "
        ).lower()
        if choice == 'rent':
            return choice
        elif choice == 'return':
            return choice
        else:
            print('Invalid option')


def employee_or_customer():
    ''' (str) -> str

    Asks user whether they are an employee or a customer and returns their identity
    '''
    while True:
        identity = input(
            "Are you an [e]mployee or a [c]ustomer? (type 'leave' to exit the application)\n>>> "
        ).lower()
        if identity == 'e':
            return 'e'
        elif identity == 'c':
            return 'c'
        elif identity == 'leave':
            print('Have a nice day!')
            quit()
        else:
            print("The identity you entered is not valid.  Please try again")


def user_login():
    ''' self -> list of dict

    Asks the user for their username and checks it against the manifesto;
    a new user is created if they don't exist in the file
    '''
    while True:
        username = input('Welcome! Please enter your name to continue.\n>>> ')
        if username.strip():
            if disk.login('customer_manifesto.txt', username):
                print(f'Welcome back {username}!')
                return username
            else:
                disk.new_user('customer_manifesto.txt', username)
                print(f'Took you long enough to find us {username}! Welcome!')
                return username
        print('Sorry, you must enter a username')


def which_item(inventory, mode, customer, customer_manifesto):
    ''' (str, str) -> dict

    Asks user which item they want and returns that item as a dictionary
    '''
    while True:
        if mode == 'rent':
            return rent_mode(inventory)
        if mode == 'return':
            return return_mode(inventory, customer, customer_manifesto)


def rent_mode(inventory):
    ''' (list of dict, str) -> dict

    checks if the item is in the inventory before it is rented
    '''
    while True:
        show_inventory(inventory, 'c')
        item_choice = input(
            '\nType the name of the item you want to rent (case sensitive)\n>>> '
        )
        for item in inventory:
            if item_choice == item['item_name'] and item['in_stock']:
                return item
        print(
            'Sorry, either we do not have that item or it is out of stock. Please try again\n'
        )


def return_mode(inventory, customer, customer_manifesto):
    ''' (list of dict, str, list of dict) -> item, None

    Returns the item that the user wants to return
    '''
    rented_items = core.get_rented_items(customer, customer_manifesto)
    while True:
        if core.can_return(customer, customer_manifesto):
            show_inventory(inventory, 'c')
            print(f'You have {len(rented_items)} item(s) you have rented:')
            print('', *rented_items, sep='\n\t', end='\n')
            item_choice = input(
                '\nType the name of the item you want to return (case sensitive)\n>>> '
            )
            for item in inventory:
                if item_choice == item['item_name'] and (
                        item_choice in rented_items):
                    return item  #returns any item choice that is first entered
            print('Sorry, that item has not been rented by you.\n')
        else:
            print(
                "You haven't rented anything yet.  Redirecting you to the login screen..."
            )
            return None


def show_receipt(cart, customer):
    ''' (list of lists [dict, str], str) -> NoneType

    prints out the receipt to the user; negative number means money was refunded
    '''
    grand_total = core.checkout(cart)
    grand_tax = core.transaction_tax(cart)
    print(f'\t{customer}')
    print('Receipt'.center(30) + '\n')
    print('*' * 40)
    for item in cart:
        if 'rent' in item:
            print(
                '''\t{:<10}{:>10.2f}{:>8}
\t{:<10}{:>18.2f}'''.format(item[0]['item_name'], item[0]['base_rental_cost'],
                            item[1]), '(Replacement Cost)',
                item[0]['replacement_cost'] * .1)
        if 'return' in item:
            print('''\t{:<10}{:>10.2f}{:>8}'''.format(
                item[0]['item_name'], -item[0]['replacement_cost'] * .1,
                item[1]))
    print('*' * 40)
    print('''\t{:<10}{:>18.2f}
\t{:<10}{:>18.2f}'''
          .format('Tax', grand_tax, 'Total',
                  grand_total))  #prints tax total then prints grand total


def main():
    greeting()
    inventory = core.process_inventory(disk.read_inventory('inventory.txt'))
    identity = employee_or_customer()
    cart = []
    while True:
        if identity == 'c':  #customer path
            username = user_login()
            choice = rent_or_return()
            customer_manifesto = disk.process_user_items(
                disk.read_manifesto('customer_manifesto.txt'))
            if choice == 'rent':
                item_choice = which_item(inventory, 'rent', username,
                                         customer_manifesto)
                core.rent_item(item_choice)
                print(
                    f'1 {item_choice["item_name"]} has been added to your cart.'
                )
                core.add_item_to_cart(cart, item_choice, choice)
            if choice == 'return':
                item_choice = which_item(inventory, 'return', username,
                                         customer_manifesto)
                if item_choice:
                    core.return_item(item_choice)
                    print(
                        f'1 {item_choice["item_name"]} has been returned.  Please checkout to get your deposit back.'
                    )
                    core.add_item_to_cart(cart, item, choice)
                else:
                    continue
            if choice == 'checkout':  #next on the agenda
                show_receipt(cart, username)
                new_customer_manifesto = core.change_rented_items(
                    cart, username, customer_manifesto)
                disk.rewrite_manifesto_file('customer_manifesto.txt',
                                            new_customer_manifesto)
                disk.rewrite_inventory('inventory.txt', inventory)
                print('\n\nGoodbye, have a nice day')


if __name__ == '__main__':
    main()