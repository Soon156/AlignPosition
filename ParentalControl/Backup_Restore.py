import csv
import json
import os
import shutil
import zipfile
import logging as log
from Funtionality.Config import app_folder, app_filter_list, temp_folder, CONFIG_PATH
from ParentalControl.Auth import read_use_time, read_app_use_time, write_use_time, write_app_use_time, \
    read_table_data, save_table_data

files = ["use_time.csv", "app_use_time.csv", "table_data.json", "filter.json", "config.ini"]


def extract_use_time():
    log.info(f"Saving Use Time...")
    data = read_use_time()
    path = os.path.join(temp_folder, files[0])
    with open(path, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)


def extract_app_use_time():
    log.info(f"Saving Program Time...")
    data = read_app_use_time()
    # Extract the column names (unique keys from all inner dictionaries)
    columns = set()
    for inner_dict in data.values():
        columns.update(inner_dict.keys())

    path = os.path.join(temp_folder, files[1])

    # Write the data to the CSV file
    with open(path, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=['Date'] + sorted(columns))
        writer.writeheader()

        for date, inner_dict in data.items():
            row = {'Date': date}
            row.update(inner_dict)
            writer.writerow(row)


def extract_table_data():
    log.info(f"Saving Parental Setting...")
    path = os.path.join(temp_folder, files[2])
    data = read_table_data()
    with open(path, "w") as file:
        json.dump(data, file)


def retrieve_use_time(path):
    log.info(f"Reading Use Time...")
    loaded_2d_array = []
    with open(path, mode="r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            loaded_2d_array.append(row)
    return loaded_2d_array


def retrieve_app_use_time(path):
    log.info(f"Reading Program Use Time...")
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


def retrieve_table_data(path):
    log.info(f"Reading Parental Setting...")
    with open(path, "r") as file:
        data = json.load(file)
    return data


def zip_files(path):
    extract_use_time()
    extract_app_use_time()
    extract_table_data()
    with zipfile.ZipFile(path, 'w') as zipf:
        for file in files:
            temp_path = os.path.join(temp_folder, file)
            if file is not files[3] and file is not files[4]:
                zipf.write(temp_path, os.path.basename(file))
                os.remove(temp_path)
            else:
                if file is files[4]:
                    log.info("Saving config...")
                    zipf.write(CONFIG_PATH, os.path.basename(file))
                else:
                    log.info("Saving app filer list...")
                    zipf.write(app_filter_list, os.path.basename(file))
    log.info(f"Data has been extracted and backup on !{path}")
    return path


def extract_zip(zip_file_path):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(temp_folder)
    for file in files:
        path = os.path.join(temp_folder, file)
        if file == files[0]:
            use_time = retrieve_use_time(path)
            write_use_time(use_time)
        if file == files[1]:
            app_time = retrieve_app_use_time(path)
            write_app_use_time(app_time)
        if file == files[2]:
            table_data = retrieve_table_data(path)
            save_table_data(table_data)
        if file == files[3]:
            os.remove(app_filter_list)
            log.info("Saving app filer list...")
            shutil.move(path, app_folder)
        if file == files[4]:
            os.remove(CONFIG_PATH)
            log.info("Saving Config...")
            shutil.move(path, app_folder)
        try:
            os.remove(path)
        except FileNotFoundError:
            pass
    log.info("Data has been recovered!")
