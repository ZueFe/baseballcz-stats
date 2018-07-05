Getting Started
===============

Firstly made sure the API is correctly installed and go through `installation <installation.html>`_ process.
If the installation process was successful, open the command line in the main directory of the API and start
Python with command::

  python

Now we will discuss using *remote* module, with specification on *local* module following later.
At the end of the page we will also discuss how to set your own remote server to download
the data on your own if necessary.

Using Data from Remote server
*****************************

With the Python running in the command line, you can, for example download the individual batting statistics,
by running following commands::

  import remote.client.download_stats as dw

  # download individual batting statistics
  data = dw.load_individual_batters()

  # access downloaded data
  data.player_data

  # access summed data
  data.summed_data

  # access file name
  data.file_name

  # access time when the data was downloaded to the server
  data.last_modified

This will download the most recent individual batter statistics and prepare them in
format that can be further processed. For more options on the kind of statistics that
can be accessed please read the `download_stats <download_stats.html>`_ page.

Computing Statistics
********************

If you have data loaded in *data* variable as in the section above, you can start computing
statistics::

  import remote.client.stats

  # get number of at-bat(AB) per player
  stats.AB(data.player_data)

  # compute isolated power(ISO) for player with
  # at least 20 plate appearances
  stats.ISO(data.player_data, 20)

If you have loaded data *batters* data, but try to compute *pitcher* statistics
this may lead to an error::

  data.file_name
  # bat_individual

  stats.ERA(data.player_data)
  # AttributeError: 'NoneType' object has no attribute 'dtype'

So make sure you are always only computing valid data. Read `stats <stats_remote.html>`_
documentation page to see, which methods are available for which data.

Computing statistics returns *Series* object that contains the computed statistics
for every available player (this can either be all players, or only the players that
fulfill the minimal plate appearances requirement).
However, the result does not contain the names of the players the statistics
belong to. You can therefore associate the computed statistics with the names as follows::

  # get players at-bat
  res = stats.AB(data.player_data)

  # get names of the players associated with the computed statistics
  stats.names_to_data(data.player_data, res)

  # get names of the players associated with the computed statistics
  # and sort the data in descending order
  stats.sort_computed_data(data.player_data, res)

  # get names of the players associated with the computed statistics
  # and sort the data in ascending order
  stats.sort_computed_data(data.player_data, res, ascending = True)

For more information on statistics that can be computed via API read `stats <stats_remote.html>`_
documentation page.

Downloading Data Locally
************************

You can use *local* module to automatically download the data locally. To download
CSV files use following commands::

  import local.download as dw
  import local.constants as cs

  # download all individual statistics
  dw.download_single_stats()

  # download all team statistics
  dw.download_team_stats()

  # download all statistics
  dw.download_all()

  # download single statistic, individual batters
  dw.download_stats(category = cs.CATEGORIES[0], team_stats = False)

If successful the data should be saved in /data/ directory.

You can then load the downloaded data as *Data_CSV* class::

  import local.load_file

  # load individual batters stored in /data/ directory
  data = load_file.load_individual_batters()

This will allow you to use loaded data the same way as in the *remote* module.

Setting Up Remote Server
************************

You can also set your own server that will download the CSV data automatically
and store them to the server local drive, or FTP. The provided scripts should
allow you to easily deploy the server to any remote server with Python on it.

Use *Dockerfile* to install all required dependencies.

Script *server.py* is the main server script, that accept requests from the clients
and returns requested files, if available.

Script *worker.py* is set up to automatically download the statistics locally, and send
them to a FTP server.

For safety reason, information about the FTP server to send the data to are set locally
as environmental variables. For more information read the `Data scraping <data_scraping.html`>_
documentation page. 
