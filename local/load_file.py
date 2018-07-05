import pandas as pd
import constants as cs
import data_CSV

## LOAD FILES from disk
def load_stats(file_name):
    global df
    global df_default

    df = pd.read_csv('{}{}'.format(cs.saveDir,file_name), encoding=cs.USED_ENCODING, delimiter=cs.SEP)
    df_default = df
    return data_CSV.Data_CSV(df, None, file_name)

def load_individual_batters():
    load_stats(cs.IND_BATTER)

def load_individual_field():
    load_stats(cs.IND_FIELD)

def load_individual_pitchers():
    load_stats(cs.IND_PITCHER)

def load_individual_catchers():
    load_stats(cs.IND_CATCHER)

def load_team_batters():
    load_stats(cs.TEAM_BATTER)

def load_team_fields():
    load_stats(cs.TEAM_FIELD)

def load_team_pitchers():
    load_stats(cs.TEAM_PITCHER)

def load_team_catchers():
    load_stats(cs.TEAM_CATCHER)
