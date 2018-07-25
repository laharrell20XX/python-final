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