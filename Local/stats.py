import pandas as pd
import constants as cs

df = None
df_default = None


## LOAD FILES from disk
def load_stats(file_name):
    global df
    global df_default

    df = pd.read_csv('.\\data\\{}'.format(file_name), encoding=cs.USED_ENCODING, delimiter=cs.SEP)
    df_default = df

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

### DECORATORS
def check_loaded(func):
    def func_wrapper(*args, **kwargs):
        if df is None:
            print("No data loaded.")
            return None

        return func(*args, **kwargs)
    return func_wrapper

def check_valid_category(func):
    def func_wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            print("Category not found")
            return None
    return func_wrapper


### METHODS
@check_loaded
def get_headers():
    return df.columns.values

@check_loaded
@check_valid_category
def get_values(category):
    if category != None:
        return df[category]

@check_loaded
@check_valid_category
def compute_columns_statistics(category):
    return df[category].describe()

@check_loaded
@check_valid_category
def compute_statistics(category, rng):
    return df[category][rng[0]: rng[1]].describe()

@check_loaded
@check_valid_category
def sort_values(by_category, ascending = False):
    return df.sort_values(by = [by_category], ascending = ascending)
