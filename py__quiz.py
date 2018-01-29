import pyautogui as pg
import time
import webbrowser


points = 0

# Question
answer = pg.prompt(
"""
Which we would you rather do?

a)Fantasy Football
b)Fantasy Baseball

"""
    )
# Give points
if answer == "a":
    points += 1
elif answer == "b":
    points +=2
    

# Question
answer = pg.prompt(
"""
What do you prefer?

a)contact
b)non contact

"""
    )
# Give points
if answer == "a":
    points += 1
elif answer == "b":
    points +=2
    

# Question
answer = pg.prompt(
"""
Would you rather

a)Be indoors and outdoors
b)Be outdoors

"""
    )
# Give points
if answer == "a":
    points += 1
elif answer == "b":
    points +=2
    

# Question
answer = pg.prompt(
"""
Which do you consider the most important part of the body?

a)the legs
b)the shoulders

"""
    )
# Give points
if answer == "a":
    points += 1
elif answer == "b":
    points +=2
    


# End of Survey

pg.alert("You're...")

# Football
if points < 6:
    pg.alert("You are a nerd")

# Baseball
if points >= 6:
    pg.alert("You are a nerd")
    webbrowser.open("https://calculatedbravery.files.wordpress.com/2014/01/nerd.jpg")
    
