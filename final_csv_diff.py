import pandas as pd
import csv

# Loading the csv file in pandas DataFrame
df1 = pd.read_csv('file1.csv')
df2 = pd.read_csv('file2.csv')

# Loading the DataFrame to numpy arr
np1 = df1.to_numpy(dtype=str, na_value='')
np2 = df2.to_numpy(dtype=str, na_value='')

# Comparing the corresponding value
status = (np1 == np2)

# Open the first CSV file and read its contents
with open('file1.csv', 'r') as file1:
    reader1 = csv.reader(file1)
    data1 = list(reader1)

# Open the second CSV file and read its contents
with open('file2.csv', 'r') as file2:
    reader2 = csv.reader(file2)
    data2 = list(reader2)

# Write the modified data back to the CSV file
complete_merge_data = data1 + data2[1:] + status.tolist()
with open('complete_merged_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(complete_merge_data)
    print("Task Completed")