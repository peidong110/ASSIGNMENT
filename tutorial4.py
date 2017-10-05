print("-----------------------------------------------------------")
print("Welcome to student interactive audit!")
print("There are just a few quesiton I will need answer to get started...")
name = input("What is your name?")
idNum = input("What is your student number?")
gpa = input("what is your gap in 12.0 scale?")
period = input("Are you a full time student?yes/no")

if	int(gpa) > 90:
	letterGrade = "A+"	

if	period == "yes" or period == "Yes":
	print("True")
else:
	print("False")
if True:
	Course1 = input("what is your courcode your are taking now?")
	Mark1 = input("what is your percentage?")
	Course2 = input("what is your courcode your are taking now?")
	Mark2 = input("what is your percentage?")	
	Course3 =input("what is your courcode your are taking now?")
	Mark3 = input("what is your percentage?")
	Course4 = input("what is your courcode your are taking now??")
	Mark4 = input("what is your percentage?")
	Course5 =input("what is your courcode your are taking now?")
	Mark5 = input("what is your percentage?")		
	
	
	
	
else:
	Course1 = input("what is your courcode your are taking now?")
	Mark1 = input("what is your percentage?")
	Course2 = input("what is your percentage?")
	Mark2 = input("what is your percentage?")	
	Course3 =input("what is your courcode your are taking now?")
	
print("Excellent, we are processing your grade")


if True:
	MarkAve1 = int(Mark1) + int(Mark2) + int(Mark3) + int(Mark4) + int(Mark5)
	MarkAve2 = MarkAve1 / 5
if MarkAve2 > 90:
	print("A+")


print("----------------------------------------------")
print("---------------------",name,"'s Trnscript","------------------")	
print(Course1)
print(Course2)
print(Course3)
print(Course4)
print(Course5)

print("Student Name:","              ",name,"             ")
print("Student Number:",    idNum,)
print("GPA is","a+")
print("Mark Ave", MarkAve2)
