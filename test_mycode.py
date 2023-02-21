import os
import sys
import openpyxl
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import myfunc

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
    expected_result = 2
    result = myfunc(input_file)
    assert result == expected_result
