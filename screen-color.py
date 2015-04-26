#!/usr/bin/env python
# 
# Autor: Jairo Moreno
#
# Get One single color to represent the screen and send to Milight
# 

import sys
import milight
import os

from time import sleep

from milight_ambilight import MilightAmbilight
from ConfigParser import SafeConfigParser

# load config files
app_path = os.path.dirname(os.path.realpath(__file__))

config = SafeConfigParser()
config.read( app_path + "/config.ini")

milight_hostname = config.get('MILIGHT','hostname')
milight_port     = config.getint('MILIGHT','port')
light_group      = config.getint('MILIGHT','light_group')
pixel_interval   = config.getint('CPU_OPTMIZATION', 'pixel_interval') # interval between pixels
time_interval    = config.getfloat('CPU_OPTMIZATION', 'time_interval') # time interval 
debug            = config.getboolean('CPU_OPTMIZATION', 'debug') # show color

# load Ambilight class
myAmbilight = MilightAmbilight()
myAmbilight.debug =  debug

points = myAmbilight.MonitoredPoints(pixel_interval)
count = len(points)

controller = milight.MiLight({'host': milight_hostname, 'port': milight_port}, wait_duration=0) 
light = milight.LightBulb(['rgbw']) # Can specify which types of bulbs to use
controller.send(light.on(light_group)) # Turn on light_group lights

# main loop
while True:
    actualcolor = myAmbilight.CurrentColor(points, count)
    controller.send(light.color(milight.color_from_rgb(actualcolor[0], actualcolor[1], actualcolor[2]), light_group)) # Change light_group to current color
    if debug :
        print   actualcolor 
    sleep(time_interval)
