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