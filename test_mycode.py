import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import myfunc

# call myfunc with input file path and user input
result = myfunc('./input_data.xlsx', 'some input')
print(result)

def test_myfunc(tmp_path):
    # create a temporary input file
    input_file = tmp_path / "test_input.xlsx"
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.cell(1, 1, "test value")
    wb.save(input_file)

    # test with valid input file and user input
    assert myfunc(input_file, "test input") == "test value"

def test_myfunc():
    assert myfunc(2, 3) == 5
    assert myfunc(0, 0) == 0
    assert myfunc(-1, 1) == 0
