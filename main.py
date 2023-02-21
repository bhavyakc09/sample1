import pandas as pd
import openpyxl
import argparse

def read_input_data(input_file):
    df = pd.read_excel(input_file)
    return df

def process_input_data(df):
    print("Column names:", df.columns)
    df['output'] = df['input'] * 2
    return df

def write_output_data(output_file, df):
    writer = pd.ExcelWriter(output_file, engine='openpyxl')
    writer.book = openpyxl.Workbook()
    df.to_excel(writer, index=False)
    writer.save()

def process_excel(input_file, output_file):
    df = read_input_data(input_file)
    df = process_input_data(df)
    write_output_data(output_file, df)
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_file', type=str, help='Path to input Excel file')
    parser.add_argument('--output_file', type=str, help='Path to output Excel file')
    args = parser.parse_args()
    
    input_file = args.input_file
    output_file = args.output_file
    
    process_excel(input_file, output_file)
