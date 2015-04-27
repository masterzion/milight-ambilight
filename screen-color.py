#!/usr/bin/env python
# 
# Autor: Jairo Moreno
#
# Get One single color to represent the screen and send to Milight
# 

import sys
import milight

from time import sleep
from milight_ambilight import MilightAmbilight
from milight_config import MilightConfig


# load config files
config = MilightConfig()

milight_hostname = config.milight_hostname
milight_port     = config.milight_port
pixel_interval   = config.pixel_interval
time_interval    = config.time_interval
debug            = config.debug


# load Ambilight class
myAmbilight = MilightAmbilight()
myAmbilight.debug =  debug

points = myAmbilight.MonitoredPoints(pixel_interval)
count = len(points)+1

controller = milight.MiLight({'host': milight_hostname, 'port': milight_port}, wait_duration=0) 
light = milight.LightBulb(['rgbw']) # Can specify which types of bulbs to use
controller.send(light.on(1)) # Turn on light_group lights

# main loop
while True:
    actualcolor = myAmbilight.CurrentColor(points, count)
    controller.send(light.color(milight.color_from_rgb(actualcolor[0], actualcolor[1], actualcolor[2]))) 
    if debug :
        print   actualcolor 
    sleep(config.time_interval)
