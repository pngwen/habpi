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


#Wifi Setup
accessPoint = False
ssid = 'SkyNet'
wpa = 'Terminat0r'
addr   = '172.24.1.1'
netmask = '255.255.255.0'
network = '172.24.1.0'
broadcast = '172.24.1.255'
dhcpStart = '172.24.1.50'
dhcpEnd = '172.24.1.55'


#Webserver Setup
port=8080

#Sense HAT Setup
senseEmu = False   #True for emulated, False for hardware
