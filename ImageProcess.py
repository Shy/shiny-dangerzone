import Image,ImageChops
import pygame
import pygame.camera
from pygame.locals import *

start = '/home/thelonelygod/Documents/shiny-dangerzone/Start.jpg'
name =  '/home/thelonelygod/Documents/shiny-dangerzone/img1.jpg'

class Capture:
	def getImage1(self,name):	
		pygame.image.save(image,name)
		img = Image.open(name)

		return img

	def compare(self,img1,img2):		
		img = ImageChops.difference(img1,img2)
		xsize , ysize = img.size

		for s in range(0,xsize/3):
			s=s*3
			for m in range (0,ysize/3):
				m=m*3
				r,g,b = img.getpixel((s,m))	
				if g > 150:
					return True

		return False		
	
	def main(self):
		pygame.init()
		pygame.camera.init()

		cam = pygame.camera.Camera("/dev/video0",(160,120))

		cam.start()

		image = cam.get_image()
		pygame.image.save(image,start)
		cam.stop()
        def switch(self):
                start = name
	def mainComp(self):
		pygame.init()
		pygame.camera.init()

		cam = pygame.camera.Camera("/dev/video0",(160,120))

		cam.start()

		image = cam.get_image()
		pygame.image.save(image,name)
		cam.stop()
		
		img1 = Image.open(start)
		img2 = Image.open(name)
		return compare (img1,img2)		
