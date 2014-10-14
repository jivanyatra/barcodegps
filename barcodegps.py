""" This is an application that allows us to quickly use a barcode
    scanner for inputting info into a CSV file for programming our
    GPS units. Hopefully, it will include a feature to scrape a
    website for the SOS validation post-programming (eventually).
"""

import re
#import scrape

running = True
while running:
    print "Welcome to the barcodegps app! Enter a command,\n"
    print "scan an imei/sim, or type help or ? for a list."
    inp = raw_input('==> ')
    if inp == 'q' or inp == 'quit':
        quit()
    elif inp == 'clear':
        scrape.clearlisting()
#    elif inp == regex for imei:
#        addimei()
    elif inp == '
""" Trying to do this stuff in a dictionary-based way...

inp = raw_input('==> ')

if imei:
if sim:
else:

commands: { 'clear' : scrape.clearlisting,
            'v' : validate,
            'validate' : validate,
            's' : showdata,
            'r' : removeline,
            'd' : removeline,
            'spoof' : spoofvalidation
}
validate()
showdata()
removeline()
spoofvalidation()
#example commands['spoof']()
"""
"""This function gets the return page from the scrape function, stores it
in 'data' and then parses it, searching for a line that matches the imei,
and has a GPS code of 7011, which is the SOS function button we use to
validate proper programming of units. Then, it'll store it along with the
imei and sim numbers.
"""

def parse_validation():
    data = scrape.scrape()
    for line in data:
        find = imei
        csvalue = [ x.strip() for x in line.split(',') ]
        if (csvalue[0].endswith(find) == True) and (csvalue[1] == '7011'):
            store = line

