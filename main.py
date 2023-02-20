import argparse
import pandas as pd

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Read an Excel file and print the values in a specified column.')
parser.add_argument('--input_file', type=str, required=True, help='path to the input Excel file')
parser.add_argument('--column_name', type=str, required=True, help='name of the column to read')
args = parser.parse_args()

# Load the Excel file
data_frame = pd.read_excel(args.input_file)

# Iterate over the rows and print the value in the input column
for index, row in data_frame.iterrows():
    input_value = row[args.column_name]
    print(f"Row {index + 1} - {args.column_name}: {input_value}")


