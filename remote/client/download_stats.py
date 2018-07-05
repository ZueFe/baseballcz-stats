import constants as cs
import pandas as pd
import io
import requests
from data_CSV import *


## LOAD FILES from disk
def load_stats(params):
    csv = requests.get(cs.URL, params = params)
    df = pd.read_csv(io.StringIO(csv.content.decode(cs.USED_ENCODING)), delimiter=cs.SEP)

    last_modified = csv.headers['last-modified']
    file_name = "{}_{}".format(params['category'], team if params['type'] == 2 else "individual")

    print("File created at server at: {}".format(last_modified))
    return Data_CSV(df, last_modified, file_name)


def load_individual_batters():
    return load_stats({'category': 'bat', 'type': '0'})

def load_individual_field():
    return load_stats({'category': 'field', 'type': '0'})

def load_individual_pitchers():
    return load_stats({'category': 'pitcher', 'type': '0'})

def load_individual_catchers():
    return load_stats({'category': 'catcher', 'type': '0'})

def load_team_batters():
    return load_stats({'category': 'bat', 'type': '2'})

def load_team_fields():
    return load_stats({'category': 'field', 'type': '2'})

def load_team_pitchers():
    return load_stats({'category': 'pitcher', 'type': '2'})

def load_team_catchers():
    return load_stats({'category': 'catcher', 'type': '2'})

# Data information
def loaded_data_name():
    return "Loaded file: {}".format(file_name)

def loaded_data_date():
    return "File from {}".format(last_modified)
