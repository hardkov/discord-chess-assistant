import os
import re
import json

from nltk import data
data.path += [f'{os.getcwd()}/nltk_data']
from nltk.corpus import wordnet

import modules.handlers as handlers

global intents
global regex_dict

def load_intents(filename):
    global intents

    file = open(filename)
    data = json.load(file)
    file.close()

    intents = data.values()

# helper function
def produce_synonyms(word):
    synonyms = []

    for syn in wordnet.synsets(word):
        for lem in syn.lemmas():
        # Remove any special characters from synonym strings
            lem_name = re.sub('[^a-zA-Z0-9 \n\.]', ' ', lem.name())
            synonyms.append(lem_name)

    return set(synonyms)

def extend_keywords():
    global intents

    for intent in intents:
        key_words = intent['keyWords']
        extended_key_words = []

        for word in key_words:
            synonyms = produce_synonyms(word)
            extended_key_words.extend(synonyms)
            extended_key_words.append(word)

        intent['keyWords'] = set(extended_key_words)
    
def build_regex_dict():
    global regex_dict
    regex_dict = {}

    for intent in intents:
        intent_name = intent["intentName"]
        key_words = intent["keyWords"]
        intent_regex = []

        for syn in (key_words):
            intent_regex.append('.*\\b'+syn+'\\b.*')

        regex_dict[intent_name] = intent_regex

    for intent, keys in regex_dict.items():
        regex_dict[intent] = re.compile("|".join(keys))

def match_intent(message):
    global regex_dict

    matched_intents = []
    
    for intent, pattern in regex_dict.items():
        if re.search(pattern, message):
            matched_intents.append(intent)

    if not matched_intents:
        matched_intents.append("DEFAULT")

    return matched_intents

def get_intent_handler(intent_name):
    for intent in intents:
        if intent["intentName"] == intent_name:
            handler = getattr(handlers, intent["handler"])
            return handler

    return getattr(handlers, "DEFAULT_handler")