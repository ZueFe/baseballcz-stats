"""
Download statistics from server as defined in `constants.py <constants.html>`_
and store them in `Data_CSV <data_csv_remote.html>`_ class.
"""

import remote.client.constants as cs
import pandas as pd
import io
import requests
from remote.client.data_CSV import *


## LOAD FILES from remote server
def load_stats(params):
    """
    Requests data from remote server, uses *params* to identify which file
    to fetch.

    :params params: Paramters to identify, which file to fetch. Paramters - "category" (bat, field, pitcher, catcher), "type" (0, 2) with 0 being individual statistics and 2 being team statistics
    :returns: Data_CSV class with the data and information about the data
    """
    csv = requests.get(cs.URL, params = params)
    df = pd.read_csv(io.StringIO(csv.content.decode(cs.USED_ENCODING)), delimiter=cs.SEP)

    last_modified = csv.headers['last-modified']
    file_name = "{}_{}".format(params['category'], 'team' if params['type'] == '2' else "individual")

    print("File created at server at: {}".format(last_modified))
    return Data_CSV(df, last_modified, file_name)


def load_individual_batters():
    """
    Loads individual batter statistics (category = bat, type = 0)

    :returns: Data_CSV class with the data and information about the data
    """
    return load_stats({'category': 'bat', 'type': '0'})

def load_individual_field():
    """
    Loads individual field statistics (category = field, type = 0)

    :returns: Data_CSV class with the data and information about the data
    """
    return load_stats({'category': 'field', 'type': '0'})

def load_individual_pitchers():
    """
    Loads individual pitching statistics (category = pitcher, type = 0)

    :returns: Data_CSV class with the data and information about the data
    """
    return load_stats({'category': 'pitcher', 'type': '0'})

def load_individual_catchers():
    """
    Loads individual catcher statistics (category = catecher, type = 0)

    :returns: Data_CSV class with the data and information about the data
    """
    return load_stats({'category': 'catcher', 'type': '0'})

def load_team_batters():
    """
    Loads team batter statistics (category = bat, type = 2)

    :returns: Data_CSV class with the data and information about the data
    """
    return load_stats({'category': 'bat', 'type': '2'})

def load_team_fields():
    """
    Loads team fielding statistics (category = field, type = 2)

    :returns: Data_CSV class with the data and information about the data
    """
    return load_stats({'category': 'field', 'type': '2'})

def load_team_pitchers():
    """
    Loads team pitching statistics (category = pitcher, type = 2)

    :returns: Data_CSV class with the data and information about the data
    """
    return load_stats({'category': 'pitcher', 'type': '2'})

def load_team_catchers():
    """
    Loads team catcher statistics (category = catecher, type = 2)

    :returns: Data_CSV class with the data and information about the data
    """
    return load_stats({'category': 'catcher', 'type': '2'})
