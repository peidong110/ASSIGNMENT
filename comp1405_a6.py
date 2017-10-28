import pygame
pygame.init()
window = pygame.display.set_mode((800,600))
window.fill((255,255,255))

background = pygame.image.load("abandoned_plant.bmp")
ghost = pygame.image.load("ghost_with_broom.bmp")
#we are now getting the width and the height of the ghost photo by using the function below
(width,height) = ghost.get_rect().size


for i in range(width):
    for j in range(height):
        #get the value of 
        (r1,g1,b1,a1) = ghost.get_at((i,j))
        (r2,g2,b2,a2) = background.get_at((i+100,j+100))
        #eliminate the green side of ghost side
        if((r1, g1, b1)==(0,255,0)):
            ghost.set_at((i,j),(r2,g2,b2))
        else:
            ghost.set_at((i,j),((r1+r2)/2,(g1+g2)/2,(b1+b2)/2))




while True:
    window.blit(background, (0,0))
    window.blit(ghost,(100,100))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()
