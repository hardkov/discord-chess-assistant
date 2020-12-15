import json
import nltk
from os import path

global config_filename

def load_config():
    global config_filename
    f = open(config_filename)

    config = json.load(f)
    f.close()

    return config

def install_data(dir):
    if not path.exists("nltk_data"):
        nltk.download('wordnet', download_dir=dir)

def dump_all_keywords(filename, intents):
    pass