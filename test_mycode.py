import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import myfunc

# call myfunc with input file path and user input
result = myfunc('./input_data.xlsx', 'some input')
print(result)


def test_myfunc():
    assert myfunc(2, 3) == 5
    assert myfunc(0, 0) == 0
    assert myfunc(-1, 1) == 0
