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
                    writer.writerow(['ID','CREATED_AT_MX','UPDATED_AT_MX','CUSTOMER_USER_ID','ACCOUNT_NUMBER','AMOUNT','AMOUNT_CURRENCY_CODE','HANDLER_REFERENCE','THIRD_PARTY_TRANSIENT_REFERENCE','THIRD_PARTY_FINAL_REFERENCE','THIRD_PARTY_NAME_CODE','THIRD_PARTY_OUTLET','THIRD_PARTY_STATUS','THIRD_PARTY_TRANSACTION_START_DATE_MX','THIRD_PARTY_TRANSACTION_COMPLETION_DATE_MX','PAYMENT_TYPE','INTENT_ID','PRODUCT','PRODUCT_ITEM_ID','STATUS','SOURCE_REFERENCE_ID','TRANSACTION_COMPLETION_DATE_MX'])  # Write header if creating a new file
                    writer.writerow(csv_entry)
                elif mode == 'a':
                    writer.writerow(csv_entry)


