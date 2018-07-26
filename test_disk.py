import disk
from bcca.test import fake_file


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
    '''car,2,3,4,5
rabbit,5,6,7,8
pen,9,10,11,12'''
})
def test_rewrite_inventory():
    with open('fake_inventory.txt', 'w') as file:
        for item in ['car,2,3,4,5\n', 'rabbit,5,6,7,8\n', 'pen,9,10,11,12\n']:
            file.write(item)
    assert open('fake_inventory.txt').read() == '''car,2,3,4,5
rabbit,5,6,7,8
pen,9,10,11,12
'''


@fake_file({'manifesto.txt': ''})
def test_login_first_customer():
    assert not disk.login('manifesto.txt', 'Logan')
    assert open('manifesto.txt').read() == 'Logan,(item)\n'


@fake_file({'manifesto.txt': 'Logan,(item)\nBill,(item)\n'})
def test_login_new_customer():
    assert not disk.login('manifesto.txt', 'Bob')
    assert open('manifesto.txt').read() == '''Logan,(item)
Bill,(item)
Bob,(item)
'''


@fake_file({'manifesto.txt': 'Logan,(item)\nBill,(item)\n'})
def test_login_existing_customer():
    assert disk.login('manifesto.txt', 'Logan')
    assert open('manifesto.txt').read() == '''Logan,(item)
Bill,(item)
'''
