#!/usr/bin/python

# usage
#
# $ scriptname domainToPing fileToWriteLogTo [numberOfPings]
#
# $ chmod +x ./testping.py
# $ ./testping.py www.google.com ping.log 100

import sys
import datetime
import commands

# default parameters
url = "www.google.com"
log = "ping.log"

loop = True
count = 0

# set passed parameters
if len(sys.argv) > 1:
    url = sys.argv[1]

if len(sys.argv) > 2:
    log = sys.argv[2]

if len(sys.argv) > 3:
    loops = int(sys.argv[3])
else:
    loops = 0  # 0 is infinte

with open(log, "a") as logfile:
    logfile.write("Pinging against " + url + " for " +
                  str(loops) + " loops and writing to " + log + "\n")
    logfile.write("Starting ping test at " +
                  str(datetime.datetime.now()) + "\n")

while loop:
    cmd = "ping -c 1 " + url
    ping = commands.getstatusoutput(cmd)

    if ping[0] != 0:
        print str(datetime.datetime.now()) + " => ping failed to " + url

        with open(log, "a") as logfile:
            logfile.write(str(datetime.datetime.now()) +
                          " => ping failed to " + url + "\n")

    if loops > 0:
        count += 1
        if count >= loops:
            loop = False
