######################################################################################
# Name: Jason Marxsen
# Date: 5/6/2020
# Description: Python file for creating Timelock from system clock in Python 3
######################################################################################
import pytz
import hashlib
from datetime import datetime,timedelta
from tzlocal import get_localzone
from string import ascii_letters

DEBUG = False

def timeElapsed(time, time2):
    time3 = (curtime_utc - datethen_utc).total_seconds()
    return int(time3)

def battleship(sec):
    hashed = hashlib.md5(str(sec).encode()).hexdigest()
    return hashed
    
zcu = get_localzone()
zcur = pytz.timezone(str(zcu))

curtime_unaware = datetime.now()
curtime_unaware = curtime_unaware-timedelta(microseconds=curtime_unaware.microsecond)

#If you plan to test a certain current time against a certain epoch, uncomment the next two lines
#and change manual_current to the desired current time

#manual_current = "2015 01 01 00 01 30"
#curtime_unaware = datetime.strptime(manual_current, "%Y %m %d %H %M %S")


if(DEBUG == True):
    print ("Current Time (Unaware): {}".format(curtime_unaware))

MANTIME = input()

if(MANTIME == None or len(MANTIME)<10):
    if(DEBUG == True):
        print("No valid manual epoch time given, using 12/31/1999 23:59:59 CST")
    timethen_unaware = "1999 12 31 23 59 59"
else:
    if(DEBUG == True):
        print("Valid manual epoch time found")
    timethen_unaware = MANTIME

datethen_unaware = datetime.strptime(timethen_unaware, "%Y %m %d %H %M %S")

if(DEBUG == True):
    print("Epoch Time (Unaware): {}".format(datethen_unaware))

datethen_aware = zcur.localize(datethen_unaware, is_dst = None)
curtime_aware = zcur.localize(curtime_unaware, is_dst = None)

if(DEBUG == True):
    print("Current Time (Aware): {}".format(curtime_aware))
    print("Epoch Time (Aware): {}".format(datethen_aware))

datethen_utc = datethen_aware.astimezone(pytz.utc)
curtime_utc = curtime_aware.astimezone(pytz.utc)

if(DEBUG == True):
    print("Current Time (UTC): {}".format(curtime_utc))
    print("Epoch Time (UTC): {}".format(datethen_utc))

change = timeElapsed(curtime_utc, datethen_utc)

if(DEBUG == True):    
    print("Total Seconds: {}".format(change))

change = change - change % 60

browns = battleship(change)
if(DEBUG == True):
    print("First Hash: {}".format(browns))

browns = battleship(browns)
if(DEBUG == True):
    print("Second Hash: {}".format(browns))

lcount = 0
ncount = 0
code = ""
browns = list(browns)
i=0
while (i<len(browns)):
    if(browns[i] in ascii_letters):
        lcount+=1
        code+=browns[i]
    if(lcount>=2):
        break
    i+=1

i=len(browns)-1
while (i>0):
    if(browns[i] not in ascii_letters):
        ncount+=1
        code+=browns[i]
    if(ncount>=2):
        break
    i-=1

print(code)

code+=browns[int(len(browns)-1)]
print(code)
