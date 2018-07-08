import os
import sys

sys.path.insert(0, os.path.abspath('.'))

import unittest
import local.download as dw

class TestDownload(unittest.TestCase):
    def test_single(self):
        dw.cleanup_dir()
        dw.download_stats()

        save_path = dw.get_saveDir()
        files = os.listdir(save_path)

        assert len(files) == 1
        assert 'individual' in files[0]
        assert 'palka' in files[0]

    def test_individual(self):
        dw.cleanup_dir()
        dw.download_single_stats()

        save_path = dw.get_saveDir()
        files = os.listdir(save_path)

        assert len(files) == 4

        for f in files:
            assert 'individual' in f

    def test_team(self):
        dw.cleanup_dir()
        dw.download_team_stats()

        save_path = dw.get_saveDir()
        files = os.listdir(save_path)

        assert len(files) == 4

        for f in files:
            assert 'team' in f

    def test_all(self):
        dw.cleanup_dir()
        dw.download_all()

        save_path = dw.get_saveDir()
        files = os.listdir(save_path)

        assert len(files) == 8

        for f in files:
            assert 'individual' in f or 'team' in f
