from test_cov.commands import comand1


def test_add():
    assert 3 == comand1.add(1, 2)


def test_sub():
    assert 3 == comand1.sub(4, 1)


def test_add_div_sub():
    assert 1 == comand1.add_div_sub(1, 1)
