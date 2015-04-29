import gtk.gdk
import wx

class MilightAmbilight():

    def __init__(self):
        self.debug = False

    def MonitoredPoints(self, interval):
        app = wx.PySimpleApp()
        screensize = wx.GetDisplaySize()

        if self.debug :
            print  "\n\n"
            print  screensize
            print  'interval: ' + str(interval)


        countx = int(screensize[0] / interval / 2) # focus on screen center
        county = int(screensize[1] / interval / 2) # focus on screen center

        if self.debug :
            print  'points count: ' + str(countx) + 'x' + str(county)


        monitoredpoints = []
        for x in range(0, countx): # ignore the borders
            for y in range(0, county): # ignore the borders
                if self.debug :
                    print  " monitored points: " + str( x * interval ) + " - " + str ( y * interval )
                monitoredpoints.append([ (x + countx) * interval, (y + county)  * interval])

        self.__points = monitoredpoints
        self.__count = len( monitoredpoints )+1
        return self.__points

    def CurrentColor(self):
        # get screen point colors based in
        # http://stackoverflow.com/questions/27395968/get-screen-pixel-color-linux-python3
        w = gtk.gdk.get_default_root_window()
        sz = w.get_size()
        pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB,False,8,sz[0],sz[1])
        pb = pb.get_from_drawable(w,w.get_colormap(),0,0,0,0,sz[0],sz[1])
        pixel_array = pb.get_pixels_array()

        #sum colors of all monitored pixels
        red   = 0
        green = 0
        blue  = 0

        for point in self.__points:
            color = pixel_array[point[1]] [point[0]]
            if self.debug :
                print pixel_array[point[1]] [point[0]]

            red   = red   + color[0]
            green = green + color[1]
            blue  = blue  + color[2]

        if self.debug :
            print "======="

        # divide by point count
        red   = int ( red   / self.__count ) + 10
        green = int ( green / self.__count ) + 10
        blue  = int ( blue  / self.__count ) + 10

        return (red, green, blue)