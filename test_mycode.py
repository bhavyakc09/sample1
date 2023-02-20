import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import mycode

def test_myfunc():
    assert mycode.myfunc(2, 3) == 5
    assert mycode.myfunc(0, 0) == 0
    assert mycode.myfunc(-1, 1) == 0
