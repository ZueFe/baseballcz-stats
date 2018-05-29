# Baseball.cz - stats (Local)
This repo serves to offer data scraping and analysis from web page http://baseball.cz . It mainly focuses on automatically downloading the stats CSVs and working with the downloaded data. Below I describe setting up API locally.

## Requirements
The application is running on Python v.3+. It requires following libraries:

* Python 3+ (tested on 3.6)
* Pandas
* Selenium (with Firefox)

After installing Python, you can use pip to download most of the required libraries. Open command line and write

`pip install pandas`
to install Pandas and

`pip install selenium`
to instal Selenium.

### Setting up Selenium
Selenium is used to download the data from the web page by simulating the click on the "Export" button. It uses Firefox to simulate browser. It is hence required to download and install [Firefox](https://www.mozilla.org/en-US/firefox/). For Selenium to work it's also required to download **geckodriver**, please follow the instructions on the [official webpage](http://selenium-python.readthedocs.io/installation.html)

## Examples
The application offers several methods to help download and work with the data. Note that as this API is not installed into the Python download location, it is required to run python scripts from the same folder where the API is located.

**Download single CSV and save it to \data\**
```python
import download as dw
import constants as cs

# Get names of possible categories
# ['palka', 'pole', 'nadhoz', 'catcher']
print(cs.CATEGORIES)

# Download CSV, individual statistics for field 
dw.download_stats(category = cs.CATEGORIES[1])

# Download CSV, team statistics for batter
dw.download_stats(category = cs.CATEGORIES[0], team_stats = True)
```

**Load single CSV and compute statistics for single column**
```python
import stats

# Load team statistics for batter
load_team_batters()

# Get column names
print(get_headers())

# Compute statistics based on the provided headers
compute_column_statistics(get_headers()[5])
```

## Disclaimer

API is still being worked on, so there might be some incomplete documentation, bugs and confusion. Keep that in mind
