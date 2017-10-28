# ============================================================
#
# Student Name (as it appears on cuLearn): Robert Collier
# Student ID (9 digits in angle brackets): <123456789>
# Course Code (for this current semester): COMP1405A
#
# ============================================================

from comp1405_f17_assistant_a5 import *



#  THE FOLLOWING CODE HAS BEEN INCLUDED FOR DEMONSTRATION PURPOSES ONLY
# YOU MUST REPLACE THIS CODE WITH THE SPECIFIC LOOPING CONTROL STRUCTURES
#   THAT WERE ASSIGNED TO YOU BY THE ASSIGNMENT GENERATOR INSTRUCTIONS

while not am_i_standing_on(4):
    move_down()
while what_number_am_i_standing_on() != 3:
	move_right()
boolFlag = True
while True:
    move_down()
    if am_i_standing_on(4):
        break
for x in range(20):
	move_left()
while True:
    move_down()
    if am_i_standing_on(4):
        break
while True:
	move_right()
	if am_i_standing_on(3):
		break
while True:
	move_down()
	if am_i_standing_on(4):
		break
for a in range(44):
	move_left()
for b in range(1):
	move_down()
'''
i = 0 
while not am_i_standing_on(3):
	move_left()
	i = i + 1
	print(i)
'''
