
from comp1405_f17_assistant_a3 import *

def decision_making_function(e):  # 'e' IS THE SHAPE ARGUMENT YOU MUST PASS TO YOUR PERMITTED FUNCTIONS

	condition_for_sending_down = is_inside_a_triangle(e) and is_colored_purple(e) or is_inside_a_circle(e) and is_colored_red(e)  # REPLACE THIS COMMENT WITH YOUR CONDITION FOR SENDING SHAPE DOWN
	condition_for_sending_left = is_inside_a_pentagon(e) and is_colored_orange(e) or is_inside_a_pentagon(e) and is_colored_blue(e) or is_inside_a_square(e)  # REPLACE THIS COMMENT WITH YOUR CONDITION FOR SENDING SHAPE LEFT
	condition_for_sending_right = is_inside_a_circle(e) and is_colored_orange(e) or is_inside_a_triangle(e) and is_colored_blue(e) # REPLACE THIS COMMENT WITH YOUR CONDITION FOR SENDING SHAPE RIGHT
	
	return (condition_for_sending_down, condition_for_sending_left, condition_for_sending_right)

	
run_the_program(decision_making_function)
# This file will import things from other library
# The logical expression from line6 to 8 can now control the direction of each shapes goes
