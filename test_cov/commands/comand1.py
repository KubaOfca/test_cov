import test_cov.utils
def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def add_div_sub(x,y):
    add_result = add(x, y)
    div_result = test_cov.utils.div(x, y)
    return add_result - div_result