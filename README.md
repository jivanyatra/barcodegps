barcodegps
==========

This hasn't been touched in a while. I did a rewrite of this, but technically it's not longer my code, so I'm listing the changes below. The original changelog is in the blockquote and dates back to 2014 or so. My changes were made circa 2016.


### Original (and dated) info:

>A tool for use with barcode scanners to make our gps programming operation easier
>
>This is ultimately meant to be a production-ready tool for use with our company.
>It waits for inputting of an IMEI and/or a SIM, then you can scrape a listing page for a validation code. The page requires authentication.
>
>Dependencies:
>* BeautifulSoup
>* mechanize
>* cookielib
>* html2text
>* python 2, in case you can't tell (i.e. you're not a python dev)
>* conf.py needs to be filled out for validation
>* re
>* datetime
>
>Work to do:
>* manage data using sqlite3
>* display data using prettytable
>* get it to actually work
>* fix the switch/case dictionary's function so it works
>* etc etc
>* not use global variables and use cleaner, leaner functions.

### Log of context and changes:

#### This is a tool to make programming our gps devices easier. The general process used to be:

1. Scan a device IMEI into application
2. Scan a SIM into application
3. Program device
4. Press and hold SOS
5. Scrape page periodically for verification, update database with verification status.

#### The changes

- ditched the switch/case dict in favor of pythonic idioms
- Moved to python 3.5
- Used venv to stage changes
- BeautifulSoup for scraping verifications periodically
- Flask to host a barebones interface on localhost:8000
- sqlite4 for locally tracking any and all changes
- used regex for scanning IMEI and ICCIDs and inputting them correctly
- added a "closeout" button which would export or optionally email a .csv file of all added device-sim pairs
- used Py2Exe to distribute to relevant users
- moved to a proper module system with imports, no global vars, and added decently helpful routes for Flask to access historical data and do db clears, etc.
