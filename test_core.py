import core
import bcca.test


def test_process_inventory_full():
    unprocessed_inventory = [
        'car,2,3,4,5\n', 'rabbit,5,6,7,8\n', 'pen,9,10,11,12'
    ]
    assert core.process_inventory(unprocessed_inventory) == [{
        'item_name':
        'car',
        'base_rental_price':
        2,
        'replacement_cost':
        3,
        'in_stock':
        4,
        'initial_stock':
        5
    }, {
        'item_name':
        'rabbit',
        'base_rental_price':
        5,
        'replacement_cost':
        6,
        'in_stock':
        7,
        'initial_stock':
        8
    }, {
        'item_name':
        'pen',
        'base_rental_price':
        9,
        'replacement_cost':
        10,
        'in_stock':
        11,
        'initial_stock':
        12
    }]


def test_convert_inventory_full():
    inventory_list = [{
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
    assert core.convert_inventory(inventory_list) == [
        'car,2,3,4,5\n', 'rabbit,5,6,7,8\n', 'pen,9,10,11,12\n'
    ]


def test_rent_item_instock():
    item = {
        'item_name': 'car',
        'base_rental_price': 2,
        'replacement_cost': 3,
        'in_stock': 4,
        'initial_stock': 5
    }
    core.rent_item(item)
    assert item['in_stock'] == 3


def test_rent_item_out_of_stock():
    item = {
        'item_name': 'car',
        'base_rental_price': 2,
        'replacement_cost': 3,
        'in_stock': 0,
        'initial_stock': 5
    }
    core.rent_item(item)
    assert item['in_stock'] == -1


def test_return_item_half_stocked():
    item = {
        'item_name': 'car',
        'base_rental_price': 2,
        'replacement_cost': 3,
        'in_stock': 3,
        'initial_stock': 6
    }
    core.return_item(item)
    assert item['in_stock'] == 4


def test_return_item_full_stocked():
    item = {
        'item_name': 'car',
        'base_rental_price': 2,
        'replacement_cost': 3,
        'in_stock': 6,
        'initial_stock': 6
    }
    core.return_item(item)
    assert item['in_stock'] == 7


def test_add_item_to_empty_cart():
    item = {'item_name': 'car', 'in_stock': 6, 'initial_stock': 6}
    cart = []
    assert core.add_item_to_cart(cart, item, 'rent') == [[{
        'item_name': 'car',
        'in_stock': 6,
        'initial_stock': 6
    }, 'rent']]


def test_check_full_stock_not_full():
    inventory = [{
        'item_name': 'car',
        'in_stock': 4,
        'initial_stock': 5
    }, {
        'item_name': 'rabbit',
        'in_stock': 7,
        'initial_stock': 8
    }, {
        'item_name': 'pen',
        'in_stock': 11,
        'initial_stock': 12
    }]
    assert not core.check_full_stock(inventory)


def test_check_full_stock_some_empty():
    inventory = [{
        'item_name': 'car',
        'in_stock': 5,
        'initial_stock': 5
    }, {
        'item_name': 'rabbit',
        'in_stock': 8,
        'initial_stock': 8
    }, {
        'item_name': 'pen',
        'in_stock': 0,
        'initial_stock': 12
    }]
    assert not core.check_full_stock(inventory)


def test_check_full_stock_full():
    inventory = [{
        'item_name': 'car',
        'in_stock': 5,
        'initial_stock': 5
    }, {
        'item_name': 'rabbit',
        'in_stock': 8,
        'initial_stock': 8
    }, {
        'item_name': 'pen',
        'in_stock': 12,
        'initial_stock': 12
    }]
    assert core.check_full_stock(inventory)


def test_checkout_rent_one():
    cart = [[{
        'item_name': 'car',
        'base_rental_price': 4,
        'replacement_cost': 10
    }, 'rent']]
    assert core.checkout(cart) == 5.28


def test_checkout_multiple_rent():
    cart = [[{
        'item_name': 'car',
        'base_rental_price': 4,
        'replacement_cost': 10
    }, 'rent'], [{
        'item_name': 'car',
        'base_rental_price': 4,
        'replacement_cost': 10
    }, 'rent'], [{
        'item_name': 'rabbit',
        'base_rental_price': 7,
        'replacement_cost': 15
    }, 'rent']]
    assert core.checkout(cart) == 19.55


def test_checkout_one_return():
    cart = [[{
        'item_name': 'car',
        'base_rental_price': 4,
        'replacement_cost': 10
    }, 'return']]
    assert core.checkout(cart) == -1.0


def test_checkout_mix():
    cart = [[{
        'item_name': 'car',
        'base_rental_price': 4,
        'replacement_cost': 10
    }, 'return'], [{
        'item_name': 'car',
        'base_rental_price': 4,
        'replacement_cost': 10
    }, 'rent'], [{
        'item_name': 'rabbit',
        'base_rental_price': 7,
        'replacement_cost': 15
    }, 'rent']]
    assert core.checkout(cart) == 13.27


def test_checkout_empty():
    cart = [[]]
    assert core.checkout(cart) == 0.00


def test_can_return_can():
    username = 'Logan'
    customer_manifesto = [{'Logan': ['one', 'two', 'three']}, {'Bill': ['']}]
    assert core.can_return(username, customer_manifesto)


def test_can_return_cannot():
    customer = 'Bill'
    customer_manifesto = [{'Logan': ['one', 'two', 'three']}, {'Bill': ['']}]
    assert not core.can_return(customer, customer_manifesto)


def test_get_rented_items():
    customer = 'Logan'
    customer_manifesto = [{'Logan': ['one', 'two', 'three']}]
    assert core.get_rented_items(
        customer, customer_manifesto) == ['one', 'two', 'three']


def test_transaction_tax():
    cart = [[{
        'item_name': 'car',
        'base_rental_price': 5
    }, 'rent'], [{
        'item_name': 'rabbit',
        'base_rental_price': 7
    }, 'rent']]
    assert core.transaction_tax(cart) == .84


def test_change_rented_items_more_items():
    cart = [[{'item_name': 'car'}, 'rent'], [{'item_name': 'pizza'}, 'rent']]
    customer = 'Logan'
    customer_manifesto = [{'Logan': ['car', 'bear']}, {'Bill': ['']}]
    assert core.change_rented_items(cart, customer, customer_manifesto) == [{
        'Logan': ['car', 'bear', 'car', 'pizza']
    }, {
        'Bill': ['']
    }]


def test_change_rented_items_new_items():
    cart = [[{'item_name': 'car'}, 'rent'], [{'item_name': 'pizza'}, 'rent']]
    customer = 'Bill'
    customer_manifesto = [{'Logan': ['car', 'bear']}, {'Bill': ['']}]
    assert core.change_rented_items(cart, customer, customer_manifesto) == [{
        'Logan': ['car', 'bear']
    }, {
        'Bill': ['car', 'pizza']
    }]
