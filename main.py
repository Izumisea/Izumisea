import turtle
import time

pename = turtle.Turtle()
pen1 = turtle.Turtle()
pen2 = turtle.Turtle()
pename.hideturtle()
pen1.hideturtle()
pen2.hideturtle()
pename.up()
pen1.up()
pen2.up()


gamesc = turtle.Screen()

scorer = 0
count = 0

gamesc.title("Pythastic Quiz")
gamesc.setup(width= 1600,height= 900)

#-----------------------------------------------------------------------------------------------------------------------

class option:
    def __init__(self, option1, option2, option3, option4):
        self.option1 = option1
        self.option2 = option2
        self.option3 = option3
        self.option4 = option4

    def show(self):
        pen2.setpos(-600, 0)
        pen2.write(self.option1, font=("Arial Black", 40, "bold"))
        pen2.setpos(-600, -70)
        pen2.write(self.option2, font=("Arial Black", 40, "bold"))
        pen2.setpos(-600, -140)
        pen2.write(self.option3, font=("Arial Black", 40, "bold"))
        pen2.setpos(-600, -210)
        pen2.write(self.option4, font=("Arial Black", 40, "bold"))

#-----------------------------------------------------------------------------------------------------------------------

questions = {
"What file extension does the python language use?: ": "B",
"Which of the following is not a valid variable in Python?: ": "A",
"What was the inspiration for the name Python?: ": "A",
"How many keywords are there in python 3.7?: ": "D",
"What data type cannot hold numeric values?": "C",
"What data can be held by float": "A",
"Python is a high-level programming language": "A",
"Which of the following will get user input from the keyboard?": "B",
"Who created Python?: ": "C",
"What year was Python created?: ": "B",
}

question1 = option("A. .html", "B. .py", "C. .jpeg", "D. .pdf")
question2 = option("A. 1Variable", "B. Variable2", "C. Number_1", "D. AmazingCodes")
question3 = option("A. Monty Python's Flying Circus ", "B. The snake type named python", "C. The name python sounds cool", "D. He love Snake")
question4 = option("A. 31", "B. 32", "C. 30", "D. 33 ")
question5 = option("A. int", "B. str", "C. boolean", "D. float")
question6 = option("A. 3.14(Correct)", "B. 314", "C. Hello", "D. None of the above")
question7 = option("A. Yes(Correct)", "B. No", "C. Sometimes", "D. Maybe")
question8 = option("A. output('Enter your name here')","B. input('Enter Your Name hire:')  ", "C. print('Enter you name here: ')", "D. input'Enter your name here! : )")
question9 = option("A. Bill Gates", "B. Elon Musk", "C. Guido van Rossum", "D. Mark Zuckerburg")
question10 = option("A. 1989", "B. 1991", "C. 2000", "D. 2016")

options = [[question1], [question2], [question3], [question4], [question5], [question6], [question7], [question8], [question9], [question10]]

#-----------------------------------------------------------------------------------------------------------------------

def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        pen1.clear()
        pen1.setpos(0, 340)
        pen1.write("Score : {} ".format(correct_guesses), align="center", font=("Arial Black", 30, "bold"))
        pen2.setpos(0, 150)
        pen2.write(key, align="center", font=("Arial Black", 35, "bold"))
        for i in options[question_num-1]:
            pen2.setpos(100, 0)
            shows = i.show()
            pen2.write(shows, align="center", font=("Arial Black", 10, "bold"))
        guess = gamesc.textinput("Question", "Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)
        pen2.clear()

        correct_guesses += check_answer(questions.get(key), guess)

        question_num += 1
    pen1.clear()
    pen1.setpos(0, 340)
    pen1.write("Score : {} ".format(correct_guesses), align="center", font=("Arial Black", 30, "bold"))
    display_score(correct_guesses)

#-----------------------------------------------------------------------------------------------------------------------

def check_answer(answer, guess):

    if answer == guess:
        pen2.color("Green")
        pen2.setpos(0, 0)
        pen2.write("CORRECT!", align="center", font=("Arial Black", 100, "bold"))
        time.sleep(1)
        pen2.color("Black")
        pen2.clear()
        return 1
    elif answer != guess:
        pen2.color("Red")
        pen2.setpos(0, 0)
        pen2.write("WRONG!", align="center", font=("Arial Black", 100, "bold"))
        time.sleep(1)
        pen2.color("Black")
        pen2.clear()
        return 0

#-----------------------------------------------------------------------------------------------------------------------

def display_score(correct_guesses):
    pen2.clear()
    score = int((correct_guesses/len(questions))*100)
    pen2.write("Your score is: "+str(score)+"%", align="center", font=("Arial Black", 100, "bold"))
    pen2.setpos(0, -300)
    pen2.write("Click To Play Again", align="center", font=("Arial Black", 30, "bold"))
    gamesc.onclick(twitch)

#-----------------------------------------------------------------------------------------------------------------------

def twitch(x, y):
    global col
    pen2.clear()
    pen1.clear()
    intro2()

#-----------------------------------------------------------------------------------------------------------------------

def intro1():
    gamesc.bgpic('intro.gif')
    pen2.up()
    pen2.write("WELLCOME TO PYTHASTIC QUIZ", align="center", font=("Arial Black", 50, "bold"))
    pen2.setpos(0,-100)
    pen2.write("Click To Play", align="center", font=("Arial Black", 20, "bold"))
    gamesc.onclick(twitch)

#-----------------------------------------------------------------------------------------------------------------------

def Intro():
    gamesc.bgpic('intro.gif')
    pen2.up()
    pen2.write("WELLCOME TO PYTHASTIC QUIZ", align="center", font=("Arial Black", 50, "bold"))
    pen2.setpos(0,-100)
    pen2.write("Click To Play", align="center", font=("Arial Black", 20, "bold"))
    pen1.up()
    User = gamesc.textinput("USER INFO", "Please Enter Your Name:")
    pename.setpos(0, 380)
    pename.write("{} ".format(User), align="center", font=("Arial Black", 40, "bold"))
    pen1.setpos(0, 340)
    pen1.write("Score : {} ".format(scorer), align="center", font=("Arial Black", 30, "bold"))
    gamesc.onclick(twitch)

#-----------------------------------------------------------------------------------------------------------------------

def intro2():
    gamesc.bgpic('kaguya.gif')
    pen1.setpos(0, 340)
    pen1.write("Score : {} ".format(scorer), align="center", font=("Arial Black", 30, "bold"))
    pen2.setpos(0, 10)
    pen2.write("Play Python Quiz", align="center", font=("Arial Black", 50, "bold"))
    pen2.setpos(0, -50)
    pen2.write("YES OR NO", align="center", font=("Arial Black", 30, "bold"))
    time.sleep(1)
    ans = gamesc.textinput("Yes Or No", "Would You Like To Play? Please Enter Yes Or No")
    string = ans.lower()
    if string == "yes":
        number = 6
        pen2.clear()
        while number >= 0:
            number -=1
            pen2.clear()
            pen2.setpos(0, -120)
            pen2.write("{}".format(number), align="center", font=("Arial Black", 150, "bold"))
            time.sleep(1)
            gamesc.update()
            if number == 0:
                break
        pen2.clear()
        pen2.setpos(0, -120)
        pen2.write("GO!!", align="center", font=("Arial Black", 100, "bold"))
        time.sleep(.5)
        pen2.clear()
        new_game()

    elif string != "yes":
        pen2.clear()
        intro1()


Intro()
gamesc.mainloop()
