import os

"""
This script contains constants used throughout other scripts.
Constant list

    * *saveDir* - directory where all downloaded files are saved. Default to ./data/
    * *CATEGORIES* - possible categories in statistics.
        * palka (batters)
        * pole (field)
        * nadhoz (pitching)
        * catcher
    * *TYPES* - types of statistics, 0 - individual, 2 - team, based on `baseball.cz <http://baseball.cz>`_ page
    * *GOOGLE_CHROME_BIN* - path to Chrome binary file
    * *CHROMEDRIVER_PATH* - path to Chrome driver
    * *USED_ENCODING* - encoding used in downloaded csv, default windows-1250
    * *SEP* - CSV separator character
    * *TEAM_BATTER* - file name for team batting statistics after renaming
    * *TEAM_FIELD* - file name for team fielding statistics after renaming
    * *TEAM_PITCHER* - file name for team pitching statistics after renaming
    * *TEAM_CATCHER* - file name for team catcher statistics after renaming
    * *IND_BATTER* - file name for individual batting statistics after renaming
    * *IND_FIELD* - file name for individual field statistics after renaming
    * *IND_PITCHER* - file name for individual pitcher statistics after renaming
    * *IND_CATCHER* - file name for individual catcher statistics after renaming
    * *URL* - URL to server where `Server <server.html>`_ script is running
"""

# SELENIUM CONSTANTS
saveDir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data")
CATEGORIES = ['palka', 'pole', 'nadhoz', 'catcher']
TYPES = {'individuální':0, "týmový":2}
GOOGLE_CHROME_BIN = '/app/.apt/usr/bin/google-chrome'
CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'

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

URL = 'https://baseballcz-stats.herokuapp.com/'
