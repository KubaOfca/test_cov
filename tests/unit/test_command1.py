from test_cov.commands import comand1


def test_add():
    assert 3 == comand1.add(1, 2)


def test_sub():
    assert 3 == comand1.sub(4, 1)
