import configparser


def get_config():
    config = configparser.ConfigParser()
    config.read('resources/properties.ini')
    return config


def get_input_file_path():
    return get_config()["FILE_PATH"]["input_file_path"]


def get_output_file_path():
    return get_config()["FILE_PATH"]["output_file_path"]

def get_rport_file_path():
    return get_config()["FILE_PATH"]["report_file_path"]




