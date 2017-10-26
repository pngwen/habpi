# HabPi - A Simple Framework for High Altitude Sensing
#   Copyright (C) 2017 Robert Lowe <robert.lowe@maryvillecollege.edu>
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#   
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#   
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
from variables import *
import time
import os

fg = [255, 255, 255]
bg = [0,0,0]

def countDown():
    '''
    Counts down on the sense hat interface.  Any stick motion will cause it
    to cancel.
    '''
    global fg, bg

    #give a chance to cancel
    for i in range(3,0,-1):
        sense.show_letter(str(i), fg, bg)
        time.sleep(1)
        if getStickRelease() != 'none':
            return False
    return True


def prompt():
    '''
    Prompt the user for input
    '''
    global sense, start,fg, bg

    #wait for the user to want to start the experiments
    reverse = False
    while not start[0]:
        if reverse:
            sense.show_letter('?', fg, bg)
            reverse = False
        else:
            sense.show_letter('?', bg, fg)
            reverse = True

        d = getStickRelease()
        if d == 'down':
            start[0] = countDown()
        elif d == 'up':
            setDate()
        elif d == 'left':
            showDateTime()
        elif d == 'right':
            setTime()
        else:
            time.sleep(0.5)


def getStickRelease():
    '''Gets the first stick release event (if any)'''
    global sense,fg,bg
    
    elist = sense.stick.get_events()
    for e in elist:
        if e.action == 'released':
            return e.direction
    return 'none'


def getNum():
    '''Gets a number from the sense hat'''
    global sense,fg,bg

    num = 0
    while True:
        sense.show_letter(str(num), fg, bg)
        d = getStickRelease()
        if d == 'middle':
            sense.show_letter(str(num), bg, fg)
            time.sleep(0.5)
            return num
        elif d == 'up':
            num = (num+1)%10
        elif d == 'down':
            num = num-1
            if num<0:
                num = 9

def setDate():
    '''Set the date from the sense hat'''
    global sense,fg,bg

    sense.show_message('MM/DD/YYYY', text_colour=fg, back_colour=bg)

    #get month
    m=getNum()
    m=m*10 + getNum()

    #get day
    sense.show_letter('/', fg, bg)
    time.sleep(0.5)
    d = getNum()
    d = d*10 + getNum()

    #get year
    sense.show_letter('/', fg, bg)
    time.sleep(0.5)
    y = getNum()
    y = y*10 + getNum()
    y = y*10 + getNum()
    y = y*10 + getNum()

    #set the date
    t=time.strftime("%H:%M:%S")
    os.system("sudo date -s \"%04d-%02d-%02d %s\" 2>&1 > /dev/null"%(y, m, d, t))
    showDateTime()


def setTime():
    '''Set the time from the sense hat'''
    global sense, fg, bg

    sense.show_message('HH:MM', text_colour=fg, back_colour=bg)
    h = getNum()
    h = h*10+getNum()
    sense.show_letter(':', fg, bg)
    time.sleep(0.5)
    m = getNum()
    m = m*10 + getNum()
    os.system("sudo date -s %02d:%02d:00 2>&1 > /dev/null"%(h, m))
    showDateTime()



def showDateTime():
    '''Show the current date and time on the sense hat'''
    global sense
    sense.show_message(time.strftime('%m/%d/%Y %H:%M'), text_colour=fg, back_colour=bg)
