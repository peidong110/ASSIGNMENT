# ============================================================
#
# Student Name (as it appears on cuLearn): Payton Pei
# Student ID (9 digits in angle brackets): <101065299>
# Course Code (for this current semester): COMP1405B
#
# ============================================================
 
#initization of the pygame
import pygame
pygame.init()
window = pygame.display.set_mode((800,600))
window.fill((255,255,255))
instructionYesOrNo = input("Do you need any instruction?yes or no")
if instructionYesOrNo.lower() == "yes":
	usr_photo = input("which background do you want? in .bmp")
	usr_ghost = input("which ghost do you want? in .bmp")

	background = pygame.image.load(usr_photo)
	ghost = pygame.image.load(usr_ghost)

else:
	background = pygame.image.load("abandoned_plant.bmp")
	ghost = pygame.image.load("ghost_with_broom.bmp")		
#we are now getting the width and the height of the ghost photo by using the function below
(width,height) = ghost.get_rect().size
while True:
	usr_ghost_x_value = int(input("where do you want to put the ghost/x value"))
	usr_ghost_y_vaule = int(input("where do you want to put the ghost/y value"))
	if usr_ghost_x_value + width > 800 or usr_ghost_y_vaule > 600:
		print("out of range")
	else:	
		break;
	 
#this is meant to scan all the ghost photo, make the rgb(0,255,255) the same as the background
#using the average value of the background and ghost can make ghost transparent
for i in range(width):
    for j in range(height):
        #get the value of 
        (r1,g1,b1,a1) = ghost.get_at((i,j))
        (r2,g2,b2,a2) = background.get_at((i+100,j+100))
        #eliminate the pure green side in ghost picture
        if((r1, g1, b1)==(0,255,0)):
            ghost.set_at((i,j),(r2,g2,b2))
        #average of two photos
        else:
            ghost.set_at((i,j),((r1+r2)/2,(g1+g2)/2,(b1+b2)/2))
 #after all the process then proceed with the showing the picture and it will stop only when user intend to quit
while True:
    window.blit(background, (0,0))
    window.blit(ghost,(usr_ghost_x_value,usr_ghost_y_vaule))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()
