"""IF statement

@see: https://docs.python.org/3/tutorial/controlflow.html

There can be zero or more elif parts, and the else part is optional. The keyword ‘elif’ is
short for ‘else if’, and is useful to avoid excessive indentation.

An if … elif … elif … sequence is a substitute for the switch or case statements found
in other languages.
"""


def test_if_statement():
    """IF statement"""

    number = 0.0
    conclusion = ''

    if number < 0.0:
        conclusion = 'Number is less than zero'
    elif number == 0.0:
        conclusion = 'Number equals to zero'
    elif number < 1.0:
        conclusion = 'Number is greater than zero but less than one'
    else:
        conclusion = 'Number bigger than or equal to one'

    assert conclusion == 'Number equals to zero'


def test_grade_boundary():
    """IF statement"""

    number = 80
    conclusion = ''

    if number < 60:
        conclusion = 'you need study '
    elif number == 60:
        conclusion = 'just pass'
    elif number < 80:
        conclusion = 'work harder '
    else:
        conclusion = 'not bad'

    assert conclusion == 'not bad'


def test_youre_rich():
    """IF statement"""

    number = 1000000
    conclusion = ''

    if number < 10000:
        conclusion = 'you are poor'
    elif number == 10000:
        conclusion = 'not bad'
    elif number < 100000:
        conclusion = 'work harder i trust you'
    else:
        conclusion = 'youre rich'

    assert conclusion == 'youre rich'