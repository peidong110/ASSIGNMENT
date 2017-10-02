print("Welcome to the Agency . .")
name = input("What is your first name again?")
surName = input("What is your Last name name again?")
wage = float(input("Right, right.. Well, "+"Mr."+surName+" How much was your hourly wage?"))
birthday = input("Hmm, I see.. and one last question: when was your birthdayt IN Year/Day/Month?>")
weeklyWage = wage*0.6*40
totalWeeks = int(365 / 7)
yearlyWage = weeklyWage  * totalWeeks
from datetime import datetime
today = datetime.today()
birthdayVar = datetime.strptime(birthday,"%Y/%d/%m")

myAge = today.year - birthdayVar.year
print(myAge)

myMonth = today.month - birthdayVar.month
print(myMonth)

myday = today.day - birthdayVar.day
print(myday)
'''print("pastday",str(birthdayVar.day))
print("currentday"+str(today.day))'''

 





print("Of course, how could I have forgotten!")
print("Here's your ID card then:")
print("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−")
print("-- Name: ",surName," ",name,"        −−-------")
print("Income: ",yearlyWage,"$ / year","-------------")
print("Birthday in:                       ----")
print(abs(myMonth),"Month,",abs(myMonth*4),"Weeks,",abs(myday),"days-------------")
print("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−")
