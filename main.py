import argparse
import pandas as pd

def main(input_file, output_file):
    # Load the input Excel file
    data_frame = pd.read_excel(input_file)

    # Iterate over the rows and print the values in all columns
    for index, row in data_frame.iterrows():
        for col_name, col_value in row.iteritems():
            print(f"Row {index + 1} - {col_name}: {col_value}")

    # Save the DataFrame to the output Excel file
    data_frame.to_excel(output_file)

if __name__ == '__main__':
    # Define the command line arguments
    parser = argparse.ArgumentParser(description='Process input file')
    parser.add_argument('--input_file', type=str, help='path to input file')
    parser.add_argument('--output_file', type=str, help='path to output file')

    # Parse the command line arguments
    args = parser.parse_args()

    # Call the main function with the input and output file paths
    main(args.input_file, args.output_file)
