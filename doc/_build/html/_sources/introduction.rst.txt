Introduction
============

Idea
****

BaseballCZ-Statistics aims to provide an easy to use Python API that could be used
to automatize pipelines for statistics computation on data from `baseball.cz <http://baseball.cz>`_ data.

The API allows to either directly use the data downloaded on the remote server, or to automatically
download the current CSV files with the data locally, and further work with those.

Used Technologies
*****************

The API is build on several other Python libraries that are used to speed up the development process.

Data Download and Remote Server
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

As of now `baseball.cz <http://baseball.cz>`_ doesn't provide an easy access for automatic data download.
`Selenium <http://selenium-python.readthedocs.io/>`_ is therefore used to simulate clicking the download button on the statistics page.
The CSVs are downloaded locally and then sent to a remote FTP server.

To retrieve the data, API communicates via `requests <http://docs.python-requests.org/en/master/>`_ module with remote
`Flask <http://flask.pocoo.org/>`_ server that sends back the loaded data.

Statistics
^^^^^^^^^^

Data received from remote server are parsed into `Pandas <https://pandas.pydata.org/>`_ Dataframe. Along with the `Numpy <http://www.numpy.org/>`_
the API provides vectorized computation of requested statistics.

The API computes most statistics described at `baseball-stat.cz <http://baseball-stat.cz>`_, and can access all statistics
provided in CSV files.
