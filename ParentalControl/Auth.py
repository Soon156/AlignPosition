import json
import os
import pickle

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from Funtionality.Config import key_file_path, salt_file_path, userdata, app_use_time, allow_use_time
import logging as log

msg = "User parental use time file modified/corrupted"

def user_register(password):
    key, salt = generate_password_derived_key(password)
    save_derived_key(key, salt)


# Function to generate a password-derived key
def generate_password_derived_key(password, salt=None, rounds=100000):
    if salt is None:
        salt = os.urandom(16)

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=rounds,
        backend=default_backend()
    )
    key = kdf.derive(password.encode('utf-8'))
    return key, salt


# Function to save the derived key to a file
def save_derived_key(derived_key, salt):
    # Save the derived key to a file
    with open(key_file_path, 'wb') as f:
        f.write(derived_key)
    with open(salt_file_path, 'wb') as f:
        f.write(salt)


# Function to retrieve the derived key from the file
def retrieve_key_salt():
    key = None
    salt = None
    try:
        # Read the derived key from the file
        with open(key_file_path, 'rb') as f:
            key = f.read()
        with open(salt_file_path, 'rb') as f:
            salt = f.read()
        return key, salt
    except FileNotFoundError:
        return key, salt


# Simulate user login
def login_user(password):
    # Retrieve the stored derived key from the file based on the username
    stored_key, stored_salt = retrieve_key_salt()
    if stored_key is not None and stored_salt is not None:
        derived_key, salt = generate_password_derived_key(password, stored_salt)
        # Compare the derived key with the stored key
        if derived_key == stored_key:
            return True
        else:
            # Password is incorrect
            return False
    else:
        # Username not found in the file
        return None


# Change password
def change_password(old_password, new_password):
    if login_user(old_password):  # Verify old password
        data1 = read_use_time()
        data = read_app_use_time()
        table = read_table_data()
        user_register(new_password)
        write_app_use_time(data)
        write_use_time(data1)
        save_table_data(table)
        log.info("Password changed")
        return True
    return False


def write_use_time(data):

    key, salt = retrieve_key_salt()
    if key is not None:
        pickled_row = pickle.dumps(data)
        encrypted_data = encrypt_data(pickled_row, key)
        with open(userdata, 'wb') as file:
            file.write(encrypted_data)
        log.info("Elapsed time saved")


def read_use_time():
    unpicked_row = []
    key, salt = retrieve_key_salt()
    if key is not None:
        try:

            with open(userdata, 'rb') as file:
                encrypted_data = file.read()
                iv = encrypted_data[:16]
                encrypted_data = encrypted_data[16:]
                decrypted_data = decrypt_data(encrypted_data, key, iv)
                unpicked_row = pickle.loads(decrypted_data)

        except pickle.UnpicklingError:
            log.error(msg)
            raise Exception(msg)
        except FileNotFoundError:
            log.warning("No use time record found")
    return unpicked_row


def write_app_use_time(data):
    log.info("App use time recorded")
    key, salt = retrieve_key_salt()
    if key is not None:
        json_data = json.dumps(data).encode('utf-8')
        encrypted_data = encrypt_data(json_data, key)
        with open(app_use_time, "wb") as file:
            file.write(encrypted_data)


def read_app_use_time():
    encrypted_data = {}
    key, salt = retrieve_key_salt()
    if key is not None:
        try:
            with open(app_use_time, "rb") as file:
                encrypted_data = file.read()
                iv = encrypted_data[:16]
                encrypted_data = encrypted_data[16:]
                decrypted_data = decrypt_data(encrypted_data, key, iv)
                json_data = decrypted_data.decode('utf-8')
                return json.loads(json_data)
        except FileNotFoundError:
            log.info("No app use time found")
        return encrypted_data


def encrypt_data(data, key):
    # Generate a random initialization vector (IV)
    iv = os.urandom(16)

    # Create the AES cipher using the derived key and IV
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())

    # Encrypt the data
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(data) + encryptor.finalize()

    # Return the IV and ciphertext (you can store or transmit them together)
    return iv + ciphertext


def decrypt_data(encrypted_data, key, iv):
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()
    return decrypted_data


def save_table_data(data):
    key, salt = retrieve_key_salt()
    if key is not None:
        pickled_row = pickle.dumps(data)
        encrypted_data = encrypt_data(pickled_row, key)
        with open(allow_use_time, 'wb') as file:
            file.write(encrypted_data)
        log.info("Allowed time updated")


def read_table_data():
    unpicked_row = []
    key, salt = retrieve_key_salt()
    if key is not None:
        try:

            with open(allow_use_time, 'rb') as file:
                encrypted_data = file.read()
                iv = encrypted_data[:16]
                encrypted_data = encrypted_data[16:]
                decrypted_data = decrypt_data(encrypted_data, key, iv)
                unpicked_row = pickle.loads(decrypted_data)

        except pickle.UnpicklingError:
            log.error(msg)
            raise Exception(msg)
        except FileNotFoundError:
            log.warning("No table data found")
    return unpicked_row
