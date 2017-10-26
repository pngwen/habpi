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
import sys
from glob import glob
from threading import Thread

#set some experiment path stuff
sys.path.append(directories['root'])
sys.path.append(directories['root']+'/experiments')

def runExperiment(fname):
    fname = fname.split('.')[0]
    __import__(fname)


def run():
    global sense, experiment_threads, directories, Thread
    while not start[0]:
        time.sleep(0.01)

    sense.show_letter('S', [0,0,0], [255,0,0])
    for script in glob(directories['root']+"/experiments/*.py"):
        script = script.split('/')[-1]
        print script
        experiment_threads.append(Thread(target=runExperiment, args=(script,)))
    time.sleep(1)

    #set up the data directory
    dataDir=directories['root']+"/data/"+time.strftime('%Y-%m-%d-%s')
    os.mkdir(dataDir)
    directories['dataDir'] = dataDir

    for t in experiment_threads:
        t.start()
    sense.show_letter('R', [0,0,0], [0,255,0])
    time.sleep(2)
    sense.clear()
