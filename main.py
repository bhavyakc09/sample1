import pandas as pd

# Read input data from Excel file
df = pd.read_excel('input_data.xlsx')

# Process input data
output_data = []
for index, row in df.iterrows():
    # Read input values from row
    input_value_1 = row['Input Column 1']
    input_value_2 = row['Input Column 2']
    
    # Perform some operation on input values
    output_value = input_value_1 + input_value_2
    
    # Append output value to output data list
    output_data.append(output_value)

# Write output data to Excel file
output_df = pd.DataFrame(output_data, columns=['Output Column'])
output_df.to_excel('output_data.xlsx', index=False)
