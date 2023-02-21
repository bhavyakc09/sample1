import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import myfunc

def test_myfunc():
    assert myfunc('input 1') == ('input 1', 'data 1', 'value 1')
    assert myfunc(2, 3) == 5
    assert myfunc(0, 0) == 0
    assert myfunc(-1, 1) == 0
