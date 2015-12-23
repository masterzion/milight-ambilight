![LOGO](https://raw.githubusercontent.com/masterzion/milight-ambilight/master/imgs/migui.png)





Get One single color to represent the screen and send to MiLight/LimitlessLed Connector.

Let's make our movies and games more realistic? ;)


MiLight Ambilight In Action!!! (click to play)

[![MiLight Ambilight in Action](https://raw.githubusercontent.com/masterzion/milight-ambilight/master/imgs/youtube.png)](https://www.youtube.com/watch?v=VNhzjfAACFY)

https://www.youtube.com/watch?v=VNhzjfAACFY




---

**1) Instalation**
``` bash
sudo apt-get install python-dev python-wxtools

sudo apt-get install python-pip

sudo pip install -U numpy

sudo pip install milight
```

**2) Configuration**
``` ini
[MILIGHT]
hostname: Milight Hostname
port: Milight port

[CPU_OPTMIZATION]
pixel_interval: interval between pixels (you dont need to check all pixels )
time_interval: sleep time
debug: show current color
```

**3) Execute**
``` bash
./milight-ambilight-cmd
```


**4) GUI Interface**

``` bash
./milight-ambilight-gui
```


![GUI Interface](http://s7.postimg.org/w593zqguj/milight_gui1.png)



![GUI Interface](http://s24.postimg.org/nmwmecafp/milight_gui2.png)


**Milight Home page**

[![Milight Home page](http://cdn2.bigcommerce.com/n-d57o0b/jesswyt/products/78/images/266/milight_bulb1__74439.1404685995.220.290.jpg?c=2)](http://www.milight.com/milight-rgbw/)
