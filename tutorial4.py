# welcoming page
import boolean
print("-----------------------------------------------------------")
print("Welcome to student interactive audit!")
print("There are just a few quesiton I will need answer to get started...")
# ask basic info
name = input("What is your name?")
idNum = input("What is your student number?")
gpa = float(input("what is your gap in 12.0 scale? please enter your 9 digit student number"))

period = input("Are you a full time student?yes/no")
if period.lower() == "true":
	period = True
else: 
	period = False

#period = boolean.Usrinput()

# if statment to get the

# if yes, ask for 5 course and their average mark
if period == True:
    Course1 = input("what is your courcode your are taking now?")
    Mark1 = input("what is your percentage?")
    Course2 = input("what is your courcode your are taking now?")
    Mark2 = input("what is your percentage?")
    Course3 = input("what is your courcode your are taking now?")
    Mark3 = input("what is your percentage?")
    Course4 = input("what is your courcode your are taking now??")
    Mark4 = input("what is your percentage?")
    Course5 = input("what is your courcode your are taking now?")
    Mark5 = input("what is your percentage?")
else:
    CourseFirst = input("what is your courcode your are taking now?")
    MarkFirst = input("what is your percentage?")
    CourseSecond = input("what is your percentage?")
    MarkSecond = input("what is your percentage?")
    CourseThird = input("what is your courcode your are taking now?")
    MarkThird = input("what is your percentage?")

print("Excellent, we are processing your grade")


# Translating the gpa point in 12.0 scale to letter grade
if gpa == 12 :
	gpa = "A+"
elif gpa == 11:
	gpa = "A"
elif gpa == 10:
	gpa = "A-"
elif gpa == 9:
	gpa = "B+"
elif gpa == 8:
	gpa = "B"
elif gpa == 7:
	gpa = "B-"
elif gpa == 6:
	gpa = "C+"
elif gpa == 5:
	gpa = "C"
elif gpa == 4:
	gpa = "C-"
elif gpa == 3:
	gpa = "D+"
elif gpa == 2:
	gpa = "D"
elif gpa == 1:
	gpa = "D-"

print("-----------------------------------------------------------")
print("------------------", name, "'s Trnscript", "-------------------")
print("        	   Student Name:",name, "      ")
print("            	   Student Number:", idNum, )
print("            	   Student GPA:",gpa,"                                        ")

print("Course List:")
if period == True:
	print("                ===========================================")
	print("                =",Course1,"       =                 ",Mark1)
	print("                =",Course2,"       =                 ",Mark2)
	print("                =",Course3,"       =                 ",Mark3)
	print("                =",Course4,"       =                 ",Mark4)
	print("                =",Course5,"       =                 ",Mark5)
	print("                ===========================================")
	print("-----------------------------------------------------------")

else:
	print("                ===========================================")
	print("                =",CourseFirst,"       -                 ",MarkFirst)
	print("                =",CourseSecond,"       -                 ",MarkSecond)
	print("                =",CourseThird,"       -                 ",MarkThird)
	print("                ===========================================")
	print("-----------------------------------------------------------")












