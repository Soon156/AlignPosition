import os
import logging as log
import pickle

from cryptography.fernet import Fernet
from Funtionality.Config import user_key_path, userdata


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


def encrypt_data(data):
    fernet = Fernet(load_init_key())
    encrypted_data = fernet.encrypt(data)
    return encrypted_data


# TODO if decrypt failed
def decrypt_data(data):
    fernet = Fernet(load_init_key())
    decrypted_data = fernet.decrypt(data)
    return decrypted_data


def write_to_file(data):
    pickled_row = pickle.dumps(data)
    encrypted_data = encrypt_data(pickled_row)
    with open(userdata, 'wb') as file:
        file.write(encrypted_data)
    log.info("Elapsed time saved")


def read_from_file():
    unpicked_row = []
    try:
        with open(userdata, 'rb') as file:
            encrypted_data = file.read()
            unpicked_row = pickle.loads(decrypt_data(encrypted_data))
    except pickle.UnpicklingError:
        log.warning("User file modified/corrupted") # TODO error handler
    return unpicked_row

