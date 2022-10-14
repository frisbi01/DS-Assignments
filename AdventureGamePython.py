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

            print("""You only see a thick garden that ends in a wall....\n
            Maybe your first idea is also the best""")
            

            userInput = " "
            
        elif userInput == "R":

            print("""You only see a thick garden that ends in a wall....\n
            Maybe your first idea is also the best""")
            

            userInput= " "
            
        elif userInput == "B":

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

    scrollTxt("""You knock on the large wooden door to find no answer from the inside..\n""")
    time.sleep(1)
    scrollTxt("""You still need all the help you can find so you venture into the mansion..\n""")
    time.sleep(2)
    scrollTxt("""Suddently you listen to dissonant swirly noises..! And distrorted melodies are coming down
    from the thin air above you!! \n""")
    print(red)
    time.sleep(2)
    print("SLAM")
    time.sleep(1)
    print(yellow)
    scrollTxt("""The door swiftly closes behind you by some unknown force!!...\n
    Panicked (!) you look around you for a place to run to..! Where will that be?""")

    while userInput not in directions:

        print(green)
        print("L / R / F / B")
        print(white)

        userInput = input()

        if userInput == "L" :

            BachRoom()

        elif userInput == "R" :

            print("You find a room but the door is locked")
            
            userInput="" 

        elif userInput == "F" :

            print("You try to to get close to the staircase but a wind like force doesn't let you!")
            
            userInput = ""

        elif userInput == "B" :

            print("You just saw this door shut by invisible forces! Are you even serious?")

            userInput=""
            
        else:

            print("Please enter one of the above options only")
            
            userInput = " "



def BachRoom():

    directions = ["L","R","F","B"]
    userInput = " "

    os.system('clear')

    scrollTxt("""You find yourself in a small room...\n""")
    time.sleep(1)
    scrollTxt("""In the right corner of the room you see an ethereal figure playing on his ghostly organ!\n
    He turnes to you and says..\n""")
    time.sleep(3)

    print(purple)
    scrollTxt("""The aim and final end of all music should be none other than the glory of God and the refreshment of the soul\n
    It is the special province of music to move the heart\n
    It cannot remain unmentioned that so many poorly equipped boys, and boys who have no talent at all for music,
    have been accepted by all of you to date..that the quality of music has necessarily declined and deteriorated!\n""")
    time.sleep(3)
    

    print(white)
    scrollTxt("""You freeze by his angry voice and can't really make sense of what you just heard or who that was...\n
    The ghost keeps playing his organ and you are his only audience...\n
    Your instincts are screaming for you to move and so you do...\n
    Where to next?""")

    while userInput not in directions:
        
        print(green)
        print("L / R / F / B")
        print(white)

        userInput = input()

        if userInput == "R" :

            print("Do you really want to meet the ghost? I wouldn't be so sure...")

            userInput = " "

        elif userInput == "L" :

            print("The only thing you see is a library..You're not also a ghost so that's not the way")

            userInput =" "

        elif userInput == "F" :

            print("The only thing you see is a barricated window. Can't get through that...")

            userInput = " "

        elif userInput == "B" :

            print("You 'escaped' into the main hall")
    
            MainHall2()

        else :
            
            print("Please enter on of the above options only")
        

            userInput = ""



def MainHall2 ():
    
    directions = ["L", "F", "B", "R"]
    userInput = ""
    os.system('clear')

    scrollTxt("""You once again venture into the main hall. Where to next?""")

    while userInput not in directions :

        print(green)
        print("L / R / F / B")
        print(white)

        userInput = input()

        if userInput == "L" :

            print("""It seems like invisible forces can't let you go upstairs...
            Is there another purpose you must fulfill? You wonder... """)
           

            userInput = " "

        elif userInput == "R" :

            print("""The wooden door is still shut by invisible forces...
            You are not getting out of this house so easily it seems""")
          

            userInput = " "
            
        elif userInput == "B" :

            print ("""I wouldn't go back in there if I were you...""")
           

            userInput = " "
        
        elif userInput == "F" :
           

            BrahmsRoom()
    

        else :

            print("Please enter one of the above options only")
            

            userInput = ""
    
    
def BrahmsRoom ():

    directions = ["L","R","F","B"]
    userInput = ""
    os.system('clear')

    scrollTxt("""You enter the room that was previously locked and to your surprise you find another ghostly figure\n
    You feel you body unable to move as you listen to the bearded small man talking to you in his deep voice\n""")
    time.sleep(2)
    print(purple)
    scrollTxt("""If there is anyone in this room that I have not insulted, I beg his pardon\n
    Without craftsmanship, inspiration is a mere reed shaken in the wind\n
    The idea comes to me from outside of me
    and is like a gift
    I then take the idea and make it my own
    that is where the skill lies...
    The only true immortality lies in one's children...
    And your children's music...has failed..!\n""")
    time.sleep(3)
   

    print(white)
    scrollTxt("""You listen to the short man's words stunned, and seem to remind you of something..\n
    Something from the text books maybe..
    Do you know these figures?
    No time for these thoughts..You are still scared..You need to get out..NOW!\n""")

    while userInput not in directions:

        print(green)
        print("L / R / F / B")
        print(white)

        userInput = input()

        if userInput == "L" :
            
            print("There's nothing but an empty wall..")
           

            userInput = ""
        
        elif userInput == "R" :

            print("There's only a library")
           

            userInput = ""
        
        elif userInput == "F" :

            print("I know he is a ghost..but don't try to run through him please..That's a no")
         

            userInput = ""

        elif userInput == "B" :

            print("You 'escape' into the main hall")
        
            
            MainHall3()
        
        else :
            print("Please enter one of the above options only")
           

            userInput = ""



def MainHall3 ():
    
    directions = ["L", "F", "B", "R"]
    userInput = ""
    os.system('clear')
    
    scrollTxt("""You once again venture into the main hall. Where to next?""")

    while userInput not in directions :

        print(green)
        print("L / R / F / B")
        print(white)

        userInput = input()

        if userInput == "R" :

            print("""This time it seems you can go upstairs with nothing stopping you..\n
            are you close to solving the mystery? """)
         

            SecondHall()

        elif userInput == "L" :

            print ("""The door is still shut by invisible forces...
            You are not getting out of this house so easily it seems""")
          

            userInput = " "
            
        elif userInput == "B" :

            print ("""I wouldn't go back in there if I were you...""")
            

            userInput = " "
        
        elif userInput == "F" :

            print ("""I wouldn't go back in there if I were you...""")
            
            
            userInput = ""

        else :

            print("Please enter one of the above options only")
            

            userInput = ""


def SecondHall():

    directions = ["L", "R", "F","B"]
    userInput = ""
    os.system('clear')

    scrollTxt("""You find yourself at the top of the stairs and into a second smaller hall.\n""")
    time.sleep(1)
    scrollTxt("""It seems to be quieter here, like all the abnormal distortion and wind stayed on the lower half of this house, but not quite..
    \n""")
    time.sleep (2)
    scrollTxt("""There is still one familiar sounding melody coming from the end of one of the hallways..\n
    Which path would you choose in this crossroad?""")
   

    while userInput not in directions:

        print(green)
        print("L / R / F / B")
        print(white)

        userInput = input()

        if userInput == "L" :

            print("You found a library room of some sorts...Maybe it has something of interest to solve this mystery")
            

            userInput = ""

        elif userInput == "R" :

            print("You followed the music to another room")    
           

            BeethovenRoom()
        
        elif userInput == "B" :

            print("Clearly the answer doesn't lie in going back down there..")
            

            userInput = ""

        elif userInput == "F" :

            print("You find another tall wooden door..There seems to be light coming from that room but you can't open it..yet")
            

            userInput = ""

        else :

            print("Please enter one of the above options only")  
            

            userInput = ""


def BeethovenRoom():
    
    directions = ["L", "R", "F","B"]
    userInput = ""
    os.system('clear')

    scrollTxt("""You walk into a room only to find another ghostly figure...\n""")
    time.sleep(1)
    print(red)
    print("DA DA DA DAAAAA\n")
    time.sleep(2)
    print(white)
    scrollTxt("""This one seems as angry in the after life as he was in his real life!\n
    The distinctive melody that comes from the air around him gave his identity away..\n
    There are many princes and noblemen. There is only one Beethoven!\n
    """)
    time.sleep(2)
    print(purple)
    scrollTxt("""Didn't hear you coming in! \n
    Applaud, my friend, the comedy is over...\n
    Music is like a dream.. One that I cannot hear..\n""")
    time.sleep(2)
    scrollTxt("""To play a wrong note is insignificant. To play without passion is inexcusable!\n
    And the music of this era is also inexcusable and without passion!\n""")
    time.sleep(2)
    scrollTxt("""Don't only practice your art, but force your way into its secrets,\n for it and knowledge can raise men to the divine!\n
    Since you cannot begin to understand it..you don't deserve to listen to the world around you..\n""")
    time.sleep(1)
    scrollTxt("Be cursed as I once were...\n""")
    time.sleep(5)
    print(red)
    print("DA DA DA DAAAAA\n")
    print(white)
    time.sleep(3)

    scrollTxt("""A shrieling sound makes you shudder and you realise you are slowly losing your hearing!
    Can it really be? Is this happening?\n""")
    time.sleep(2)
    scrollTxt("Hurry now!\n")
    scrollTxt("You must cast these ghosts away into the afterlife and break this curse cast uppon you..!\n")
    time.sleep(1)
    scrollTxt("...Where to next?")

    while userInput not in directions:

        print(green)
        print("L / R / F / B")
        print(white)

        userInput = input()

        if userInput == "L" :

            print("Are you already deaf?! Get out of here! You must hurry!")
            
            userInput = ""

        elif userInput == "R" :

            print("Are you already deaf?! Get out of here! You must hurry!")    
           

            userInput = ""
            
        elif userInput == "B" :

            print("Clearly the answer doesn't lie in going back down there..")
            

            SecondHall2()

        elif userInput == "F" :

            print("Are you already deaf?! Get out of here! You must hurry!")
            

            userInput = ""

        else :

            print("Please enter one of the above options only")  
            

            userInput = ""

    
def SecondHall2() :
    
    directions = ["L", "R", "F","B"]
    userInput = ""
    os.system('clear')

    scrollTxt("""You run into the hall again..Panicked, you need to find the solution to this whole paranormal mystery!\n""")
    time.sleep(1)
    scrollTxt("""Where to next?""")

    while userInput not in directions:

        print(green)
        print("L / R / F / B")
        print(white)

        userInput = input()

        if userInput == "L" :

            print("The answer clearly can't be found downstairs..! Hurry!")
           

            userInput = ""

        elif userInput == "B" :

            print("You can't possibly believe you have to get back there..! Hurry!") 
            

            userInput = ""

        elif userInput == "R" :

            print("This door is still locked! There's a strange aura about it...you might need to come back later! Hurry!") 
          

            userInput = "" 

        elif userInput == "F" :

            print("You enter another room") 
            

            LibraryRoom()   

        else :

            print("Please enter one of the above options only")  
           

            userInput = ""


def LibraryRoom() :
    
    directions = ["L", "R", "F","B"]
    userInput = ""
    os.system('clear')

    scrollTxt("""You find yourself in a room full of books, sheet music and records...\n
    The house is starting to tremble from the terrible noises the ghosts are making with their...'music'\n
    There must be a way out of this..\n""")
    time.sleep(1)
    scrollTxt("""There must be something you can do to make them go away before you stay deaf forever!\n""")
    
    time.sleep(3)
    scrollTxt("""You search around for anything that might help!..but your focus turns to a single vinyl record on the floor...\n""")
    scrollTxt("""It's called...\n""")
    time.sleep(1)
    print(yellow)
    scrollTxt(""" 'The Big 3 B'..\n""")
    time.sleep(2)
    print(white)
    scrollTxt("""You have no idea why.. but you feel like if you find somewhere to play this record maybe the ghosts will calm themselves
    and the curse will be lifted...\n
    But where??\n
    ...There is no time...! Hurry!""")

    while userInput not in directions:

        print(green)
        print("L / R / F / B")
        print(white)

        userInput = input()

        if userInput == "L" :

            print("You've already searched the room..Hurry!")
            

            userInput = ""

        elif userInput == "B" :

            print("There is only one place left...the last wooden door! Hurry!") 
            

            FinalRoom()

        elif userInput == "R" :

            print("You've already searched the room..Hurry!") 
            

            userInput = "" 

        elif userInput == "F" :

            print("You've already searched the room..Hurry!")
            

            userInput = ""    

        else :

            print("Please enter one of the above options only")  
            

            userInput = ""

           
    
    
def FinalRoom ():

    os.system('clear')

    scrollTxt("""You find the wooden doors at the last hallway open!..As if fate wanted you to be here...!\n""")
    time.sleep(1)
    print(yellow)
    scrollTxt("""In the middle of the room you find an old grammophone surrouned by a warm light!\n""")
    print(white)
    time.sleep(2)
    scrollTxt("""This is it! This must be it! you think!\n""")
    time.sleep(1)
    scrollTxt("""You put the record on and try to put the needle the right way through all this trembling..!\n
    You did it!\n""")
    time.sleep(1)
    scrollTxt("""The record starts spinning......and.......\n""")
    time.sleep(5)
    scrollTxt(name)
    time.sleep(2)
    print(green)
    scrollTxt(""" You can actually hear the music....!!\n
    It is a warm melodic music from old times...\n
    The music is the only thing breaking the sudden silence......\n""")
    print(white)
    time.sleep(3)
    scrollTxt("""You feel safe...\n
    You go into the rooms one by one...\n
    The ghosts are not present anymore..\n""")
    time.sleep(1)
    scrollTxt("You are free \n")
    time.sleep(3)
    scrollTxt("""You get close to the front door and you realise it's already open 
    so you get outside...\n
    it's morning already...\n""")
    time.sleep(3)
    scrollTxt("""Well......\n""")
    time.sleep(3)
    scrollTxt("..What a trip..\n")
    time.sleep(3)
    scrollTxt("Who were these other guys really......?\n")
    time.sleep(5)
    print(blue)
    scrollTxt("The End")

Garden()