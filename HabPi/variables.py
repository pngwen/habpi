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
import os
import config
import time

#set up directories
directories = {}

#Get the habpi root
directories['root'] = os.path.dirname(os.path.realpath(__file__)).split('/')
directories['root'] = '/'.join(directories['root'][:-1])

#Set up the sense hat
if config.senseEmu:
    senseMod = 'sense_emu'
else:
    senseMod = 'sense_hat'
sense = __import__(senseMod).SenseHat()


#thread list
interface_threads = []
experiment_threads = []


#data share
sensors={}

#don't start right away
start = [False]
