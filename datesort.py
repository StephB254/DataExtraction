#!/usr/bin/python3

import csv
from datetime import datetime
import os

def process_data(data):
    
    try:
        # Use datetime.strptime to parse the date string
        date_obj = datetime.strptime(data, "%Y-%m-%dT%H:%M:%S.%f%z")
    
        # Extract and return the day
        day = date_obj.strftime("%Y-%m-%d")
        return day
    except ValueError:
        # error handling
        print(f"Unable to parse date: {data}")
        pass
        



    
file_named = input("Enter path to file: ")
# Column to  process
column_index = 1

with open(filenamed, 'r') as file:
    reader = csv.reader(file)
    
    # Skip the header row if it exists
    header = next(reader, None)  # Use next() to skip the header row
    
    # Iterate through the rows and process data from the specified column
    for row in reader:
        if len(row) > column_index:  # Check if the specified column exists
            data_to_process = row[column_index]  # Get data from the specified column
            
            day = process_data(data_to_process)
            # Check if extraction was successful
            if day is not None:

            # Define the CSV filename using the extracted day
                csv_filename = f"{day}_data.csv"

            # Check if the CSV file already exists
                if os.path.isfile(csv_filename):
                    mode = 'a'  # Append mode if does
                else:
                    mode = 'w'  # Write mode if it doesn't 

            # Entering data to date appropriated file
            csv_entry = row

            # Save file
            with open(csv_filename, mode, newline='') as file:
                writer = csv.writer(file)
                if mode == 'w':
                    writer.writerow(header)
                    writer.writerow(csv_entry)
                elif mode == 'a':
                    writer.writerow(csv_entry)


