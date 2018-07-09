import os
import sys

sys.path.insert(0, os.path.abspath('.'))

import unittest
import pandas as pd
import remote.client.download_stats as dw
import remote.client.constants as cs

class TestDataCSV(unittest.TestCase):
    def test_save(self):
        data = dw.load_individual_batters()

        data.save_stats("data.csv")
        loaded_stats = pd.read_csv('data.csv', encoding=cs.USED_ENCODING, sep=';')

        os.remove('data.csv')

        assert data.player_data.equals(loaded_stats[:-1])
        assert data.summed_data.equals(loaded_stats.tail(1))
