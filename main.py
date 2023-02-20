import argparse
import pandas as pd

# Define the command line arguments
parser = argparse.ArgumentParser(description='Process input file')
parser.add_argument('--input_file', type=str, help='path to input file')

# Parse the command line arguments
args = parser.parse_args()

# Load the Excel file
data_frame = pd.read_excel(args.input_file)

# Iterate over the rows and print the values in all columns
for index, row in data_frame.iterrows():
    for col_name, col_value in row.iteritems():
        print(f"Row {index + 1} - {col_name}: {col_value}")



