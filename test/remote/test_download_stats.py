import os
import sys

sys.path.insert(0, os.path.abspath('.'))

import unittest
import numpy.testing as npt
import remote.client.download_stats as dw

class TestDownload(unittest.TestCase):
    def test_individual_batters(self):
        df = dw.load_individual_batters()

        if df == None:
            #skip test of data was corrupted
            return True

        assert 'bat' in df.file_name
        assert 'individual' in df.file_name

    def test_individual_field(self):
        df = dw.load_individual_field()

        if df == None:
            #skip test of data was corrupted
            return True

        assert 'field' in df.file_name
        assert 'individual' in df.file_name

    def test_individual_pitchers(self):
        df = dw.load_individual_pitchers()

        if df == None:
            #skip test of data was corrupted
            return True

        assert 'pitcher' in df.file_name
        assert 'individual' in df.file_name

    def test_individual_catchers(self):
        df = dw.load_individual_catchers()

        if df == None:
            #skip test of data was corrupted
            return True

        assert 'catcher' in df.file_name
        assert 'individual' in df.file_name

    def test_team_batters(self):
        df = dw.load_team_batters()

        if df == None:
            #skip test of data was corrupted
            return True

        assert 'bat' in df.file_name
        assert 'team' in df.file_name

    def test_team_field(self):
        df = dw.load_team_fields()

        if df == None:
            #skip test of data was corrupted
            return True

        assert 'field' in df.file_name
        assert 'team' in df.file_name

    def test_team_pitchers(self):
        df = dw.load_team_pitchers()

        if df == None:
            #skip test of data was corrupted
            return True

        assert 'pitcher' in df.file_name
        assert 'team' in df.file_name

    def test_team_catcher(self):
        df = dw.load_team_catchers()

        if df == None:
            #skip test of data was corrupted
            return True

        assert 'catcher' in df.file_name
        assert 'team' in df.file_name

    def test_error(self):
        with npt.assert_raises(Exception):
            df = dw.load_stats({'category': 'not', 'type': '4'})
