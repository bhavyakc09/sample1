import pandas as pd

# Load the Excel file
input_file = input('Enter the path to the input Excel file: ')
data_frame = pd.read_excel(input_file)

# Display the names of all columns in the file
print('Available columns:')
print(', '.join(data_frame.columns))

# Prompt the user to enter the name of the column
input_column = input('Enter the name of the column you want to use as input: ')

# Iterate over the rows and print the value in the input column
for index, row in data_frame.iterrows():
    input_value = row[input_column]
    print(f"Row {index + 1} - {input_column}: {input_value}")

