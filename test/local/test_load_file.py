import sys
import os

sys.path.insert(0, os.path.abspath('.'))

import unittest
import numpy.testing as npt
import local.download as dw
import local.constants as cs
import local.load_file as lf

class TestLoadFile(unittest.TestCase):

    @classmethod
    def tearDownClass(cls):
        dw.cleanup_dir()

    def read_files(self, category, team_stats = False):
        dw.cleanup_dir()
        driver = dw.setup_firefox_opt()
        dw.download_stats(driver, category, team_stats)
        driver.close()

    def test_individual_batters(self):
        self.read_files(cs.CATEGORIES[0])
        df = lf.load_individual_batters()

        assert df != None
        assert 'individual' in df.file_name
        assert 'palka' in df.file_name

    def test_individual_field(self):
        self.read_files(cs.CATEGORIES[1])
        df = lf.load_individual_field()

        assert df != None
        assert 'individual' in df.file_name
        assert 'pole' in df.file_name


    def test_individual_pitcher(self):
        self.read_files(cs.CATEGORIES[2])
        df = lf.load_individual_pitchers()

        assert df != None
        assert 'individual' in df.file_name
        assert 'nadhoz' in df.file_name

    def test_individual_catchers(self):
        self.read_files(cs.CATEGORIES[3])
        df = lf.load_individual_catchers()

        assert df != None
        assert 'individual' in df.file_name
        assert 'catcher' in df.file_name


    def test_team_batters(self):
        self.read_files(cs.CATEGORIES[0], team_stats = True)
        df = lf.load_team_batters()

        assert df != None
        assert 'team' in df.file_name
        assert 'palka' in df.file_name


    def test_team_field(self):
        self.read_files(cs.CATEGORIES[1], team_stats = True)
        df = lf.load_team_fields()

        assert df != None
        assert 'team' in df.file_name
        assert 'pole' in df.file_name


    def test_team_pitchers(self):
        self.read_files(cs.CATEGORIES[2], team_stats = True)
        df = lf.load_team_pitchers()

        assert df != None
        assert 'team' in df.file_name
        assert 'nadhoz' in df.file_name


    def test_team_catcher(self):
        self.read_files(cs.CATEGORIES[3], team_stats = True)
        df = lf.load_team_catchers()

        assert df != None
        assert 'team' in df.file_name
        assert 'catcher' in df.file_name

    def test_error(self):
        with npt.assert_raises(Exception):
            lf.load_stats("a.csv")
