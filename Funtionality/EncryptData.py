import json
import os
import logging as log
import pickle
from datetime import datetime

from cryptography.fernet import Fernet
from Funtionality.Config import user_key_path, userdata, app_folder

# Get the current month and year
now = datetime.now()
current_month, current_year = now.month, now.year
existing_filename = f"use_time_{current_month:02d}_{current_year}.bin"
filename = os.path.join(app_folder, existing_filename)


def load_init_key():
    if os.path.exists(user_key_path):
        with open(user_key_path, 'rb') as key_file:
            return key_file.read()
    else:
        encryption_key = Fernet.generate_key()
        os.makedirs(os.path.dirname(user_key_path), exist_ok=True)
        with open(user_key_path, 'wb') as key_file:
            key_file.write(encryption_key)
        return encryption_key


fernet = Fernet(load_init_key())


def write_use_time(data):
    pickled_row = pickle.dumps(data)
    encrypted_data = fernet.encrypt(pickled_row)
    with open(userdata, 'wb') as file:
        file.write(encrypted_data)
    log.info("Elapsed time saved")


def read_use_time():
    unpicked_row = []
    try:
        with open(userdata, 'rb') as file:
            encrypted_data = file.read()
            unpicked_row = pickle.loads(fernet.decrypt(encrypted_data))
    except pickle.UnpicklingError:
        log.warning("User file modified/corrupted")  # TODO error handler
    return unpicked_row


def write_app_use_time(data):
    json_data = json.dumps(data).encode('utf-8')
    encrypted_data = fernet.encrypt(json_data)
    with open(filename, "wb") as file:
        file.write(encrypted_data)


def read_app_use_time():
    loaded_data = {}
    with open(filename, "rb") as file:
        loaded_data = file.read()
    decrypted_data = fernet.decrypt(loaded_data)
    json_data = decrypted_data.decode('utf-8')
    return json.loads(json_data)