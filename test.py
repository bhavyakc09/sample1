import my_module

def test_function1():
    assert my_module.function1(1, 2) == 3

def test_function2():
    assert my_module.function2(4) == 16
    assert my_module.function2(-4) == 16

def test_function3():
    assert my_module.function3([1, 2, 3, 4]) == 2.5
    assert my_module.function3([0, 0, 0]) == 0
    
def test_addition():
    assert 2 + 2 == 4


