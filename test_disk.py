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


@fake_file({'manifesto.txt': 'Logan, ()\nBill, ()\n'})
def test_login_new_customer():
    assert not disk.login('manifesto.txt', 'Bob')


@fake_file({'manifesto.txt': 'Logan, ()\nBill, ()\n'})
def test_login_existing_customer():
    assert disk.login('manifesto.txt', 'Logan')


def test_process_user_items():
    list_of_usernames = ['Logan, ()', 'Bill, (two,three,four)']
    assert disk.process_user_items(list_of_usernames) == [{
        'Logan': '()'
    }, {
        'Bill':
        '(two,three,four)'
    }]


@fake_file({'manifesto.txt': 'Logan, ()'})
def test_rewrite_manifesto_file():
    items = [{'Logan': ['two', 'three', 'four']}, {'Bill': []}]
    user_list = []
    for user in items:
        for username in user.keys():
            user_list.append(f"{username}, ({(',').join(user[username])})")
    with open('manifesto.txt', 'w') as file:
        file.write(('\n').join(user_list))
    assert open('manifesto.txt').read() == '''Logan, (two,three,four)
Bill, ()'''
