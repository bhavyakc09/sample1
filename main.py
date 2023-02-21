import openpyxl

# define myfunc() function
def myfunc(input_file_path=None):
    if input_file_path:
        # read input from Excel file
        wb = openpyxl.load_workbook(input_file_path)
        sheet = wb.active
        # Prompt the user to enter the input value from the Excel file
        user_input = input(f"Enter any input from the Excel file (or press Enter to use the default value): ")
        if user_input:
            input_value = sheet[user_input].value
        else:
            input_value = sheet['A1'].value if sheet['A1'].value is not None else 0
    else:
        # read input from user
        input_value = input("Enter any input value: ")

    # Do some processing with the input value
    result = input_value * 2

    return result
