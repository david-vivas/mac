#Install SpoofMAC with the following lines into the CLI
#git clone git://github.com/feross/SpoofMAC.git
#cd SpoofMAC
#python setup.py install

#cd home and replace "enp0" and "wlp0" with the actual device names
#as needed after running ifconfig
#run this script with sudo:  sudo python mac.py

import os
import time

while True:
	print(os.popen("sudo spoof-mac.py randomise enp0").read())
	print(os.popen("sudo spoof-mac.py randomise wlp0").read())
	time.sleep(30)
