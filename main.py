import sys
import pandas as pd

# Read command line argument for input column name
input_column = sys.argv[1]

# Read input Excel file
df = pd.read_excel('input.xlsx')

# Perform some operation on input column
for index, row in df.iterrows():
    input_value = row[input_column]
    # perform some operation on input value
    print(input_value)
