============
Installation
============

The *baseballcz-statistics* API provides two ways to work with the data. First off, you can access
a remote server and compute the statistics without needing to download the CSV data locally.
This will use CSV files from a remote server that are downloaded daily.

The second option is to download the CSV files locally and work with the data.

Downloads
*********

As this is a Python API, make sure you have Python 3+ installed. You can download
Python from the `official <https://www.python.org/downloads/>`_ page. You can also download
`Anaconda <https://www.anaconda.com/download>`_ distribution to have some of the required
libraries installed right away.

To install the API first download the source codes from the `baseballcz-statistics.github.com <https://github.com/ZueFe/baseballcz-stats>`_
github page. You can either clone the repository, or click on the green *Clone or Download* button, then
click *Download ZIP*.

If you downloaded ZIP file, extract it to your disk.

Modules
********

There are two modules available. *Remote* module contains scripts that work with
data on the remote server. *Local* module contains scripts that allow you to download
and work with the data locally.

Required Libraries
******************

To install the required libraries, open the command line in the main directory of the
API.

If you'd like to install and use *remote* module, run the following command::

  pip install /remote/requirements.txt

If you'd like to install and use *local* module, run the following command::

  pip install /local/requirements.txt

If you are installing *local* module you will need to set up Firefox
webdriver. Please follow the instruction on `Selenium <http://selenium-python.readthedocs.io/>`_ page
to correctly set them up. BaseballCZ-Statistics currently doesn't support downloading via
other browsers.

Test Installation
*****************

To test whether all the parts of the installation process were successful, open the command
line in the main directory of the API. Then start Python interpreter by typing::

  python

and try to import a module from the API. If you installed *remote* module type::

  import remote.client.stats

or if you installed *local* module type::

  import local.stats

If you didn't encounter any errors, the API is ready to be used.
