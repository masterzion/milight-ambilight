import os
from ConfigParser import SafeConfigParser

class MilightConfig():
    def __init__(self):
            app_path = os.path.dirname(os.path.realpath(__file__))
            self.configfile = app_path + "/config.ini"
            self.config = SafeConfigParser()

            self.config.read( self.configfile )
            self.milight_hostname = self.config.get('MILIGHT','hostname')
            self.milight_port     = self.config.getint('MILIGHT','port')
            self.pixel_interval   = self.config.getint('CPU_OPTMIZATION', 'pixel_interval') # interval between pixels
            self.time_interval    = self.config.getfloat('CPU_OPTMIZATION', 'time_interval') # time interval 
            self.debug            = self.config.getboolean('CPU_OPTMIZATION', 'debug') # show color

    def save_config(self):
            self.config = SafeConfigParser()
            self.config.add_section('MILIGHT')
            self.config.set('MILIGHT',  'hostname', self.milight_hostname   )
            self.config.set('MILIGHT',  'port',     str( int(self.milight_port) ) )

            self.config.add_section('CPU_OPTMIZATION')
            self.config.set('CPU_OPTMIZATION', 'pixel_interval', str( int(self.pixel_interval) ) ) 
            self.config.set('CPU_OPTMIZATION', 'time_interval',  str(self.time_interval) )
            self.config.set('CPU_OPTMIZATION', 'debug',          str(self.debug) )

            with open(self.configfile, 'wb') as configfile:
                  self.config.write(configfile)

