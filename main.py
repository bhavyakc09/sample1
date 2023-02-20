import openpyxl

# open the Excel file
wb = openpyxl.load_workbook('./input_data.xlsx')

# select the active sheet
ws = wb.active

# prompt the user to enter input
user_input = input("Enter any input from the Excel file: ")

# search for the input in the sheet
for row in ws.iter_rows(values_only=True):
    if user_input in row:
        print(row)
