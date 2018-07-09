"""
This class provides information about loaded data.
"""
import pandas as pd

class Data_CSV:
    """
    Store information about loaded data, last modified date and name of the file.
    To access the properties of the class access variables directly.

    Example:
        Access data about player/team::

            $ loaded = Data_CSV(data, last_modified, file_name)
            $ loaded.player_data

        Acceess information about date of the data::

            $ loaded = Data_CSV(data, last_modified, file_name)
            $ loaded.last_modified

        Access information about file name::

            $ loaded = Data_CSV(data, last_modified, file_name)
            $ loaded.file_name

    :param data: Pandas dataframe containing loaded values
    :param last_modified: String with time when data was downloaded to the server
    :param file_name: Name of the loaded file
    """
    def __init__(self, data, last_modified, file_name):
        self.player_data = data[:-1]
        self.summed_data = data.tail(1)
        self.last_modified = last_modified
        self.file_name = file_name


    def __str__(self):
        return "File name: {}, created {}".format(self.file_name, self.last_modified)

    def save_stats(self, path, encoding='windows-1250', sep=';'):
        """
        Saves loaded dataframe to given path.

        :param path: Full path to saved dataframe, along with all directories and file name ending in *.csv*.
        """
        res = pd.DataFrame(self.player_data).append(self.summed_data)
        res.to_csv(path, encoding=encoding, sep=sep, index=False)
