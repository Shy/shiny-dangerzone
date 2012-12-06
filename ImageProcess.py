import Image,ImageChops
import pygame
import pygame.camera
from pygame.locals import *

#Image Save Paths - Need to shift to a config file
intial = '/home/thelonelygod/Documents/shiny-dangerzone/Start.jpg'
second =  '/home/thelonelygod/Documents/shiny-dangerzone/img1.jpg'

class Capture:
        def main(self,cam):
                cam.start()
                
		image = cam.get_image()
                pygame.image.save(image,intial)
        
		cam.stop()
        def compare(self,img1,img2):            
                img = ImageChops.difference(img1,img2)
                xsize , ysize = img.size

                for s in range(0,xsize/3):
                        s=s*3
                        for m in range (0,ysize/3):
                                m=m*3
                                img.getpixel((s,m))     
                                if g > 150:
                                        return True
                return False                    
        def switch(self):
                second.save(intial)
        def mainComp(self,cam):
                cam.start()
                image = cam.get_image()
                pygame.image.save(image,second)
                cam.stop()
                
                img1 = Image.open(intial)
                img2 = Image.open(second)
                return self.compare (img1,img2)              