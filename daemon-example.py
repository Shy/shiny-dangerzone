#!/usr/bin/env python

import sys, time
from daemon import Daemon
from ImageProcess import Capture

class MyDaemon(Daemon):
	def run(self):
		imgprocess = Capture()
		imgprocess.main()
		while True:
	    		test = imgprocess.mainComp()
			if test == True:
				print "Image has Changed" 
			time.sleep(15)

if __name__ == "__main__":
	daemon = MyDaemon('/home/thelonelygod/Documents/shiny-dangerzone/daemon-example.pid')
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
