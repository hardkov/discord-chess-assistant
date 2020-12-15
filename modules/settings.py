import json

global config_filename

def load_config():
    global config_filename
    f = open(config_filename)

    config = json.load(f)
    f.close()

    return config

def install_data(dir):
    pass

def dump_all_keywords(filename, intents):
    pass