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

import sys
import os
import config
from variables import *
from sense_interface import prompt
from threading import Thread
import experiments


#start the interface threads
sense_interface_thread = Thread(target=prompt)
interface_threads.append(sense_interface_thread)
sense_interface_thread.start()

experiments_thread = Thread(target=experiments.run)
interface_threads.append(experiments_thread)
experiments_thread.start()


def join_all():
    global interface_threads, experiment_threads

    for t in interface_threads:
        t.join()

    for t in experiment_thread:
        t.join()
