import os
import sys
import openpyxl
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    
def myfunc(tmp_path, monkeypatch):
    input_file = tmp_path / "input_data.xlsx"
    # create a test Excel file
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet["A1"] = 1
    sheet["A2"] = 2
    sheet["A3"] = 3
    wb.save(input_file)

    # set up input for the function
    input_str = "A2\n"  # simulate user entering "A2" at the prompt
    monkeypatch.setattr('builtins.input', lambda x: input_str)

    # test myfunc with the test input file
    expected_result = 4
    result = myfunc(input_file)
    assert result == expected_result
    
   

