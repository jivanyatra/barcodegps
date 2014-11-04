barcodegps
==========

A tool for use with barcode scanners to make our gps programming operation easier

This is ultimately meant to be a production-ready tool for use with our company.
It waits for inputting of an IMEI and/or a SIM, then you can scrape a listing page for a validation code. The page requires authentication.

Dependencies:
* BeautifulSoup
* mechanize
* cookielib
* html2text
* python 2, in case you can't tell (i.e. you're not a python dev)
* conf.py needs to be filled out for validation
* re
* datetime

Work to do:
* manage data using sqlite3
* display data using prettytable
* get it to actually work
* fix the switch/case dictionary's function so it works
* etc etc
* not use global variables and use cleaner, leaner functions.
