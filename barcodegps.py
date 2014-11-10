""" This is an application that allows us to quickly use a barcode
    scanner for inputting info into a CSV file for programming our
    GPS units. Hopefully, it will include a feature to scrape a
    website for the SOS validation post-programming (eventually).
"""

import re
import scrape
import datetime
from conf import *

msg = ''
imei = ''
sim = ''
filename = ''
date = ''
valstr = ''
imeire = r'^[0-9]{15}$'
simre = r'^[0-9]{19}F*$'


def choosefilename():
    global filename
    """Choose a filename for output, in a csv format
    """
    msg = "Please choose a filename, or press enter for default\n" 
          + "(uses today's date): "
    filename = raw_input(msg)
    if filename[-3:] != 'csv':
        filename = filename + '.csv'

    if not filename:
        filename = 'spytecgps_'+ date + '.csv'
    return filename
    
def getdate():
    global date
    date = datetime.datetime.today().strftime("%m-%d-%y")

def checkinput(input):
    commands = { 'clear' : clear,
            'v' : validate,
            'validate' : validate,
            'r' : removeline,
            'd' : removeline,
            'spoof' : spoofvalidation,
            'q' : 'exit',
            'quit' : 'exit',
            'h' : help,
            'help' : help
    }
    try:
        if commands[input] != exit:
            commands[input]()
        else:
            try:
                fh.close()
                print "file closed"
            except:
                print "file already closed"
            return True
    except:
        print "Invalid input. Please try something else, or ask for help."

def showinfo():
    """This function is responsible for displaying data on screen
    """
    global imei
    global sim
    if imei:
        print "IMEI # scanned: " + imei
    if sim:
        print "SIM # scanned: " + sim

def validate(imei):
    """This function gets the return page from the scrape function, stores it
    in 'data' and then parses it, searching for a line that matches the imei,
    and has a GPS code of 7011, which is the SOS function button we use to
    validate proper programming of units. Then, it'll store it along with the
    imei and sim numbers.
    """
    global valstr
    data = scrape.getpage(sessionurl, uname, passw, clearurl)
    for line in data:
        find = imei
        csvalue = [ x.strip() for x in line.split(',') ]
        if (csvalue[0].endswith(find) == True) and (csvalue[1] == '7011'):
            valstr = line
            print "IMEI # " + find + " validated"
            break
        else:
            print "No validation found! Try again!"

def clear():
    scrape.clearpage(sessionurl, uname, passw, clearurl)
    print "Validation listing page cleared!"

def removeline():
    """Remove a line of data, probably used when encountering a bad
    unit or a bad sim, and you need to swap units/sims.
    """
    global imei
    global sim
    global valstr
    imei = ''
    sim = ''
    valstr = ''
    print "IMEI and SIM deleted!"

def spoofvalidation(imei):
    """This recreates the proper validation code for the argument the
    function was called with. It does NOT scrape the website for the
    actual validation code, it merely creates it as a string.
    """
    global valstr
    valstr = "www.spytecgps.com :$$" + imei + ",7011,//,::,,,0,54," \
             + "0,1,1672,0,8,1.0,0,0.0,0,31,1,0,0.0 "

def help():
    """This prints out the list of commands and basic things for how the
    program works.
    """

def opensavefile(file):
    global imei
    global sim
    global valstr
    if imei and sim and valstr:
        with open(file, 'a') as fh:
            lineout = imei + ',' + sim + ',' + valstr + '\n'
            fh.write(lineout)
        imei = ''
        sim = ''
        valstr = ''
        print "IMEI, SIM, and Validation saved!"
    else:
        print "IMEI, SIM, and/or Validation missing; file not saved."
    
if __name__ == "__main__":
    getdate()
    choosefilename()
    while True:
        inp = ''
        print "Welcome to the barcodegps app! Enter a command,\n"
        print "scan an imei/sim, or type help or ? for a list."
        showinfo()
        inp = raw_input('==> ')
        #Trying to do this stuff in a dictionary-based way...
        if re.search(imeire, inp):
            global imei = str(inp)
        elif re.search(simre, inp):
            global sim = str(inp)
        else:
            checkinput(inp)
        opensavefile(filename)
    print "Exiting..."
