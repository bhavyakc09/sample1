import mycode

def test_myfunc():
    assert mycode.myfunc(2, 3) == 5
    assert mycode.myfunc(0, 0) == 0
    assert mycode.myfunc(-1, 1) == 0
