import Image,ImageChops
import pygame
import pygame.camera
from pygame.locals import *


class Capture:

	def getImage1(self,name):
		
		pygame.image.save(image,name)
		img = Image.open(name)

		return img

	def compare(self,img1,img2):
		img = ImageChops.difference(img1,img2)
		return img
	def main(self,name):
		pygame.init()
		pygame.camera.init()

		cam = pygame.camera.Camera("/dev/video0",(640,480))

		cam.start()

		image = cam.get_image()
		pygame.image.save(image,name)
		cam.stop()
