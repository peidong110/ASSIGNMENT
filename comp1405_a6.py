# ============================================================
#
# Student Name (as it appears on cuLearn): Payton Pei
# Student ID (9 digits in angle brackets): <101065299>
# Course Code (for this current semester): COMP1405B
#
# ============================================================

#general instruction section
instruction = input("DO you need instruction?")
if instruction.lower() == "yes":
    print("Here is the way to play the game")
    print("You will be asked the input the background name")
    print("you will also need to enter the ghost name")
    print("Enter the x and y value")
# if usr dont want instruction we pass and skip to next step
else:
    pass 
usr_photo = input("which background photo do you want?")
#initization of pygame
import pygame
pygame.init()
#load any bmp format picture
background = pygame.image.load(usr_photo)
(width_background,height_background) = background.get_rect().size
window = pygame.display.set_mode((width_background,height_background))
#show the background right away to let usr to choose where to put the ghost
window.blit(background, (0,0))
pygame.display.update()
#ask specific location of ghost
usr_ghost = input("which ghost do you want?")
usr_ghost_x = int(input("where do you want the ghost for x"))
usr_ghost_y = int(input("where do you want the ghost for y")) 

ghost = pygame.image.load(usr_ghost)
(width,height) = ghost.get_rect().size
# in order to centre it we do it divide them by two
widthHalf = int(width/ 2)
heightHalf = int(height / 2 )

# boundary check 
while usr_ghost_x < 0 or usr_ghost_x > width:
    usr_ghost_x = int(input("Please re-enter a valid number for x value"))
else:
    pass
while usr_ghost_y < 0 or usr_ghost_y > height:
    usr_ghost_y = int(input("Please re-enter a valia number for y value"))
# foor loop make it transparent
for i in range(width):
    for j in range(height):
        #get the value of ghost at the width and length
        (r1,g1,b1,a1) = ghost.get_at((i,j))
        # checking if every pixel is > 0 and available 
        if ((usr_ghost_x+i-widthHalf)>=0) and ((usr_ghost_y+j-heightHalf)>=0):
            (r2,g2,b2,a2) = background.get_at((usr_ghost_x+i-widthHalf, usr_ghost_y+j-heightHalf))
        else:
            #set them all to 0
            (r2,g2,b2,a2) = (0, 0, 0, 0)
        #eliminate the pure green side in ghost picture
        if((r1, g1, b1)==(0,255,0)):
            ghost.set_at((i,j),(r2,g2,b2))
        #average of two photos
        else:
            ghost.set_at((i,j),((r1+r2)/2,(g1+g2)/2,(b1+b2)/2))

window.blit(ghost,(usr_ghost_x-widthHalf,usr_ghost_y-heightHalf))

 #after all the process then proceed with the showing the picture and it will stop only when user intend to quit
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        #terminal always report video system not initized, we add a exit func, so it will not appear that anymore
            exit()
    pygame.display.update()
