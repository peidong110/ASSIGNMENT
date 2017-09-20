#import functions from pygame library
import pygame
#initializes pygame
pygame.init()
#create a window with 48*56
drawing_window = pygame.display.set_mode((48,56))

#fiil the windwo with a white colour
drawing_window.fill((255,255,255))

#draw the first purple Trapezoidal
pygame.draw.polygon(drawing_window,(131,117,175),((19,5),(25,11),(33,11),(39,5)))
#draw the second red Trapezoidal
pygame.draw.polygon(drawing_window,(166,65,77),((17,28),(11,34),(31,34),(25,28)))
#draw the green polygon
pygame.draw.polygon(drawing_window,(82,144,60),((8,5),(2,11),(2,27),(9,34),(15,28),(8,28)))
#draw the grey polygon
pygame.draw.polygon(drawing_window,(42,52,67),((40,38),(33,45),(19,45),(25,51),(33,51),(40,44)))
pygame.display.update()
pygame.image.save(drawing_window,"num#.png")
