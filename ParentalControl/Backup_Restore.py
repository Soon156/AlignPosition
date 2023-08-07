import csv
import os
import zipfile
import logging as log
from Funtionality.Config import desktop_path
from ParentalControl.Auth import read_use_time, read_app_use_time, write_use_time, write_app_use_time

files = ["use_time.csv", "app_use_time.csv"]


def extract_use_time():
    data = read_use_time()
    with open(files[0], mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)


def extract_app_use_time():
    data = read_app_use_time()
    # Extract the column names (unique keys from all inner dictionaries)
    columns = set()
    for inner_dict in data.values():
        columns.update(inner_dict.keys())

    # Write the data to the CSV file
    with open(files[1], mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=['Date'] + sorted(columns))
        writer.writeheader()

        for date, inner_dict in data.items():
            row = {'Date': date}
            row.update(inner_dict)
            writer.writerow(row)


def retrieve_use_time(path):
    loaded_2d_array = []
    with open(path, mode="r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            loaded_2d_array.append(row)
    return loaded_2d_array


def retrieve_app_use_time(path):
    # Initialize an empty dictionary to store the retrieved data
    retrieved_data = {}

    # Read the data from the CSV file
    with open(path, mode="r") as file:
        reader = csv.DictReader(file)

        # Loop through each row in the CSV
        for row in reader:
            date = row['Date']
            inner_dict = {}

            # Loop through each column (except the 'Date' column) and build the inner dictionary
            for column, value in row.items():
                if column != 'Date':
                    if value != '':
                        inner_dict[column] = int(value)

            # Add the inner dictionary to the retrieved data dictionary
            retrieved_data[date] = inner_dict
    return retrieved_data


def zip_files(path):
    extract_use_time()
    extract_app_use_time()
    with zipfile.ZipFile(path, 'w') as zipf:
        for file in files:
            zipf.write(file, os.path.basename(file))
            os.remove(file)
    return path


def extract_zip(zip_file_path):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(desktop_path)
    for file in files:
        path = os.path.join(desktop_path, file)
        print(path)
        if file == "use_time.csv":
            use_time = retrieve_use_time(path)
            write_use_time(use_time)
        if file == "app_use_time.csv":
            app_time = retrieve_app_use_time(path)
            write_app_use_time(app_time)
        try:
            os.remove(path)
        except FileNotFoundError:
            pass
