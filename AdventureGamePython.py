# Let's start the Adventure
# These modules here are important to make some functions down the line
import os
from os import system
import time
from time import sleep
import sys


# This function makes scrolling text.
def scrollTxt (text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)

# We are gonna use some colors so lets define those

black = "\033[0;30m"
purple = "\033[0;35m"
blue = "\033[0;34m"
green = "\033[0;32m"
red = "\033[0;31m"
yellow = "\033[0;33m"
white = "\033[0;37m"

# We'll just use a print(blue) before our text output to change the colour displayed
# A few more functions that will be usefull
# The time function adds time between the dialogues or wherever
# time.sleep(1)
# The system('clear') clears the console whenever necessary


scrollTxt("You open your eyes...\n")
time.sleep(3)
scrollTxt("Still dizzy you remember what happened...")
time.sleep(1)
scrollTxt("""You lost control of the car you rented for this cursed trip around Europe
and ended up crashing it into a garden wall.""")
time.sleep(2)
os.system('clear')
scrollTxt(""" You hit your head so hard you barely remember you name.\n
Your name is....""")
time.sleep(2)
os.system('clear')

name = input()
time.sleep(2)
os.system('clear')
scrollTxt(name)
time.sleep(2)
scrollTxt("""....That's right...You feel better now.\n
You look around and see an old mansion...""")
scrollTxt("Is this a ")
print(yellow)
scrollTxt("light?")
time.sleep(2)
os.system('clear')
print(white)
scrollTxt("The flickering light on the top window makes you want to search for help in this seemingly abbandoned house...")
time.sleep(3)
os.system('clear')

# Now we have to create the rooms as functions so we can call them later on according to our needs

def Garden():
    directions = ["L","R","F","B"]
    scrollTxt("You find yourself in the middle of a garden.")

    userInput = " "

    print(blue)
    print("""In this game you can move in either directions\n
        Left, Right, Backwards and Forwards.\n
        Use the first letter of these directions to use them.""")

    while userInput not in directions:
        
        print(green)
        print("L / R / B / F ")
        print(white)
        
        userInput = input()

        if userInput == "L":

            os.system('clear')
            print("""You only see a thick garden that ends in a wall....\n
            Maybe your first idea is also the best""")

            userInput = " "
            
        elif userInput == "R":

            os.system('clear')
            print("""You only see a thick garden that ends in a wall....\n
            Maybe your first idea is also the best""")

            userInput= " "
            
        elif userInput == "B":

            os.system('clear')
            print("""You see what is left of your car and the open road...\n
            Maybe not your best idea to head that way, you think to yourself...""")

            userInput=" "
            
        elif userInput == "F":

            MainHall()
        
        else:
            print("Please enter one of the above options only")

            userInput = " "    


def MainHall():
    directions = ["L","R","F","B"]

    userInput = " "

    os.system('clear')

    scrollTxt("""You knock on the large wooden door to find no answer from the inside..
    You still need all the help you can find so you venture into the mansion..\n
    Suddently you listen to dissonant swirly noises and distrorted melodies coming
    from the thin air above you! \n""")
    print(red)
    time.sleep(1.5)
    print("SLAM")
    os.system('clear')
    print(yellow)
    scrollTxt("""The door swiftly closes behind you by some unknown force!!...\n
    Panicked (!) you look around you for a place to run to..! Where will that be?""")

    while userInput not in directions:

        print(green)
        print("L / R / F")
        print(white)

        userInput = input()

        if userInput == "L" :

            BachRoom()

        elif userInput == "R" :

            print("You cannot enter a room")
            os.system('clear')

            userInput="" 

        elif userInput == "F" :

            print("You go up the staircase")
            os.system('clear')

            userInput = ""

        elif userInput == "B" :

            print("You just saw this door shut by invisible forces! Are you even serious?")
            os.system('clear')

        else:

            print("Please enter one of the above options only")
            os.system('clear')

            userInput = " "



def BachRoom():

    directions = ["L","R","F","B"]
    userInput = " "

    os.system('clear')

    scrollTxt("""You find yourself in a small room...\n
    In the right corner of the room you see an ethereal figure playing on his ghostly organ!\n
    He turnes to you and says..""")
    os.system('clear')

    print(purple)
    scrollTxt("""The aim and final end of all music should be none other than the glory of God and the refreshment of the soul\n
    It is the special province of music to move the heart\n
    God's gift to his sorrowing creatures is a joy worthy of their destiny\n
    It cannot remain unmentioned that so many poorly equipped boys, and boys who have no talent at all for music,
    have been accepted into the school
    to date that the quality of music has necessarily declined and deteriorated""")
    time.sleep(3)
    os.system('clear')

    print(white)
    scrollTxt("""You freeze by his angry voice and can't really make sense of what you just heard...\n
    The ghost keeps playing his organ like you are his only audience...\n
    Your instincts are screaming for you to move and so you do...\n
    Where to next?""")

    while userInput not in directions:
        
        print(green)
        print("L / R / F / B")
        print(white)

        userInput = input()

        if userInput == "R" :

            print("Do you really want to meet the ghost? I wouldn't be so sure...")
            os.system('clear')

            userInput = " "

        elif userInput == "L" :

            print("The only thing you see is a library..You're not also a ghost so that's not the way")
            os.system('clear')

            userInput =" "

        elif userInput == "F" :

            print("The only thing you see is a barricated window. Can't get through that...yet")
            os.system('clear')

            userInput = " "

        elif userInput == "B" :

            print("You 'escaped' into the main hall")
            os.system('clear')
            MainHall2()

        else :
            
            print("Please enter on of the above options only")
            os.system('clear')



def MainHall2 ():
    
    directions = ["L", "F", "B", "R"]
    userInput = ""
    
    scrollTxt("""You once again venture into the main hall. Where to next?""")

    while userInput not in directions :

        print(green)
        print("L / R / F / B")
        print(white)

        userInput = input()

        if userInput == "L" :

            scrollTxt("""It seems like invisible forces can't let you go upstairs...
            Is there another purpose you must fulfill? You wonder... """)
            os.system('clear')

            userInput = " "

        elif userInput == "R" :

            print ("""The door is still shut by invisible forces...
            You are not getting out of this house so easily it seems""")
            os.system('clear')

            userInput = " "
            
        elif userInput == "B" :

            print ("""I wouldn't go back in there if I were you...""")
            os.system('clear')

            userInput = " "
        
        elif userInput == "F" :
            os.system('clear')

            BrahmsRoom()
    

        else :

            print("Please enter one of the above options only")
            os.system('clear')
    
    
def BrahmsRoom ():

    directions = ["L","R","F","B"]
    userInput = ""

    scrollTxt("""You enter a room and to your surprise you find another ghostly figure\n
    You feel you body unable to move as you listen to the bearded small man talking to you in his deep voice""")
    print(purple)
    scrollTxt("""If there is anyone in this room that I have not insulted, I beg his pardon\n
    Without craftsmanship, inspiration is a mere reed shaken in the wind\n
    The idea comes to me from outside of me
    and is like a gift
    I then take the idea and make it my own
    that is where the skill lies...
    The only true immortality lies in one's children...""")
    time.sleep(3)
    os.system('clear')

    print(white)
    scrollTxt("""You listen to the short man's words stunned, and seem to remind you of something..\n
    Do you know these figures?
    Can you recognise the anger in their words?
    No time for these thoughts..You are still scared..You need to get out..NOW!""")

    while userInput not in directions:

        print(green)
        print("L / R / F / B")
        print(white)

        userInput = input()

        if userInput == "L" :
            
            print("There's nothing but an empty wall..")
            os.system('clear')

            userInput = ""
        
        elif userInput == "R" :

            print("There's a library")
            os.system('clear')

            userInput = ""
        
        elif userInput == "F" :

            print("I know he is a ghost..but don't try to run through him please..That's a no")
            os.system('clear')

            userInput = ""

        elif userInput == "B" :

            print("You 'escape' into the main hall")
            os.system('clear')
            
            MainHall3()
        
        else :
            print("Please enter one of the above options only")
            os.system('clear')



def MainHall3 ():
    
    directions = ["L", "F", "B", "R"]
    userInput = ""
    
    scrollTxt("""You once again venture into the main hall. Where to next?""")

    while userInput not in directions :

        print(green)
        print("L / R / F / B")
        print(white)

        userInput = input()

        if userInput == "R" :

            scrollTxt("""This time it seems you can go upstairs\n
            are you close to solving the mystery? """)
            os.system('clear')

            break

        elif userInput == "L" :

            print ("""The door is still shut by invisible forces...
            You are not getting out of this house so easily it seems""")
            os.system('clear')

            userInput = " "
            
        elif userInput == "B" :

            print ("""I wouldn't go back in there if I were you...""")
            os.system('clear')

            userInput = " "
        
        elif userInput == "F" :

            os.system('clear')
            print ("""I wouldn't go back in there if I were you...""")
            
            userInput = ""

        else :

            print("Please enter one of the above options only")
            os.system('clear')
