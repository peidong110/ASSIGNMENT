import pygame, sys
from pygame.locals import *
str1 = ""


name = input("How do you want to name your store")
number = int(input("How many type of things do you want to cell"))
while number < 0:
	number = int(input("Please enter again, your number is not valid"))
else:
	pass
	
for i in range(number):
	for j in range(number):
		itemName = input("What it the name of the item")
		amount = int(input("Amount in stock"))
		price = int(input("price"))
		while amount < 0:
			amount = int(input("Please reenter a new one"))
		else:
			amount = str(amount)
		while price < 0:
			price = int(input("Please reenter a new one"))
		else:
			price = str(price)


		str1 += "Name of item:  "+itemName+"  amount in stock: "+amount+"   price:  "+price+"\n"	
print(str1)





 





pygame.init()
  
pygame.display.set_caption(name)
size = [640, 480]
screen = pygame.display.set_mode(size)
  
 
  
basicfont = pygame.font.SysFont("Times New Roman", 90)
text = basicfont.render(name,1,(41, 118,242), (255, 255, 255))
textrect = text.get_rect()
textrect.centerx = screen.get_rect().centerx
textrect.centery = screen.get_rect().centery
  
screen.fill((255, 255, 255))
screen.blit(text, textrect)
  
pygame.display.update()
  
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
