import openpyxl

# define myfunc() function
def myfunc(a, b):
    return a + b

    # open the Excel file
    wb = openpyxl.load_workbook('./input_data.xlsx')

    # select the active sheet
    ws = wb.active

    # prompt the user to enter input
    try:
        user_input = input("Enter any input from the Excel file (or press Enter to use the default value): ") or "default value"
    except EOFError:
        user_input = "default value"

    # search for the input in the sheet
    for row in ws.iter_rows(values_only=True):
        if user_input in row:
            return row
    return None
