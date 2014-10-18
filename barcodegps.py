""" This is an application that allows us to quickly use a barcode
    scanner for inputting info into a CSV file for programming our
    GPS units. Hopefully, it will include a feature to scrape a
    website for the SOS validation post-programming (eventually).
"""

import re
import scrape
import config
from conf.txt import *

def checkinput(input):
    commands: { 'clear' : clear,
            'v' : validate,
            'validate' : validate,
            'r' : removeline,
            'd' : removeline,
            'spoof' : spoofvalidation
            'q' : savexit
            'quit' : savexit
            'h' : help
            'help' : help
    }
    try:
        commands[input]()
    except:
        print "Invalid input. Please try something else, or ask for help."

def showdisplay():
    """This function is responsible for displaying data on screen
    using PrettyTable
    """
    print msg
    pass

def validate():
    """This function gets the return page from the scrape function, stores it
    in 'data' and then parses it, searching for a line that matches the imei,
    and has a GPS code of 7011, which is the SOS function button we use to
    validate proper programming of units. Then, it'll store it along with the
    imei and sim numbers.
    """
    date = scrape.getpage(sessionurl, uname, passw, clearurl)
    for line in data:
        find = imei
        csvalue = [ x.strip() for x in line.split(',') ]
        if (csvalue[0].endswith(find) == True) and (csvalue[1] == '7011'):
            valstr = line
        break
    # put valstr in a list or something.
    msg = "IMEI #" + find + " validated and added to table"

def clear():
    scrape.clearpage(sessionurl, uname, passw, clearurl)
    msg = "Validation listing page cleared!"

def removeline():
    """Remove a line of data, probably used when encountering a bad
    unit or a bad sim, and you need to swap units/sims.
    """
    pass

def spoofvalidation(imei):
    """This recreates the proper validation code for the argument the
    function was called with. It does NOT scrape the website for the
    actual validation code, it merely creates it as a string.
    """
    valstr = "www.spytecgps.com :$$" + imei + ",7011,//,::,,,0,54," \
             + "0,1,1672,0,8,1.0,0,0.0,0,31,1,0,0.0 "

def help():
    """This prints out the list of commands and basic things for how the
    program works.
    """

def savexit():
    pass

if __name__ == "__main__":
    running = True
    while running:
        inp = ''
        showdisplay()
        print "Welcome to the barcodegps app! Enter a command,\n"
        print "scan an imei/sim, or type help or ? for a list."
        inp = raw_input('==> ')
        #Trying to do this stuff in a dictionary-based way...
        if imei:
        if sim:
        else:
            checkinput(inp)

