
#!/usr/bin/env python
# 
# Autor: Jairo Moreno
#
# Get One single color to represent the screen
# 
# TODO: Apply to python-milight

import gtk.gdk
import sys
import wx
from time import sleep

# interval between pixels
# less interval will increase the cpu usage
interval = 100


# Create an array of points (pixels) to be monitored
def MonitoredPoints(interval):
	app = wx.PySimpleApp()
	screensize = wx.GetDisplaySize()

	countx = screensize[0]/interval
	county = screensize[1]/interval
	actualcolor = (0,0,0)
	totalpoints = countx * county
	monitoredpoints = []

	for x in range(0, countx):
		for y in range(0, county):
			monitoredpoints.append([x * interval, y * interval])

	return monitoredpoints




def CurrentColor(points, pointcount):
    # get screen point colors
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
	red = red / pointcount
	green = green / pointcount
	blue = blue / pointcount

	return (red, green, blue)

points = MonitoredPoints(interval)
pointcount = len(points)


# execute each 0.1 milisecond
while True:
	actualcolor =CurrentColor(points, pointcount)
	print actualcolor
	sleep(0.1)
