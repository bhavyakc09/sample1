import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import myfunc

# call myfunc with input file path and user input
result = myfunc('./input_data.xlsx', 'some input')
print(result)

def test_myfunc(tmp_path):
    input_file = tmp_path / "test_input.xlsx"
    # create a test Excel file
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet["A1"] = 1
    sheet["A2"] = 2
    sheet["A3"] = 3
    wb.save(input_file)

    # test myfunc with the test input file
    result = myfunc(input_file, 'some input')
    assert result == expected_result

