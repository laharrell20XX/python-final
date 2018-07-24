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
