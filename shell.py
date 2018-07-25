import core, shell


def greeting():
    '''
    Greets the user
    '''


def show_inventory_customer(inventory):
    ''' (list of dict) -> NoneType

    Shows the inventory in a customer friendly way
    '''
    inventory_str = ''
    for item in inventory:
        if item['in_stock']:
            inventory_str += f'{item["item_name"]}: ${item["base_rental_price"]:.2f} to rent (${item["replacement_cost"]:.2f} to replace), {item["in_stock"]} left in stock\n'
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


def main():
    pass


if __name__ == '__main__':
    main()