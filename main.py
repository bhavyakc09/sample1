import pandas as pd

import sys
print(sys.executable)

# Load the Excel file
data_frame = pd.read_excel('input_data.xlsx')

# Prompt the user to enter the column name
input_column = input('Enter the name of the column you want to use as input: ')

# Iterate over the rows and print the value in the input column
for index, row in data_frame.iterrows():
    input_value = row[input_column]
    print(f"Row {index + 1} - {input_column}: {input_value}")
    df = pd.read_excel('input_data.xlsx', engine='openpyxl')

