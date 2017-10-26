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
import glob
import time
import sys
import HabPi

#get the sense hat
sense = HabPi.sense

#change to the data directory
os.chdir(HabPi.directories['dataDir'])

#some functions to help read from the sensors 
def read_temp_raw(device):
  if not os.path.exists(device):
    return ''

  f = open(device, 'r')
  lines = f.readlines()
  f.close()
  return lines

 
def read_temp(device):
  lines = read_temp_raw(device)
  if lines[0].strip()[-3:] != 'YES':
    return ' '
  equals_pos = lines[1].find('t=')
  if equals_pos != -1:
    temp_string = lines[1][equals_pos+2:]
    temp = float(temp_string) / 1000.0
    return temp


def read_all_temps(devices):
  temps = []
  for d in devices:
    device = d + '/w1_slave'
    temps.append(read_temp(device))
  return temps


#find the devices
base_dir = '/sys/bus/w1/devices/'
devices = glob.glob(base_dir + '28*')

#generate the short-names 
snames=[]
for d in devices:
  snames.append(d[-4:])

#create the header
fname = 'temperatures.csv'
file = open(fname, 'w')
file.write("Time, HTemp, PTemp," + ', '.join(snames))
file.write("\n")
file.close()


while True:
  temps=read_all_temps(devices)	
  file = open(fname, 'a')
  file.write(str(int(time.time()))+', ')
  file.write(str(sense.get_temperature_from_humidity())+', ')
  file.write(str(sense.get_temperature_from_pressure()))

  for t in temps:
    file.write(", ")
    file.write(str(t))
  file.write("\n")
  file.close()
  time.sleep(1)
