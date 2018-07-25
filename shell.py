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


def which_item(inventory, mode):
    ''' (str) -> dict

    Asks user which item they want and returns that item as a dictionary
    '''
    while True:
        show_inventory(inventory, 'c')
        if mode == 'rent':
            item_choice = input(
                '\nType the name of the item you want to rent (case sensitive)\n>>> '
            )
            for item in inventory:
                if item_choice == item['item_name'] and item['in_stock']:
                    return item
            print(
                'Sorry, either we do not have that item or it is out of stock. Please try again\n'
            )
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


def add_item_to_cart(cart, item, choice):
    ''' (list, dict) -> list of lists

    Adds an item to the cart; can either be an item to rent or an item to return
    '''
    cart.append([item['item_name'], choice])


def main():
    inventory = core.process_inventory(disk.read_inventory('inventory.txt'))
    while True:
        identity = employee_or_customer()
        if identity == 'c':  #customer path
            choice = rent_or_return()
            if choice == 'rent':
                item_choice = which_item(inventory, 'rent')
                core.rent_item(item_choice)
                print(
                    f'1 {item_choice["item_name"]} has been added to your cart'
                )
            if choice == 'return':
                pass

    #if not item['in_stock'] == item['initial_stock']:  #checks if an item has full stock


if __name__ == '__main__':
    main()