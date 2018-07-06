import pandas as pd
import local.constants as cs
from local.data_CSV import *

## LOAD FILES from disk
def load_stats(file_name):
    df = pd.read_csv('{}{}'.format(cs.saveDir,file_name), encoding=cs.USED_ENCODING, delimiter=cs.SEP)
    return Data_CSV(df, None, file_name)

def load_individual_batters():
    return load_stats(cs.IND_BATTER)

def load_individual_field():
    return load_stats(cs.IND_FIELD)

def load_individual_pitchers():
    return load_stats(cs.IND_PITCHER)

def load_individual_catchers():
    return load_stats(cs.IND_CATCHER)

def load_team_batters():
    return load_stats(cs.TEAM_BATTER)

def load_team_fields():
    return load_stats(cs.TEAM_FIELD)

def load_team_pitchers():
    return load_stats(cs.TEAM_PITCHER)

def load_team_catchers():
    return load_stats(cs.TEAM_CATCHER)
