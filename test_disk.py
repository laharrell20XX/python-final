import disk
from bcca.test import fake_file
from datetime import datetime


@fake_file({
    'fake_inventory.txt':
    '''car,2,3,4,5
rabbit,5,6,7,8
pen,9,10,11,12'''
})
def test_read_inventory():
    assert disk.read_inventory('fake_inventory.txt') == [
        'car,2,3,4,5\n', 'rabbit,5,6,7,8\n', 'pen,9,10,11,12'
    ]


@fake_file({
    'fake_inventory.txt':
    '''car,2,3,5,5
rabbit,5,6,7,8
pen,9,10,11,12
'''
})
def test_rewrite_inventory():
    inventory = [{
        'item_name': 'car',
        'base_rental_price': 2,
        'replacement_cost': 3,
        'in_stock': 2,
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
    with open('fake_inventory.txt', 'w') as file:
        for item in inventory:
            file.write(
                f"{item['item_name']},{item['base_rental_price']},{item['replacement_cost']},{item['in_stock']},{item['initial_stock']}\n"
            )
    assert open('fake_inventory.txt').read() == '''car,2,3,2,5
rabbit,5,6,7,8
pen,9,10,11,12
'''


@fake_file({'manifesto.txt': ''})
def test_login_first_customer():
    assert not disk.login('manifesto.txt', 'Logan')


@fake_file({'manifesto.txt': 'Logan, ()\nBill, ()\n'})
def test_login_new_customer():
    assert not disk.login('manifesto.txt', 'Bob')


@fake_file({'manifesto.txt': 'Logan, ()\nBill, ()\n'})
def test_login_existing_customer():
    assert disk.login('manifesto.txt', 'Logan')


def test_process_user_items():
    list_of_usernames = ['Logan, ()', 'Bill, (two,three,four)']
    assert disk.process_user_items(list_of_usernames) == [{
        'Logan': ['']
    }, {
        'Bill': ['two', 'three', 'four']
    }]


@fake_file({'manifesto.txt': 'Logan, ()'})
def test_rewrite_manifesto_file():
    customer_manifesto = [{'Logan': ['two', 'three', 'four']}, {'Bill': []}]
    user_list = []
    for user in customer_manifesto:
        for username in user.keys():
            user_list.append(f"{username}, ({(',').join(user[username])})")
    with open('manifesto.txt', 'w') as file:
        file.write(('\n').join(user_list))
    assert open('manifesto.txt').read() == '''Logan, (two,three,four)
Bill, ()'''


@fake_file({'fake_revenue.txt': '100.00'})
def test_read_revenue_nonempty():
    assert disk.read_revenue('fake_revenue.txt') == 100.0


@fake_file({'fake_revenue.txt': ''})
def test_read_revenue_empty():
    assert disk.read_revenue('fake_revenue.txt') == 0.0


@fake_file({'fake_revenue.txt': '100.00'})
def test_update_revenue():
    revenue = 100.0
    total = 42.5
    with open('fake_revenue.txt', 'w') as file:
        file.write(f'{revenue + total:.2f}')
    assert open('fake_revenue.txt').read() == '142.50'


@fake_file({'fake_history.txt': 'Logan, 07/30/18 @ 09:40:28 AM, $72.50'})
def test_read_history():
    assert disk.read_history('fake_history.txt') == [
        'Logan, 07/30/18 @ 09:40:28 AM, $72.50'
    ]
