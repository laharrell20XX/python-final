import shell
from bcca.test import fake_file, should_print, with_inputs


@with_inputs('fef', 'g', 'E')
@should_print
def test_employee_or_customer_emp(output):
    assert shell.employee_or_customer() == 'e'
    assert output == '''Are you an [e]mployee or a [c]ustomer? (type 'leave' to exit the application)
>>> fef
The identity you entered is not valid.  Please try again
Are you an [e]mployee or a [c]ustomer? (type 'leave' to exit the application)
>>> g
The identity you entered is not valid.  Please try again
Are you an [e]mployee or a [c]ustomer? (type 'leave' to exit the application)
>>> E'''


@with_inputs('p', 'C')
@should_print
def test_employee_or_customer_cust(output):
    assert shell.employee_or_customer() == 'c'
    assert output == '''Are you an [e]mployee or a [c]ustomer? (type 'leave' to exit the application)
>>> p
The identity you entered is not valid.  Please try again
Are you an [e]mployee or a [c]ustomer? (type 'leave' to exit the application)
>>> C'''


@with_inputs('q', 'eturn', 'Return')
@should_print
def test_rent_or_return_return(output):
    assert shell.rent_or_return() == 'return'
    assert output == '''Hi!  Type 'rent' to rent an item, or type 'return' to return an item.
>>> q
Invalid option
Hi!  Type 'rent' to rent an item, or type 'return' to return an item.
>>> eturn
Invalid option
Hi!  Type 'rent' to rent an item, or type 'return' to return an item.
>>> Return'''


@with_inputs('q', 'ent', 'RENT')
@should_print
def test_rent_or_return_rent(output):
    assert shell.rent_or_return() == 'rent'
    assert output == '''Hi!  Type 'rent' to rent an item, or type 'return' to return an item.
>>> q
Invalid option
Hi!  Type 'rent' to rent an item, or type 'return' to return an item.
>>> ent
Invalid option
Hi!  Type 'rent' to rent an item, or type 'return' to return an item.
>>> RENT'''


@should_print
def test_show_inventory_customer_nonempty(output):
    inventory = [{
        'item_name': 'car',
        'base_rental_price': 2,
        'replacement_cost': 3,
        'in_stock': 4,
        'initial_stock': 5
    }, {
        'item_name': 'rabbit',
        'base_rental_price': 5,
        'replacement_cost': 6,
        'in_stock': 7,
        'initial_stock': 8
    }, {
        'item_name': 'pen',
        'base_rental_price': 9,
        'replacement_cost': 10,
        'in_stock': 11,
        'initial_stock': 12
    }]
    shell.show_inventory(inventory, 'c')
    assert output == '''car: $2.00 to rent ($3.00 to replace), 4 left in stock
rabbit: $5.00 to rent ($6.00 to replace), 7 left in stock
pen: $9.00 to rent ($10.00 to replace), 11 left in stock
'''


@should_print
def test_show_inventory_customer_empty(output):
    inventory = [{
        'item_name': 'car',
        'base_rental_price': 2,
        'replacement_cost': 3,
        'in_stock': 4,
        'initial_stock': 5
    }, {
        'item_name': 'rabbit',
        'base_rental_price': 5,
        'replacement_cost': 6,
        'in_stock': 0,
        'initial_stock': 8
    }, {
        'item_name': 'pen',
        'base_rental_price': 9,
        'replacement_cost': 10,
        'in_stock': 11,
        'initial_stock': 12
    }]
    shell.show_inventory(inventory, 'c')
    assert output == '''car: $2.00 to rent ($3.00 to replace), 4 left in stock
pen: $9.00 to rent ($10.00 to replace), 11 left in stock
'''


@should_print
def test_show_inventory_employee_nonempty(output):
    inventory = [{
        'item_name': 'car',
        'base_rental_price': 2,
        'replacement_cost': 3,
        'in_stock': 4,
        'initial_stock': 5
    }, {
        'item_name': 'rabbit',
        'base_rental_price': 5,
        'replacement_cost': 6,
        'in_stock': 7,
        'initial_stock': 8
    }, {
        'item_name': 'pen',
        'base_rental_price': 9,
        'replacement_cost': 10,
        'in_stock': 11,
        'initial_stock': 12
    }]
    shell.show_inventory(inventory, 'e')
    assert output == '''car: $2.00 to rent ($3.00 to replace), 4 left in stock (initial stock: 5)
rabbit: $5.00 to rent ($6.00 to replace), 7 left in stock (initial stock: 8)
pen: $9.00 to rent ($10.00 to replace), 11 left in stock (initial stock: 12)
'''


@should_print
def test_show_inventory_employee_empty(output):
    inventory = [{
        'item_name': 'car',
        'base_rental_price': 2,
        'replacement_cost': 3,
        'in_stock': 4,
        'initial_stock': 5
    }, {
        'item_name': 'rabbit',
        'base_rental_price': 5,
        'replacement_cost': 6,
        'in_stock': 0,
        'initial_stock': 8
    }, {
        'item_name': 'pen',
        'base_rental_price': 9,
        'replacement_cost': 10,
        'in_stock': 11,
        'initial_stock': 12
    }]
    shell.show_inventory(inventory, 'e')
    assert output == '''car: $2.00 to rent ($3.00 to replace), 4 left in stock (initial stock: 5)
rabbit: $5.00 to rent ($6.00 to replace), 0 left in stock (initial stock: 8)
pen: $9.00 to rent ($10.00 to replace), 11 left in stock (initial stock: 12)
'''