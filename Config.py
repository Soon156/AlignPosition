import ast
import configparser
import os

# default config
file_name = 'config.ini'
default_value = {'width': 63,
                 'focal': 840,
                 'distance': 53,
                 'camera': 0,
                 'range': 10,
                 'speed': 1,
                 'position': 5,
                 'idle': 5,
                 'rest': 5,
                 'scaling': 1.0,
                 'appearance': 'System',
                 'notifications': True,
                 'background': True,
                 'init': True,
                 }


# save value to config
def write_config(dictionary_str):
    config = configparser.ConfigParser(allow_no_value=True)
    config.read(file_name)
    config.optionxform = str
    config['Option'] = ast.literal_eval(str(dictionary_str))
    with open(file_name, "w") as f:
        config.write(f)


# create or reset config
def create_config():
    config = configparser.ConfigParser(allow_no_value=True)
    config['Option'] = default_value
    with open(file_name, "w") as f:
        config.write(f)


# read value from config
def read_config():
    if os.path.exists(file_name):
        # Read config from a file
        config = configparser.ConfigParser(allow_no_value=True)
        config.read(file_name)
        config_dict = dict(config['Option'])
        return config_dict
    else:
        create_config()


# Check value type when get value
def get_config():
    try:
        check_condition()
    except Exception as e:
        create_config()
    finally:
        var = read_config()
        return var


# check config condition
def check_condition():  # FIXME need to change condition
    values = read_config()
    for i in default_value:
        if i not in values:
            raise Exception()
    float(values.get('width'))
    float(values.get('focal'))
    float(values.get('distance'))
    float(values.get('range'))
    int(values.get('camera'))
    float(values.get('speed'))
    float(values.get('position'))
    float(values.get('idle'))
    float(values.get('rest'))
    float(values.get('scaling'))
    a = values.get('background') == 'True' or values.get('background') == 'False'
    b = values.get('notifications') == 'True' or values.get('notifications') == 'False'
    c = values.get('init') == 'True' or values.get('init') == 'False'
    d = values.get('appearance') == 'System' or values.get('appearance') == 'Light' or \
        values.get('appearance') == 'Dark'
    e = values.get('scaling') == 1.2 or values.get('scaling') == 1.1 or values.get('scaling') == 1.0 \
        or values.get('scaling') == 0.9 or values.get('scaling') == 0.8
    if not (a or b or c or d or e):
        raise Exception()
