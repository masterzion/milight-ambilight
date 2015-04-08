
#!/usr/bin/env python
# 
# Autor: Jairo Moreno
#
# Get One single color to represent the screen and send to Milight
# 

import gtk.gdk
import sys
import wx
import milight
import os
from ConfigParser import SafeConfigParser
from time import sleep

# Create an array of points (pixels) to be monitored
def MonitoredPoints(interval):
    app = wx.PySimpleApp()
    screensize = wx.GetDisplaySize()

    countx = screensize[0]/interval
    county = screensize[1]/interval

    monitoredpoints = []
    for x in range(0, countx):
        for y in range(0, county):
            monitoredpoints.append([x * interval, y * interval])

    return monitoredpoints

def CurrentColor(points, count):
    # get screen point colors based in
    # http://stackoverflow.com/questions/27395968/get-screen-pixel-color-linux-python3
    w = gtk.gdk.get_default_root_window()
    sz = w.get_size()
    pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB,False,8,sz[0],sz[1])
    pb = pb.get_from_drawable(w,w.get_colormap(),0,0,0,0,sz[0],sz[1])
    pixel_array = pb.get_pixels_array()

    #sum colors of all monitored pixels
    red = 0
    green = 0
    blue = 0
    for point in points:
        color = pixel_array[point[1]] [point[0]]

        red   = red + color[0]
        green = green + color[1]
        blue  = blue + color[2]

    # divide by point count
    red = red / count
    green = green / count
    blue = blue / count

    return (red, green, blue)

# load config files
app_path = os.path.dirname(os.path.realpath(__file__))

config = SafeConfigParser()
config.read( app_path + "/config.ini")

milight_hostname = config.get('MILIGHT','hostname')
milight_port     = config.getint('MILIGHT','port')
pixel_interval   = config.getint('CPU_OPTMIZATION', 'pixel_interval') # interval between pixels
time_interval    = config.getfloat('CPU_OPTMIZATION', 'time_interval') # time interval 
debug            = config.getboolean('CPU_OPTMIZATION', 'debug') # show color

points = MonitoredPoints(pixel_interval)
count = len(points)

controller = milight.MiLight({'host': milight_hostname, 'port': milight_port}, wait_duration=0) 

# main loop
while True:
    actualcolor =CurrentColor(points, count)
    milight.color_from_rgb(actualcolor[0], actualcolor[1], actualcolor[2])
    if debug :
        print   actualcolor 
    sleep(time_interval)

