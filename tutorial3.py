import pygame
import math
from datetime import datetime


print("Welcome to the Agency . .")
name = input("What is your first name again?")
surName = input("What is your Last name name again?")
wage = float(input("Right, right.. Well, " + "Mr." + surName + " How much was your hourly wage?"))
birthday = input("Hmm, I see.. and one last question: when was your birthday IN Year/Day/Month?")
weeklyWage = wage * 0.6 * 40
totalWeeks = int(365 / 7)
yearlyWage = weeklyWage * totalWeeks

today = datetime.today()
birthdayVar = datetime.strptime(birthday, "%Y/%d/%m")

myAge = today.year - birthdayVar.year

myMonth = today.month - birthdayVar.month


myday = today.day - birthdayVar.day

print("Of course, how could I have forgotten!")
print("Here's your ID card then:")
print("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−")
print("-- Name: ", surName, " ", name, "        −−-------")
print("Income: ", yearlyWage, "$ / year", "-------------")
print("Birthday in:                       ----")
print(abs(myMonth), "Month,", abs(myMonth * 4), "Weeks,", abs(myday), "days-------------")
print("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−")

red = (255, 0, 0)
black = (0, 0, 0)
pygame.init()
drawing_window = pygame.display.set_mode((700,700))
drawing_window.fill((255,255,255))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.draw.circle(drawing_window, black, (350, 350), 350, 10)
    endAngle = myday / (2 * math.pi)
    pygame.draw.arc(drawing_window, red, (0, 0, 700, 700),abs(endAngle * 2 * math.pi), math.pi/2, 10)
    pygame.display.update()


