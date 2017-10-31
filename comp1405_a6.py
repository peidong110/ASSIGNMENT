import pygame
pygame.init()
window = pygame.display.set_mode((800,600))
window.fill((255,255,255))
instruction = input("DO you need instruction?")
# ask the user if they need instructions, if yes print yes if no pass
if instruction.lower() == "yes":
	print("Here is the way to play the game")
	print("You will be asked the input the background name")
	print("you will also need to enter the ghost name")
	print("Enter the x and y value")
else:
	pass
#load the picture at once
usr_photo = input("which background photo do you want?")
background = pygame.image.load(usr_photo)
window.blit(background, (0,0))

usr_ghost = input("which ghost do you want?")
usr_ghost_x = int(input("where do you want the ghost for x"))
usr_ghost_y = int(input("where do you want the ghost for y"))

ghost = pygame.image.load(usr_ghost)
(width,height) = ghost.get_rect().size


while width +  usr_ghost_x > 800 or height + usr_ghost_y > 600:
	print("out of range")
else:
	pass











while True:
	pygame.display.update()
	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			pygame.quit()
	pygame.display.update()
	
