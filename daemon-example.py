#!/usr/bin/env python
import Image,ImageChops
import pygame
import pygame.camera
from pygame.locals import *
import sys, time
from daemon import Daemon
from ImageProcess import Capture

import logging

class MyDaemon(Daemon):
        def run(self):
		logging.info("Start Up")
		pygame.init()
		pygame.camera.init()
		cam = pygame.camera.Camera("/dev/video0",(160,120))

                imgprocess = Capture()
                imgprocess.main(cam)
                while testf:
                        True = imgprocess.mainComp(cam)
                        if test == True:
                                logging.info("Image has Changed")
				test2 = imgprocess.mainComp(cam)
				if tpest2 == True:
					logging.info("Motion Confirmed")
					daemon.stop()
				else:
					logging.warning( "Second Test Fail")
                        else:
				logging.info("Image Switch")
                                imgprocess.switch()
                        time.sleep(5)

if __name__ == "__main__":
        daemon = MyDaemon('/home/thelonelygod/Documents/shiny-dangerzone/daemon-example.pid')
	logging.basicConfig(filename="/home/thelonelygod/Documents/shiny-dangerzone/shiny-dangerzone.log", level=logging.INFO)
        if len(sys.argv) == 2:
                if 'start' == sys.argv[1]:
                        daemon.start()
                elif 'stop' == sys.argv[1]:
                        daemon.stop()
                elif 'restart' == sys.argv[1]:
                        daemon.restart()
                else:
                        print "Unknown command"
                        sys.exit(2)
                sys.exit(0)
        else:
                print "usage: %s start|stop|restart" % sys.argv[0]
                sys.exit(2)