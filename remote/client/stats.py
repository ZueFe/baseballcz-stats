"""
Main script for computation of all the statistics. Appreciation goes to `Baseball Stats CZ <https://baseball-stat.cz>`_ for
help and explanation with different statistics and equations.
"""

import pandas as pd
import numpy as np

# Ignore divide by 0, will return NaN and be subbed for 0 later
np.seterr(divide='ignore', invalid='ignore')

### DECORATORS
def check_loaded(func):
    def func_wrapper(*args, **kwargs):
        if any([x is None for x in args]):
            print("No data loaded.")
            return None

        return func(*args, **kwargs)
    return func_wrapper

def check_valid_category(func):
    def func_wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            print("Category {} not found".format(args[0]))
            return None
    return func_wrapper

### METHODS
## BATTERS
def G(df):
    """
    Games played. Available for pitchers and batters.

    :param df: Pandas Dataframe containing parsed csv with data.
    :returns: Pandas Series with given statistics, for each player.
    """
    return values(df, "G")

def PAB(df):
    """
    Plate appearances. Counts all appearances at plate. Available for batters.

    :param df: Pandas Dataframe containing parsed csv with data.
    :returns: Pandas Series with given statistics, for each player.
    """
    return values(df ,"PAB")

# for pitchers too
def AB(df):
    """
    At bat, doesn't count sacrifice, walks and hit by pitch. Available for pitchers and batters.

    :param df: Pandas Dataframe containing parsed csv with data.
    :returns: Pandas Series with given statistics, for each player.
    """
    return values(df, "AB")

# works for pitchers too
def R(df):
    """
    Number of runs to home plate for batters, or number of allowed runs for pitchers.

    :param df: Pandas Dataframe containing parsed csv with data.
    :returns: Pandas Series with given statistics, for each player.
    """
    return values(df, "R")

# also used for pitchers
def H(df):
    """
    Number of hits for batters, or number of hits allowed for pitchers.

    :param df: Pandas Dataframe containing parsed csv with data.
    :returns: Pandas Series with given statistics, for each player.
    """
    res = values(df, "H")
    return change_type(res, 'int64')

#also used for pitchers
def double(df):
    """
    Number of double hits for batters, or number of doubles allowed for pitchers.

    :param df: Pandas Dataframe containing parsed csv with data.
    :returns: Pandas Series with given statistics, for each player.
    """
    return values(df, "2B")

#also used for pitchers
def triple(df):
    """
    Number of triple hits for batters, or number of triples allowed for pitchers.

    :param df: Pandas Dataframe containing parsed csv with data.
    :returns: Pandas Series with given statistics, for each player.
    """
    return values(df, "3B")

#also used for pitchers
def single(df):
    """
    Number of single hits for batters, or number of singles allowed for pitchers.

    :param df: Pandas Dataframe containing parsed csv with data.
    :returns: Pandas Series with given statistics, for each player.
    """
    two_b = double(df)
    three_b = triple(df)
    hr = HR(df)
    h = H(df)

    res = np.subtract(h, np.add(two_b, np.add(three_b, hr)))
    res.name = '1B'

    return res

def RBI(df):
    """
    Number of batted runs, available for batters.

    :param df: Pandas Dataframe containing parsed csv with data.
    :returns: Pandas Series with given statistics, for each player.
    """
    return values(df, "RBI")

#also used for pitchers
def HR(df):
    """
    Number of home runs for batters, or number of home runs allowed per pitcher.

    :param df: Pandas Dataframe containing parsed csv with data.
    :returns: Pandas Series with given statistics, for each player.
    """
    res = values(df, "HR")
    return change_type(res, 'int64')

#also for catchers
def SB(df):
    """
    Number of stolen bases for batters, or catchers.

    :param df: Pandas Dataframe containing parsed csv with data.
    :returns: Pandas Series with given statistics, for each player.
    """
    return values(df, "SB")

#also for catcher
def CS(df):
    """
    Number of times caught stealing base for batters, or number of players caught stealing for catchers.

    :param df: Pandas Dataframe containing parsed csv with data.
    :returns: Pandas Series with given statistics, for each player.
    """
    return change_type(values(df, "CS"), 'int64')

#SBA in data
def SB_perct(df):
    """
    Percentage of successfully stolen bases. Available for pitchers.

    :param df: Pandas Dataframe containing parsed csv with data.
    :returns: Pandas Series with given statistics, for each player.
    """
    res = values(df, "SBA")
    return change_type(res, 'float64')

#for pitchers too
def BB(df):
    """
    Number free bases for batters, or number of free bases given by pitchers.

    :param df: Pandas Dataframe containing parsed csv with data.
    :returns: Pandas Series with given statistics, for each player.
    """
    return values(df, 'BB')

def BB_perct(df):
    """
    Percentage of free bases to plate appearances. Available for batters.

    :param df: Pandas Dataframe containing parsed csv with data.
    :returns: Pandas Series with given statistics, for each player. NAN values are substituted for 0.
    """
    bb = BB(df)
    pa = PAB(df)

    res = np.divide(bb,pa)
    res.name = 'BB%'

    return nan_to_zero(res)

def HP(df):
    """
    Number of hit by pitch, for batters and pitchers.

    :param df: Pandas Dataframe containing parsed csv with data.
    :returns: Pandas Series with given statistics, for each player.
    """
    return values(df, 'HP')

def SH(df):
    """
    Sacrificial hit. Available for batters and pitchers.

    :param df: Pandas Dataframe containing parsed csv with data.
    :returns: Pandas Series with given statistics, for each player.
    """
    return values(df, 'SH')

def SF(df):
    """
    Sacrificial fly-out, available for batters.

    :param df: Pandas Dataframe containing parsed csv with data.
    :returns: Pandas Series with given statistics, for each player.
    """
    return values(df, 'SF')

def XBH(df):
    """
    Number of extra base hits for batters, or number of extra base hits allowed for pitchers.

    :param df: Pandas Dataframe containing parsed csv with data.
    :returns: Pandas Series with given statistics, for each player.
    """
    sec_b = double(df)
    third_b = triple(df)
    hr = HR(df)

    res = np.add(sec_b, np.add(third_b,hr))
    res.name = 'XBH'

    return res

def TB(df):
    """
    Total bases hit for batters.

    :param df: Pandas Dataframe containing parsed csv with data.
    :returns: Pandas Series with given statistics, for each player.
    """
    return change_type(values(df, 'TB'), 'int64')

def BA(df):
    """
    Batting average for batters and pitchers.

    :param df: Pandas Dataframe containing parsed csv with data.
    :returns: Pandas Series with given statistics, for each player.
    """
    res = values(df, 'BA')
    return change_type(res, 'float64')

#SOA in data
def KA(df):
    """
    Strikeout average. Number of strikeouts per at bad, available for batters.

    :param df: Pandas Dataframe containing parsed csv with data.
    :returns: Pandas Series with given statistics, for each player.
    """
    res = change_type(values(df, 'SOA'), 'float64')
    res.name = 'KA'
    return res


# slugging, pitchers (SLGA), batters (SLG)
def SA(df):
    """
    Slugging for batters, or slugging against for pitchers.

    :param df: Pandas Dataframe containing parsed csv with data.
    :returns: Pandas Series with given statistics, for each player.
    """
    return change_type(values(df, 'SA'), 'float64')

# works for pitchers too
def OBP(df):
    """
    On-base percentage, available for batters and pitchers.

    :param df: Pandas Dataframe containing parsed csv with data.
    :returns: Pandas Series with given statistics, for each player.
    """
    res = values(df, 'OBP')
    return change_type(res, 'float64')

def ISO(df, min_pa):
    """
    Isolated power, computed as ratio between slugging and batting average. Available for batters.

    :param df: Pandas Dataframe containing parsed csv with data.
    :returns: Pandas Series with given statistics, for each player.
    """
    filtered_df = df[df['PAB'] >= min_pa]
    slg = SA(filtered_df)
    ba = BA(filtered_df)
    res = np.subtract(slg, ba)

    res.name = 'ISO'

    return res

def OPS(df):
    """
    On-base percentage, plus slugging. Available for batters.

    :param df: Pandas Dataframe containing parsed csv with data.
    :returns: Pandas Series with given statistics, for each player.
    """
    obp = OBP(df)
    slg = SA(df)

    res = np.add(obp, slg)
    res.name = 'OPS'

    return res

def BABIP(df):
    """
    Batting average on balls in play. Available for batters.

    :param df: Pandas Dataframe containing parsed csv with data.
    :returns: Pandas Series with given statistics, for each player. NAN values are substituted for 0.
    """
    h = H(df)
    hr = HR(df)
    ab = AB(df)
    so = K(df)
    sf = SF(df)

    top = np.subtract(h, hr)
    bottom = np.add(np.subtract(np.subtract(ab, hr), so), sf)

    res = np.divide(top, bottom)
    res.name ='BABIP'

    return nan_to_zero(res)

def wOBA(df, min_pa):
    """
    Weighted on-base average. Can be adjusted to be computed only for players with certain
    number on plate appearances.

    :param df: Pandas Dataframe containing parsed csv with data.
    :param min_pa: Minimal number of plate appearances(PA). All players with smaller number of PA will be neglected from computation
    :returns: Pandas Series with given statistics, for each player. NAN values are substituted for 0.
    """
    filtered_df = df[df['PAB'] >= min_pa]
    bb = np.multiply(BB(filtered_df), 0.72)
    hp = np.multiply(HP(filtered_df), 0.75)
    one_b = np.multiply(single(filtered_df), 0.9)
    two_b = np.multiply(double(filtered_df), 1.24)
    three_b = np.multiply(triple(filtered_df), 1.56)
    hr = np.multiply(HR(filtered_df), 1.95)
    pa = PAB(filtered_df)

    res = np.add(bb, np.add(hp, np.add(one_b, np.add(two_b, np.add(three_b, hr)))))
    res = np.divide(res, pa)
    res.name = 'wOBA'

    return nan_to_zero(res)

#TODO: add oWAR, bWAR, rWAR

#WAR computation
def wRAA(df, min_pa):
    filtered_df = df[df['PAB'] >= min_pa]
    woba = wOBA(filtered_df, min_pa)
    lgwOBA = np.mean(woba)
    pa = PAB(df)[df['PAB'] >= min_pa]
    woba_scale = wOBA_scale(woba)


    res = np.multiply(np.divide(np.subtract(woba, lgwOBA), woba_scale), pa)
    res.name = 'Batted Runs'

    return nan_to_zero(res)


def wOBA_scale(woba):
    wOBA_const = 0.395606495399472

    return np.divide(woba, wOBA_const)

######
def R_to_PA(df, min_pa):
    filtered_df = df[df['PAB'] >= min_pa]
    r = R(filtered_df)
    pa = PAB(filtered_df)

    return np.mean(np.divide(r,pa))

#TODO: chcek if lgR/PA is computed correctly
def wRC(df, min_pa):
    """
    Weighted runs created. Available for batters.

    :param df: Pandas Dataframe containing parsed csv with data.
    :param min_pa: Minimal number of plate appearances(PA). All players with smaller number of PA will be neglected from computation
    :returns: Pandas Series with given statistics, for each player. NAN values are substituted for 0.
    """
    woba = wOBA(df,min_pa)
    lgwoba = np.mean(woba)
    woba_scale = wOBA_scale(woba)
    lg_r_to_pa = np.mean(R_to_PA(df, min_pa))
    pa = PAB(df)[df['PAB'] >= min_pa]

    res = np.multiply(np.add(np.divide(np.subtract(woba, lgwoba), woba_scale), lg_r_to_pa), pa)
    res.name = 'wRC'

    return nan_to_zero(res)

# taken from http://bleedcubbieblue.com
# TODO: check, doesn't work for min_pa == 0 (returns -0.0)
def wRC_plus(df, min_pa):
    """
    Weighted run created plus. 100.0 is league average. Available for batters.

    :param df: Pandas Dataframe containing parsed csv with data.
    :param min_pa: Minimal number of plate appearances(PA). All players with smaller number of PA will be neglected from computation
    :returns: Pandas Series with given statistics, for each player. NAN values are substituted for 0.
    """
    wrc = wRC(df, min_pa)
    lg_wrc = np.mean(wrc)

    res = np.multiply(np.divide(wrc, lg_wrc), 100)

    res.name = 'wRC+'

    return res


## PITCHERS
def CG(df):
    """
    Complete games. Available for pitchers.


    :param df: Pandas Dataframe containing parsed csv with data.
    :returns: Pandas Series with given statistics, for each player. NAN values are substituted for 0.
    """
    return values(df,'CG')

def W(df):
    """
    Wins. Available for pitchers.

    :param df: Pandas Dataframe containing parsed csv with data.
    :returns: Pandas Series with given statistics, for each player. NAN values are substituted for 0.
    """
    return values(df, 'W')

def L(df):
    """
    Losses. Available for pitchers.

    :param df: Pandas Dataframe containing parsed csv with data.
    :returns: Pandas Series with given statistics, for each player. NAN values are substituted for 0.
    """
    return values(df, 'L')

#SAV in data
def SV(df):
    """
    Saves. Available for pitchers.

    :param df: Pandas Dataframe containing parsed csv with data.
    :returns: Pandas Series with given statistics, for each player. NAN values are substituted for 0.
    """
    return change_type(values(df, 'SAV'), 'int64')

#data contain % so will compute this myself
def WA(df):
    """
    Win average. Available for pitchers.

    :param df: Pandas Dataframe containing parsed csv with data.
    :returns: Pandas Series with given statistics, for each player. NAN values are substituted for 0.
    """
    w = W(df)
    l = L(df)

    res = np.divide(w,np.add(w,l))
    res.name = 'WA'
    return nan_to_zero(res)

#also catchers
def IP(df):
    """
    Innings pitched. Available for pitchers and catchers.


    :param df: Pandas Dataframe containing parsed csv with data.
    :returns: Pandas Series with given statistics, for each player. NAN values are substituted for 0.
    """
    res = values(df, 'IP')
    return change_type(res, 'float64')

def BFP(df):
    """
    Number of batters pitcher pitched to. Available for pitchers.

    :param df: Pandas Dataframe containing parsed csv with data.
    :returns: Pandas Series with given statistics, for each player. NAN values are substituted for 0.
    """
    return values(df, 'BFP')

#SO in data, work for pitchers too
def K(df):
    """
    Number of strikeout. Available for batters and pitchers.

    :param df: Pandas Dataframe containing parsed csv with data.
    :returns: Pandas Series with given statistics, for each player. NAN values are substituted for 0.
    """
    res = change_type(values(df, 'SO'), 'int64')
    res.name = 'K'
    return res

def BB(df):
    """
    Bases on balls, free bases given to opponent batters. Available for pitchers.

    :param df: Pandas Dataframe containing parsed csv with data.
    :returns: Pandas Series with given statistics, for each player. NAN values are substituted for 0.
    """
    return values(df, 'BB')

def ER(df):
    """
    Earned runs. Available for pitchers.

    :param df: Pandas Dataframe containing parsed csv with data.
    :returns: Pandas Series with given statistics, for each player. NAN values are substituted for 0.
    """
    return change_type(values(df, 'ER'), 'int64')

def WP(df):
    """
    Wild pitch. Available for pitchers.

    :param df: Pandas Dataframe containing parsed csv with data.
    :returns: Pandas Series with given statistics, for each player. NAN values are substituted for 0.
    """
    return values(df, 'WP')

def HB(df):
    """
    Hit batters. Available for pitchers.

    :param df: Pandas Dataframe containing parsed csv with data.
    :returns: Pandas Series with given statistics, for each player. NAN values are substituted for 0.
    """
    return values(df, 'HB')

def ERA(df):
    """
    Earned run average. Number of runs allowed per 9 innings. Available for pitchers.

    :param df: Pandas Dataframe containing parsed csv with data.
    :returns: Pandas Series with given statistics, for each player. NAN values are substituted for 0.
    """
    res = values(df, 'ERA')
    return change_type(res, 'float64')

def WPA(df):
    """
    Wild pitches average, number of wild pitches per 9 innings. Available for pitchers.

    :param df: Pandas Dataframe containing parsed csv with data.
    :returns: Pandas Series with given statistics, for each player. NAN values are substituted for 0.
    """
    return change_type(values(df, 'WPA'), 'float64')

def WHIP(df):
    """
    Walks and hits per inning pitched. Available for pitchers.

    :param df: Pandas Dataframe containing parsed csv with data.
    :returns: Pandas Series with given statistics, for each player. NAN values are substituted for 0.
    """
    bb = BB(df)
    h = H(df)
    ip = IP(df)

    res = np.divide(np.add(bb, h),ip)
    res.name = 'WHIP'

    return nan_to_zero(res)

def K9(df):
    """
    Strikouts per 9 innings. Available for pitchers.

    :param df: Pandas Dataframe containing parsed csv with data.
    :returns: Pandas Series with given statistics, for each player. NAN values are substituted for 0.
    """
    k = K(df)
    ip = IP(df)

    res = np.divide(k, np.multiply(ip, 9))
    res.name = 'K/9'

    return nan_to_zero(res)

def BB9(df):
    """
    Bases on balls per 9 innings. Available for pitchers.

    :param df: Pandas Dataframe containing parsed csv with data.
    :returns: Pandas Series with given statistics, for each player. NAN values are substituted for 0.
    """
    bb = BB(df)
    ip = IP(df)

    res = np.divide(bb, np.multiply(ip, 9))
    res.name = 'BB/9'

    return nan_to_zero(res)

def KtoBB(df):
    """
    Ratio of strikeouts to bases on balls. Available to pitchers.

    :param df: Pandas Dataframe containing parsed csv with data.
    :returns: Pandas Series with given statistics, for each player. NAN values are substituted for 0.
    """
    bb = BB(df)
    k = K(df)

    res = np.divide(k,bb)
    res.name = 'K/BB'

    return nan_to_zero(res)

def BAA(df):
    """
    Batting average against. Available to pitchers.

    :param df: Pandas Dataframe containing parsed csv with data.
    :returns: Pandas Series with given statistics, for each player. NAN values are substituted for 0.
    """
    h = H(df)
    ip = IP(df)

    res = np.divide(h, ip)
    res.name = 'BAA'

    return nan_to_zero(res)

def OPSA(df):
    """
    On-base plus slugging average. Available to pitchers.

    :param df: Pandas Dataframe containing parsed csv with data.
    :returns: Pandas Series with given statistics, for each player. NAN values are substituted for 0.
    """
    slg = SA(df)
    obp = OBP(df)

    res = np.add(slg, obp)
    res.name = 'OPSA'

    return res

#Filter out pitchers with few IP to get proper ERA and league values
def FIP(df, min_ip):
    """
    Fielding independent pitching. Available for pitchers.

    :param df: Pandas Dataframe containing parsed csv with data.
    :param min_pa: Minimal number of plate appearances(PA). All players with smaller number of PA will be neglected from computation
    :returns: Pandas Series with given statistics, for each player. NAN values are substituted for 0.
    """
    filtered_df = df[change_type(df['IP'], 'float64') >= min_ip]

    hr = HR(filtered_df)
    bb = BB(filtered_df)
    hb = HB(filtered_df)
    k = K(filtered_df)
    ip = IP(filtered_df)

    lgERA = np.mean(ERA(filtered_df))
    lgHR = compute_league_stats(filtered_df ,'HR')
    lgBB = compute_league_stats(filtered_df, 'BB')
    lgHB = compute_league_stats(filtered_df, 'HB')
    lgK = compute_league_stats(filtered_df, 'SO')
    lgIP = compute_league_stats(filtered_df, 'IP')


    const = compute_FIP_constant(lgERA, lgHR, lgBB, lgHB, lgK, lgIP)

    res = np.add(compute_partial_FIP(hr, bb, hb, k, ip) , const)
    res.name = 'FIP'

    return res

def compute_league_stats(df, stat):
    res = values(df, stat)
    if res.dtype == 'object':
        res = change_type(res, 'float64')
    res = np.mean(res)

    return res

def compute_partial_FIP(hr, bb, hb, k, ip):
    res = np.add(bb,hb)
    res = np.multiply(res, 3)
    res_mid = np.multiply(hr, 13)
    res = np.add(res_mid, res)
    res_mid = np.multiply(k, 2)
    res = np.subtract(res, res_mid)
    res = np.divide(res, ip)

    return res

def compute_FIP_constant(era, hr, bb, hb, k, ip):
    partial_FIP = compute_partial_FIP(hr, bb, hb, k, ip)
    res = np.subtract(era, partial_FIP)

    return res

#TODO: check, doesn't work for min_ip = 0
def FIP_minus(df, min_ip):
    """
    FIP through percentage, 100.0 is league average. Available for pitchers.

    :param df: Pandas Dataframe containing parsed csv with data.
    :param min_pa: Minimal number of plate appearances(PA). All players with smaller number of PA will be neglected from computation
    :returns: Pandas Series with given statistics, for each player. NAN values are substituted for 0.
    """
    fip = FIP(df, min_ip)
    lgfip = np.mean(fip)

    res = np.multiply(np.divide(lgfip,fip), 100)
    res.name = "FIP-"

    return res

################
#FIELD

def PO(df):
    """
    Number of played outs. Available for field players.

    :param df: Pandas Dataframe containing parsed csv with data.
    :returns: Pandas Series with given statistics, for each player. NAN values are substituted for 0.
    """
    return values(df, 'PO')

def A(df):
    """
    Number of assists. Available for field players.

    :param df: Pandas Dataframe containing parsed csv with data.
    :returns: Pandas Series with given statistics, for each player. NAN values are substituted for 0.
    """
    return values(df, 'A')

def E(df):
    """
    Number of errors. Available for field players.

    :param df: Pandas Dataframe containing parsed csv with data.
    :returns: Pandas Series with given statistics, for each player. NAN values are substituted for 0.
    """
    return values(df, 'E')

def F(df):
    """
    Number of fieldings. Available for field players.

    :param df: Pandas Dataframe containing parsed csv with data.
    :returns: Pandas Series with given statistics, for each player. NAN values are substituted for 0.
    """
    return change_type(values(df, 'F'), 'int64')

def FA(df):
    """
    Number of successful actions in field to errors. Available for field players.

    :param df: Pandas Dataframe containing parsed csv with data.
    :returns: Pandas Series with given statistics, for each player. NAN values are substituted for 0.
    """
    return change_type(values(df, 'FA'), 'float64')

def EA(df):
    """
    Error average. Available for field players.

    :param df: Pandas Dataframe containing parsed csv with data.
    :returns: Pandas Series with given statistics, for each player. NAN values are substituted for 0.
    """
    return change_type(values(df, 'EA'), 'float64')

#TODO: add DEF

#################
#Catcher

def CSA(df):
    """
    Caught stealing average, shown as fraction, e.g., 0.97. Available for catchers.

    :param df: Pandas Dataframe containing parsed csv with data.
    :returns: Pandas Series with given statistics, for each player. NAN values are substituted for 0.
    """
    res = change_type(values(df, 'CSA'), 'float64')
    res = np.divide(res, 100)
    return res

def PB(df):
    """
    Number of uncatched pitches. Available for catchers.

    :param df: Pandas Dataframe containing parsed csv with data.
    :returns: Pandas Series with given statistics, for each player. NAN values are substituted for 0.
    """
    return change_type(values(df, 'PB'), 'int64')

def PBA(df):
    """
    Uncatched pitches average. Available for catchers.

    :param df: Pandas Dataframe containing parsed csv with data.
    :returns: Pandas Series with given statistics, for each player. NAN values are substituted for 0.
    """
    return change_type(values(df, 'PBA'), 'float64')

@check_loaded
def headers(df):
    """
    Shows headers of loaded Dataframe.

    :params df: Pandas Dataframe containing parsed csv with data.
    :returns: List of headers in the loaded Dataframe.
    """
    return df.columns.values

@check_loaded
@check_valid_category
def values(df, category):
    """
    Get values from the Dataframe *df* based on the given category.

    :param df: Pandas Dataframe containing parsed csv with data.
    :param category: String name of the category to be returned.
    :returns: Column with data from given category.
    """
    if category != None:
        return df[category]

@check_loaded
@check_valid_category
def compute_columns_statistics(df ,category):
    """
    Computes the basic statistics such as mean, median, percentile, var and std for given category.

    :param df: Pandas Dataframe containg parsed csv with data.
    :param category: String name of the category to compute the statistics on.
    :returns: Statistics on given category.
    """
    return df[category].describe()

@check_loaded
@check_valid_category
def compute_statistics(df, category, rng):
    """
    Computes the basic statistics such as mean, median, percentile, var and std for given category.
    Only consider entries in given range.

    :param df: Pandas Dataframe containg parsed csv with data.
    :param category: String name of the category to compute the statisics on.
    :param rng: Tuple with lower and upper range values.
    :returns: Statistics on given category for given range.
    """
    return df[category][rng[0]: rng[1]].describe()

@check_loaded
@check_valid_category
def sort_values(df, by_category, ascending = False):
    """
    Sort values in the dataframe by given category.

    :param df: Pandas dataframe containg parsed csv with data.
    :param by_category: String name of the category that is to be used to sort the data.
    :param ascending: Whether to sort data in ascending order or not.
    :returns: Pandas Dataframe with data sorted by the category.
    """
    return df.sort_values([by_category], ascending = ascending)

@check_loaded
def names_to_data(df, computed_data):
    """
    Associate values in *computed_data* Series with the names from *df* Dataframe. Paired based on indices.

    :param df: Pandas Dataframe containg parsed csv with data.
    :param compute_data: Series with computed data, such as those coming out of statistic functions.
    :returns: Pandas Dataframe with names and values of the computed data.
    """
    return pd.DataFrame({'Jméno': df['Jméno'], computed_data.name: computed_data})

def sort_computed_data(df, computed_data, ascending = False):
    """
    Sort computed data values and connect them with the names from Dataframe *df*.

    :param df: Pandas Dataframe containing parsed csv with data.
    :param computed_data: Series with computed data, such as those coming out of statistic functions.
    :param ascending: Whether to sort data in the ascending order on not.
    :returns: Pandas Dataframe with *computed_data* sorted and joined with the names of players.
    """
    merged_df = names_to_data(df, computed_data)
    sort = sort_values(merged_df, computed_data.name, ascending)
    return sort

#TODO: change type in change_type function to type of df_stat
def min_stat_values(df, df_stat, stat, min_stat_value):
    c_type = change_type(df[stat], 'float64')
    return df_stat[c_type >= min_stat_value]

# Helper functions
def create_player_data(data):
    return data.head(-1)

def create_summed_data(data):
    return data.tail(1)

# helper stat functions
def nan_to_zero(data):
    """
    Change all NaN values to 0.

    :param data: Data where the NaN values should be swapped.
    :returns: Data with NaN values swapped for 0.
    """
    return data.fillna(0)

def change_type(data, t):
    """
    Change type of the Series to given type. All ',' are changed to '.' and all '%' are erased to work with statistic computation.

    :param data: Series to change the type of.
    :param t: Type to change to.
    :returns: Series with type changed to *t*.
    """
    if data.dtype == t:
        return data
    d = data.str.replace(',', '.')
    d = d.str.replace('%', '')
    return d.astype(t)

def remove_nan(data):
    """
    Remove all NaN values from data.

    :param data: Data to remove NaN values from.
    :returns: Data with NaN values removed.
    """
    return data[np.logical_not(np.isnan(data))]
