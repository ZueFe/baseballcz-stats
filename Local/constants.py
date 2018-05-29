import os

# SELENIUM CONSTANTS
saveDir =   "{}\\data\\".format(os.path.dirname(os.path.realpath(__file__)))
CATEGORIES = ['palka', 'pole', 'nadhoz', 'catcher']
TYPES = {'individuální':0, "týmový":2}

# STATS_CONSTANTS
USED_ENCODING = 'windows-1250'
SEP = ';'
TEAM_BATTER = 'stats_palka_team.csv'
TEAM_FIELD = 'stats_pole_team.csv'
TEAM_PITCHER = 'stats_nadhoz_team.csv'
TEAM_CATCHER = 'stats_catcher_team.csv'
IND_BATTER = 'stats_palka_individual.csv'
IND_FIELD = 'stats_pole_individual.csv'
IND_PITCHER = 'stats_nadhoz_individual.csv'
IND_CATCHER = 'stats_catcher_individual.csv'
