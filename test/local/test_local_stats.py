import os
import sys

sys.path.insert(0, os.path.abspath('.'))

import unittest
import numpy.testing as npt
import pandas as pd
import numpy as np
import local.stats as s

class TestStats(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        data = {'2B' : [0, 2, 2, 0], '3B' : [0, 1, 0, 0], 'HR' : [4, 0, 2, 0], 'H' : [6, 9, 12, 0],
        'BB' : [5, 8, 3, 0], 'PAB' : [13, 40, 73, 0], 'SA': [.5, 1.32, 3.33, .0], 'BA' : [.332, .124, .556, .0],
        'OBP' : [.012, .350, .227, .0], 'SF' : [0, 7, 3, 0], 'AB' : [17, 93, 125, 2], 'SO' : [12, 33, 29, 2],
        'HP' : [3, 8, 17, 0], 'R' : [12, 55, 23, 0], 'IP' : [20, 13.3, 0.3, 127.3], 'ERA' : [3.32, 1.55, 6.73, 0.53],
        'HB' : [12, 3, 44, 0], 'Jméno' : ['Joe', 'Bob', 'Ross', 'Luke']}
        cls.df = pd.DataFrame(data)

    def test_none(self):
        res = s.values(None, 'R')

        assert res == None

    def test_none_df(self):
        res = s.AB(None)

        assert res == None

    def test_wrong_category(self):
        res = s.values(self.df, 'Kek')

        assert res == None

    def test_min_stat_value(self):
        res = s.min_stat_values(self.df, self.df['2B'], 'IP', 15)

        assert len(res) == 2


    def test_single(self):
        res = s.single(self.df)

        assert res.dtype == 'int64'
        assert res[0] < res[1]
        npt.assert_allclose(res[0], 2)
        npt.assert_allclose(res[1], 6)
        npt.assert_allclose(res[2], 8)

    def test_BB_perct(self):
        res = s.BB_perct(self.df)

        assert res.dtype == 'float64'
        npt.assert_allclose(res[0], 5 / 13)
        npt.assert_allclose(res[1], 8 / 40)
        npt.assert_allclose(res[2], 3 / 73)

    def test_XBH(self):
        res = s.XBH(self.df)

        assert res.dtype != 'object'
        npt.assert_allclose(res[0], 4)
        npt.assert_allclose(res[1], 3)
        npt.assert_allclose(res[2], 4)

    def test_ISO(self):
        res = s.ISO(self.df, 0)

        assert res.dtype != 'object'
        assert len(res) == 4
        npt.assert_allclose(res[0], .5 - .332)
        npt.assert_allclose(res[1], 1.32 - .124)
        npt.assert_allclose(res[2], 3.33 - .556)

    def test_ISO_min_PA(self):
        res = s.ISO(self.df, 20)

        assert res.dtype != 'object'
        assert len(res) == 2

        npt.assert_allclose(res[1], 1.32 - .124)
        npt.assert_allclose(res[2], 3.33 - .556)

        with npt.assert_raises(KeyError):
            res[0]


    def test_OPS(self):
        res = s.OPS(self.df)

        assert res.dtype != 'object'
        npt.assert_allclose(res[0],.012 + .5)
        npt.assert_allclose(res[1], .350 + 1.32)
        npt.assert_allclose(res[2], .227 + 3.33)

    def test_BABIP(self):
        res = s.BABIP(self.df)

        assert res.dtype != 'object'
        npt.assert_allclose(res[0], (6-4) / (17 - 4 - 12 + 0))
        npt.assert_allclose(res[1], (9) / (93 - 33 + 7))
        npt.assert_allclose(res[2], (12 - 2) / (125 - 2 - 29 + 3))

    def test_wOBA(self):
        res = s.wOBA(self.df, 0)
        singles = s.single(self.df)

        assert res.dtype != 'object'
        npt.assert_allclose(res[0], (0.72 * 5 + 0.75 * 3 + 0.9 * singles[0] + 1.24 * 0 + 1.56 * 0 + 1.95 * 4) / 13)
        npt.assert_allclose(res[1], (0.72 * 8 + 0.75 * 8 + 0.9 * singles[1] + 1.24 * 2 + 1.56 * 1 + 1.95 * 0) / 40)
        npt.assert_allclose(res[2], (0.72 * 3 + 0.75 * 17 + 0.9 * singles[2] + 1.24 * 2 + 1.56 * 0 + 1.95 * 2) / 73)

    def test_wOBA_min_app(self):
        res = s.wOBA(self.df, 20)

        assert len(res) == 2
        with npt.assert_raises(Exception):
            res[0]

    def test_wrc(self):
        res = s.wRC(self.df, 0)

        woba = s.wOBA(self.df, 0)
        league_woba = np.mean(s.wOBA(self.df, 0))
        woba_scale = s.wOBA_scale(woba)
        lg_rtopa = np.mean(np.divide(self.df['R'], self.df['PAB']))

        assert res.dtype != 'object'
        npt.assert_allclose(res[0], (((woba[0] - league_woba) / woba_scale[0]) + lg_rtopa) * 13)
        npt.assert_allclose(res[1], (((woba[1] - league_woba) / woba_scale[1]) + lg_rtopa) * 40)
        npt.assert_allclose(res[2], (((woba[2] - league_woba) / woba_scale[2]) + lg_rtopa) * 73)
        npt.assert_allclose(res[3], 0)

    def test_wrc_min_pa(self):
        res = s.wRC(self.df, 20)

        assert len(res) == 2
        with npt.assert_raises(Exception):
            res[0]

        res = s.wRC(self.df, 10)

        assert len(res) == 3

    def test_wrc_plus(self):
        res = s.wRC_plus(self.df, 0)

        wrc = s.wRC(self.df, 0)
        lgWRC = np.mean(wrc)

        assert res.dtype != 'object'
        npt.assert_allclose(res[0], wrc[0] / lgWRC * 100)
        npt.assert_allclose(res[1], wrc[1] / lgWRC * 100)
        npt.assert_allclose(res[2], wrc[2] / lgWRC * 100)


    def test_wrc_plus_min_pa(self):
        res = s.wRC_plus(self.df, 20)

        assert len(res) == 2

    def test_WHIP(self):
        res = s.WHIP(self.df)

        assert res.dtype != 'object'
        npt.assert_allclose(res[0], (5 + 6) / 20)
        npt.assert_allclose(res[1], (8 + 9) / 13.3)
        npt.assert_allclose(res[2], (3 + 12) / 0.3)
        npt.assert_allclose(res[3], (0 + 0) / 127.3)

    def test_FIP(self):
        res = s.FIP(self.df, 0)

        lg_hr = np.mean(self.df['HR'])
        lg_bb = np.mean(self.df['BB'])
        lg_hbp = np.mean(self.df['HB'])
        lg_k = np.mean(self.df['SO'])
        lg_era = np.mean(self.df['ERA'])
        lg_ip = np.mean(self.df['IP'])

        fip_const = lg_era - ((13 * lg_hr) + (3 * (lg_bb + lg_hbp)) - (2 * lg_k)) / lg_ip

        assert res.dtype != 'object'

        npt.assert_allclose(res[0], ((13 * 4) + (3 * (5 + 12)) - (2 * 12)) / 20 + fip_const)
        npt.assert_allclose(res[1], ((13 * 0) + (3 * (8 + 3)) - (2 * 33)) / 13.3 + fip_const)
        npt.assert_allclose(res[2], ((13 * 2) + (3 * (3 + 44)) - (2 * 29)) / 0.3 + fip_const)
        npt.assert_allclose(res[3], ((13 * 0) + (3 * (0 + 0)) - (2 * 2)) /  127.3 + fip_const)

    def test_FIP_min_ip(self):
        res = s.FIP(self.df, 15)

        assert len(res) == 2

    def test_FIP_mminus(self):
        res = s.FIP_minus(self.df, 0)

        fip = s.FIP(self.df, 0)
        lgFIP = np.mean(fip)

        assert res.dtype != 'object'

        npt.assert_allclose(res[0], lgFIP / fip[0] * 100)
        npt.assert_allclose(res[1], lgFIP / fip[1] * 100)
        npt.assert_allclose(res[2], lgFIP / fip[2] * 100)
        npt.assert_allclose(res[3], lgFIP / fip[3] * 100)

    def test_FIP_mminus_min_ip(self):
        res = s.FIP_minus(self.df, 15)

        assert len(res) == 2

    def test_name_to_data(self):
        res = s.FIP(self.df, 0)

        names = s.names_to_data(self.df, res)

        assert names['Jméno'][0] == 'Joe'
        assert names['Jméno'][1] == 'Bob'
        assert names['Jméno'][2] == 'Ross'
        assert names['Jméno'][3] == 'Luke'

    def test_sort_data(self):
        res = self.df['HB']

        sort = s.sort_computed_data(self.df, res)

        for i in range(len(sort) - 1):
            ix = sort.index[i]
            ix_2 = sort.index[i+1]
            assert sort['HB'][ix] > sort['HB'][ix_2]

        assert sort.index[0] == 2
        assert sort.index[1] == 0
        assert sort.index[2] == 1
        assert sort.index[3] == 3

        assert sort['Jméno'][sort.index[0]] == 'Ross'
        assert sort['Jméno'][sort.index[1]] == 'Joe'
        assert sort['Jméno'][sort.index[2]] == 'Bob'
        assert sort['Jméno'][sort.index[3]] == 'Luke'
