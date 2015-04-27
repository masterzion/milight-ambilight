#!/usr/bin/env python
import gtk
import gtk.glade
import milight
import time


from milight_config import MilightConfig
from milight_ambilight import MilightAmbilight
from multiprocessing import Process
from time import sleep


# https://github.com/jmcantrell/python-imageutils/blob/master/imageutils/color.py
def rgb16_to_rgb8(value): 
    return tuple(int(v/257.0) for v in value)



'''

    def __init__(self, controller, light, color, groups, interval):
        super(ThreadSendSingle, self).__init__()
        threading.Thread.__init__(self)
        self.controller = controller
        self.light      = light
        self.color      = color
        self.groups     = groups
        self.interval   = interval
'''


class ShowMain:
    global color
    def __init__(self):
        #Set the Glade file
        self.gladefile = "main.glade"  
        self.wTree = gtk.glade.XML(self.gladefile) 
        self.wTree.signal_connect("on_colorselection1_color_changed", self.set_color)
        self.wTree.signal_connect("on_btnSave_clicked",               self.save_config)
        self.wTree.signal_connect("gtk_main_quit", self.on_destroy)
        
    

        # get components
        self.colorselection1 = self.wTree.get_widget("colorselection1");
        self.checkBox1 = self.wTree.get_widget("checkbutton1");
        self.checkBox2 = self.wTree.get_widget("checkbutton2");
        self.checkBox3 = self.wTree.get_widget("checkbutton3");
        self.checkBox4 = self.wTree.get_widget("checkbutton4");
        self.ambilight = self.wTree.get_widget("checkambilight");

        # load config
        self.config = MilightConfig()

        self.wTree.get_widget("edtHost").set_text( self.config.milight_hostname ) 
        self.wTree.get_widget("edtPort").set_value( self.config.milight_port ) 
        self.wTree.get_widget("hscalepixel").set_value( self.config.pixel_interval );
        self.wTree.get_widget("hscaleinterval").set_value( self.config.time_interval * 1000 ) 
        self.wTree.get_widget("checkdebug").set_active( self.config.debug ) 

        # connect
        light = milight.LightBulb(['rgbw'])
        self.controller = milight.MiLight({'host': self.config.milight_hostname, 'port': self.config.milight_port}, wait_duration=0) 
        self.light = milight.LightBulb(['rgbw'])
        self.window = self.wTree.get_widget("MainWindow")



        #self.sendThread = Process(target=self.sendFunction )
        #self.sendThread.start()


        self.controller.send(light.all_on())

        if (self.window):
            self.window.connect("destroy", gtk.main_quit)


    #def sendFunction(self):
    #    while True:
    #        print self.color
    #        sleep(self.config.time_interval)



    def on_destroy(self, widget=None, *data):
        gtk.main_quit
        self.sendThread.terminate()


    def save_config(self, widget):
        self.config.milight_hostname  = self.wTree.get_widget("edtHost").get_text() 
        self.config.milight_port      = self.wTree.get_widget("edtPort").get_value() 
        self.config.pixel_interval    = self.wTree.get_widget("hscalepixel").get_value();
        self.config.time_interval     = self.wTree.get_widget("hscaleinterval").get_value() /  1000
        self.config.debug             = self.wTree.get_widget("checkdebug").get_active() 
        self.config.save_config()




    def set_color(self, widget):
        color  = self.colorselection1.get_current_color()
        colorrgb  = (color.red, color.green, color.blue)
        color = rgb16_to_rgb8( colorrgb )

        group_array = list()


        if (self.checkBox1.get_active()):
            group_array.append(1)

        if (self.checkBox2.get_active()):
            group_array.append(2)

        if (self.checkBox3.get_active()):
            group_array.append(3)

        if (self.checkBox4.get_active()):
            group_array.append(4)

        if ( len( group_array ) == 4 ) :
            self.controller.send(self.light.color(milight.color_from_rgb( color[0], color[1], color[2] ) ) )
        else :
            for group in group_array:
                self.controller.send(self.light.color( milight.color_from_rgb( color[0], color[1], color[2] ) , group)  )



if __name__ == "__main__":
    hwg = ShowMain()
    gtk.main()