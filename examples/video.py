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
import picamera
import time
import os
import sys
import HabPi

#change to the data directory and make an images directory
vidDir = HabPi.directories['dataDir'] + "/video"
os.mkdir(vidDir)
os.chdir(vidDir)

#get the camera, set for max resolution
camera = picamera.PiCamera()
camera.resolution = (1280, 720)

#set orientation
camera.rotation = 180

#start the first recording
vidname="%d.h264"%(int(time.time()))
camera.start_recording(vidname, sps_timing=True)

while True:
  #record for 10 minutes then switch the file
  camera.wait_recording(600)
  vidname="%d.h264"%(int(time.time()))
  camera.split_recording(vidname, sps_timing=True)
