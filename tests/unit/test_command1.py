from test_cov.commands import comand1


def test_add():
    assert 3 == comand1.add(1, 2)
