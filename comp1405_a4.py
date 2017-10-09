# we are only allowed to use make_a_guess function and ask_question functio
from comp1405_f17_assistant_a4 import *
#question bank is showing below

#decide whether it has mustache
questionMustache = ask_question("Does it have mustache?")
if questionMustache.lower() == "yes":
    questionEarring = ask_question("Does it have earring?")
    if questionEarring.lower() == "yes":
        questionPipe = ask_question("Does it have pipe?")
        if questionPipe.lower() == "yes":
            questionHat = ask_question("Does it have hat?")
            if questionHat.lower() == "yes":
                make_a_guess("Alex")
            else:
                make_a_guess("Dale")
        else:
            questionGlassFirstUse = ask_question("Does it have glass?")
            if questionGlassFirstUse.lower() == "yes":
                make_a_guess("Kelly")
            else:
                make_a_guess("Caelan")
    else:
        questionTatto = ask_question("Does it have tatto?")
        if questionTatto.lower() == "yes":
            questionHatSecondUse = ask_question("Does it have hat?")
            if questionHatSecondUse.lower() == "yes":
                make_a_guess("Amari")
            else:
                make_a_guess("Reagan")
        else:
            questionGlassSecondUse = ask_question("Does it have glass?")
            if questionGlassSecondUse.lower() == "yes":
                make_a_guess("Val")
            else:
                make_a_guess("River")
else:
    questionGlassThirdUse = ask_question("Does it have glass?")
    if questionGlassThirdUse.lower() == "yes":
        questionEyepatch = ask_question("Does it have eyepaych?")
        if questionEyepatch.lower() == "yes":
            questionHatThirdUse = ask_question("Does it have hat?")
            if questionHatThirdUse.lower() == "yer":
                make_a_guess("Daryl")
            else:
                make_a_guess("Mason")
        else:
            questionEarringSecond = ask_question("Does it have earring?")
            if questionEarringSecond.lower() == "yes":
                make_a_guess("Gabriel")
            else:
                make_a_guess("Eddie")
    else:
        questionHair = ask_question("Does it have hair?")
        if questionHair.lower() == "yes":
            questionTie = ask_question("Does it have tie?")
            if questionTie.lower() == "yes":
                make_a_guess("Frankie")
            else:
                make_a_guess("Kennedy")
        else:
            questionEarringThirdUse = ask_question("Does it have earring?")
            if questionEarringThirdUse.lower() == "yes":
                make_a_guess("Dylan")
            else:
                make_a_guess("Tyler")





