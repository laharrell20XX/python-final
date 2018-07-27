import core, disk


def greeting():
    '''
    Greets the user
    '''


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
                return disk.process_user_items(
                    disk.read_manifesto('customer_manifesto.txt'))
            else:
                disk.new_user('customer_manifesto.txt', username)
                print(f'Took you long enough to find us {username}! Welcome!')
                return disk.process_user_items(
                    disk.read_manifesto('customer_manifesto.txt'))
        print('Sorry, you must enter a username')


def which_item(inventory, mode):
    ''' (str) -> dict

    Asks user which item they want and returns that item as a dictionary
    '''
    while True:
        if mode == 'rent':
            return rent_mode(inventory)
        if mode == 'return':
            item_choice = input(
                '\nType the name of the item you want to return (case sensitive)\n>>> '
            )
            for item in inventory:
                if item_choice == item['item_name'] and item['in_stock'] < item['initial_stock']:
                    return item
            print(
                "Sorry that item is unable to be returned either because no one has rented it yet, or it is not offered here\n"
            )


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


#if not item['in_stock'] == item['initial_stock']:  #checks if an item has full stock
def main():
    inventory = core.process_inventory(disk.read_inventory('inventory.txt'))
    identity = employee_or_customer()
    while True:
        if identity == 'c':  #customer path
            username = user_login()
            choice = rent_or_return()
            if choice == 'rent':
                item_choice = which_item(inventory, 'rent')
                core.rent_item(item_choice)
                print(
                    f'1 {item_choice["item_name"]} has been added to your cart.'
                )
            if choice == 'return':
                item_choice = which_item(inventory, 'return')
                core.return_item(item_choice)
                print(
                    f'1 {item_choice["item_name"]} has been returned.  Please checkout to get your deposit back.'
                )
            if choice == 'checkout':
                pass


if __name__ == '__main__':
    main()