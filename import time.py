import time

import random


def print_pause(f):
    print(f)
    time.sleep(1)


def validate_input(s):
    try:
        n = int(s)
        return True, n
    except:
        return False, s


# function that take the imput from the user
# & make sure if the imput from the given choices
def variables(out):
    x = input("please, Enter a number form the choices")
    Flag, n = validate_input(x)
    while (Flag == False) or (n not in out):
        print("Wrong input")
        x = input("Please, try again & choice one of the numbers.")
        Flag, n = validate_input(x)
    the_right_imput = n
    return the_right_imput


def hale():
    print_pause("would you like to play again??" + " \n 1)yes \n 2)No")
    list = [1, 2]
    value1 = variables(list)
    return value1


# function that show on the user to play again
def repeat():
    mar = hale()
    while mar == 1:
        game()
        mar = hale()
    else:
        print("\t\t\t\t\tWe hope you enjoyed the game ")


# This the main functtion in the game that display all of remaining funnctions
def prompt():
    print(
        "\t\t\twelcome to the first edition game" + "'The savior and the last dragon'"
    )
    name = input("enter your name, please.")
    print(f"would you like to play our game,{name} ?? \n 1)yes \n 2)No")
    list = [1, 2]
    generate = variables(list)
    if generate == 1:
        game()
        repeat()
    else:
        print("Ok,Enjoy your free time")


# this function provide the main story that may be repeated more than one
def storyline(n):
    print_pause(
        "Since There is a legend that says that Sesunami slept in"
        + " one of the rivers in Tail Kingdom for 500 years"
    )
    print_pause("This legend is the guide for the area of the Sesunam")
    n += 2
    ("Now, your score =" + str(n))
    print_pause(
        "Since Sesunami is the lonely creature that has the ability"
        + " to gather powers of all parts of crystal together"
    )
    print_pause(
        "During your journey for seeking about the Sesunami,"
        + " An old man offers you to roll a dice,"
        + " and based on the number that appears randomly,"
        + " you will take a certain thing"
    )

    print_pause("will you accept this offer??\n 1)yes \n 2)No")
    choise1 = [1, 2]
    value1 = variables(choise1)
    if value1 == 1:
        print_pause("this decision wise!!")
        dice = {
            1: "Sword",
            2: "None",
            3: "Sword",
            4: "None",
            5: "Sword",
            6: "None",
        }
        list1 = [1, 2, 3, 4, 5, 6]
        random_num = random.choice(list1)
        object = dice[random_num]
        if object == "Sword":
            print_pause("You win Sword!!")
            n += 2
            print_pause("congrats!!Your score become ")
            print(n)
            components = [object]
        else:
            print_pause("You aren't win anything")

    else:
        print_pause(
            "you will continue in looking for" + " the river where Sesunam sleep "
        )
    print_pause("When you reach that place , you find it like heaven")
    print_pause(" you will perform some rituals to wake up Sesunam ")
    print_pause("Suddenly, Sesunam appear")
    print_pause("Her look is amazing, it is large and her hair is blue")
    print_pause("You will give Sesunam your own part from the crystal ")
    print_pause("when Sesunam touch the crystall , she will shine!!!")
    print_pause(
        "After that, you and her will try to"
        + " find the crystal part that existed in Tail"
    )
    print_pause("You will head to the temple" + " where the Tailed Queen is")
    print_pause("Keep in mind that the temple is" + " booby-trapped from the inside")
    print_pause("When you reach the temple, you will find 2 doors ")
    print_pause(
        "what will you choose?" + " \n 1) The first door \n 2) the second door "
    )
    choise2 = [1, 2]
    value2 = variables(choise2)
    if value2 == 1:
        print_pause("you will find a scary " + "monster, he is relatively large")
        print_pause("The door you choose is now closed. ")
        print_pause("So, you haven't any chance" + " He has no chance of coming back")
        print_pause("Now, you are forced to face the monster")
        if "Sword" in components:
            print_pause("you are lucky!!! since you have the sword")
            print_pause("Finally, you managed to kill the monster")
            print_pause("you get rid" + " of the monster")
            print_pause(
                "Finally, You find the another" + " part of crystal in the temple"
            )
            print_pause(
                "while the Sesunam touch another part" + ", she could her appearance"
            )
            print_pause(
                "This good step as Sesunam can hide her"
                + " appearance by Transform into human"
                + " form to no one know that "
            )

        else:
            print_pause(" while trying to kill the monster" + " , the monster kill you")
            print_pause("currently, you are dead")
            print_pause("your n =" + str(n))
            quit()
    else:
        print_pause(
            "This path leads you directly to" + " the crystal, without any traps "
        )
        print_pause("But, there is the Bump popping insects ")
        print_pause(
            "Be careful, you and Sesunam, because "
            + "the slightest sound wakes up popping bomb insects"
        )
        print_pause("Finally, You find the another" + " part of crystal in the temple")
        print_pause(
            "while the Sesunam touch another part," + " she could her appearance"
        )
        print_pause(
            "This good step as Sesunam can"
            + " hide her appearance by Transform"
            + " into human form in order to no one know that "
        )
        n += 2
        print_pause("Your score now equal" + str(n))
    print_pause("To which kingdom will you go now? \n 1)Talon \n 2)Fang ")
    choise3 = [1, 2]
    value3 = variables(choise3)
    if value3 == 2:
        print_pause("When you reach there, ")
        print_pause("you will find that Fang is surrounded by trench")
        print_pause(
            "This kingdom is famous for its big cats,"
            + " which are used by its soldiers"
        )
        print_pause("Sesunam help you in passing the trench")
        print_pause(
            "When you hear about the crystal, you find that"
            + " there is a large creature called (Emojy)"
            + " existed there to prevent anyone from taking it "
        )
        print_pause("while you walking , you finding something shine")
        print_pause("Would you like to take this something and open it?")
        print_pause("1) Yes \n 2)No")
        choise4 = [1, 2]
        value4 = variables(choise4)
        if value4 == 1:
            print_pause("right reponse !!")
            n += 2
            print_pause("Now, your score is " + str(n))
            print_pause("you open it")
            print_pause(
                "golden manuscript that has theses words 'to"
                + " kill Emojy, you must obtain "
                + "the crystal part in Talon first'"
            )
            print("Now, You and Sesunam are heading towards Talon")
            print_pause(
                "In the Talon, there is" + " the large and powerful part of crystal"
            )
            print_pause(
                "By gathering this part and the other parts"
                + " you have, You can kill the 'Emojy' monster"
            )
            print_pause(
                "This monster kill anyone try" + " to take the crystal in the Fang"
            )
            print_pause("Now, you are in a talon which " + "is surrounded by Droons")
            print_pause(
                "This kingdom was built on the water"
                + " to prevent the droons from attacking "
            )
            print_pause("While you and Sesunam are in place around Talon")
            print_pause(
                "Suddenly, some Predatory " + "creatures start to run behind you"
            )
            print_pause("You see cave on your right")
            print_pause("What will be you action?")
            print("1)you will enter this cave")
            print("2) you will continue running")
            op = [1, 2]
            value6 = variables(op)
            if value6 == 1:
                print_pause("This the right option!!!")
                n += 2
                print_pause("Your score now equal" + str(n))
                print_pause("while you enter the cave")
                print_pause("Suddenly, you see the crystal part")
                print_pause(
                    "When she touches this part,"
                    + " she can control weather, lightning, and thunder"
                )
            else:
                print_pause("These creatures continue running ")
                print_pause("Creatures managed to catch up with you and devour you")
                print_pause("Unfortunately, you are now dead")
                print_pause("Your score after whole game equal" + str(n))
                quit()
        else:
            print_pause("you must not still in Fang for long time")
            print_pause(
                "Since, In the Talon, there is "
                + "the large and powerful part of crystal"
            )
            print_pause(
                "By gathering this part and the other"
                + " parts you have, You can "
                + "kill the 'Emojy' monster"
            )
            print_pause(
                "This monster kill anyone try " + "to take the crystal in the Fang"
            )
            print_pause("Now, you are in a talon which is surrounded by Droons")
            print_pause(
                "This kingdom was built on the water"
                + " to prevent the droons from attacking "
            )
            print_pause("While you and Sesunam are in place around Talon")
            print_pause(
                "Suddenly, some Predatory " + "creatures start to run behind you"
            )
            print_pause("You see cave on your right")
            print_pause("What will be you action?")
            print("1)you will enter this cave")
            print("2) you will continue running")
            op = [1, 2]
            value6 = variables(op)
            if value6 == 1:
                print_pause("This the right option!!!")
                n += 2
                print_pause("Your score now equal" + str(n))
                print_pause("while you enter the cave")
                print_pause("Suddenly, you see the crystal part")
                print_pause(
                    "When she touches this part,"
                    + " she can control weather, lightning, and thunder"
                )
                print_pause(
                    "\t\t\t\t\t\t\t\t\t\t\t\t\t{Now, you are " + "heading towards Fang}"
                )
                print_pause(
                    "you went directly to the area"
                    + " where the crystal and Emojy exist"
                )
                print_pause("In the mission,Sesunam have a pivotal role")
                print_pause("Sesunam managed to kill Emojy")
                print_pause("Sesunam touch the last part")
                print_pause(
                    "Now, she has the ability to control in" + "weather tornadoes"
                )
                n += 2
                print_pause("\t\t\t\t\t\t\t\t{The main mission is advieved} ")
                if n > 8:
                    print_pause("Finally, you win the game ")

                else:
                    print_pause("Unfortunately, you lose the game")
                print_pause("you score equal" + str(n))
                print_pause("\t\t\t\t\t\t\t\t\t\t\t {Game is over}")
            else:
                print_pause("These creatures continue running ")
                print_pause(
                    "Creatures managed to " + "catch up with you and devour you"
                )
                print_pause("Unfortunately, you are now dead")
                print_pause("Your score after whole game equal" + str(n))
                quit()
    else:
        print_pause("This is the right option")
        n += 2
        print_pause(
            "Since, In the Talon, there is the" + " large and powerful part of crystal"
        )
        print_pause(
            "By gathering this part and the other"
            + " parts you have, You can kill the 'Emojy' monster"
        )
        print_pause("This monster kill anyone " + "try to take the crystal in the Fang")
        print_pause("Now, you are in a talon which is surrounded by Droons")
        print_pause(
            "This kingdom was built on the water"
            + " to prevent the droons from attacking "
        )
        print_pause("While you and Sesunam are in place around Talon")
        print_pause("Suddenly, some Predatory " + "creatures start to run behind you")
        print_pause("You see cave on your right")
        print_pause("What will be you action?")
        print("1)you will enter this cave")
        print("2) you will continue running")
        op = [1, 2]
        value6 = variables(op)
        if value6 == 1:
            print_pause("This the right option!!!")
            n += 2
            print_pause("Your score now equal" + str(n))
            print_pause("while you enter the cave")
            print_pause("Suddenly, you see the crystal part")
            print_pause(
                "When she touches this part,"
                + " she can control weather, lightning, and thunder"
            )
            print_pause("\t\t\t\t\t\t\t\t\t\t\t\t\t{Now, you are heading towards Fang}")
            print_pause(
                "you went directly to the area where the crystal and Emojy exist"
            )
            print_pause("In the mission,Sesunam have a pivotal role")
            print_pause("Sesunam managed to kill Emojy")
            print_pause("Sesunam touch the last part")
            print_pause("Now, she has the ability to control in" + "weather tornadoes")
            n += 2
            print_pause("\t\t\t\t\t\t\t\t{The main mission is advieved} ")
            if n > 8:
                print_pause("Finally, you win the game ")

            else:
                print_pause("Unfortunately, you lose the game")
            print_pause("you score equal" + str(n))
            print_pause("\t\t\t\t\t\t\t\t\t\t\t {Game is over}")
        else:
            print_pause("These creatures continue running ")
            print_pause("Creatures managed to " + "catch up with you and devour you")
            print_pause("Unfortunately, you are now dead")
            print_pause("Your score after whole game equal" + str(n))
            quit()


# this function provide all of the options that player may choose
def game():
    place = ["Tail", "Heart", "Talon", "Fang"]
    print_pause(
        "500 years ago, It tells that" + "there was alarge Kingdom called COMANDRA"
    )
    print_pause(
        "It was the greatest Kingdom on Earth,"
        + "where magical creatures called dragons lived"
    )
    print_pause("In this time, There was " + "destructive creatures called  'Droons' ")
    print_pause(
        "Droons created because of" + " dispute and Distrust between the humans"
    )
    print_pause(
        "At this time, The drone started turning "
        + "humans and dragons into stone, leaving five of the dragons"
    )
    print_pause(
        "The Sesunami, from the five dragons,"
        + " made a magical crystal in "
        + "which to gather their five powers"
    )
    print_pause("this blue crystal hid the" + " droons from Earth")
    print_pause(
        "After hundred years, Comandra is divided"
        + " into five kingdoms and the crystal existed in Heart kingdom"
    )
    print_pause(
        "Your father was the ruler of the Heart"
        + " Realm and made you one of the Crystal saviors"
    )
    print_pause(
        "So, the four kingdoms fought to obtain"
        + " the crystal until this crystal broke."
        + " In the time, The droons started to appear"
        + " again and every kingdom took part of crystal"
    )
    print_pause(
        "Drones are creatures that do not exist in"
        + " the place where water and crystal exist "
    )
    print_pause(" your father turned into rock ")
    print_pause(
        "Now, your mission is to gather the parts of "
        + "crystal and unite the kingdoms to return Comandra"
    )

    print_pause(
        "Which kingdoms will you start with?" + "\n 1)Tail \n 2)Talon \n 3)Fang "
    )
    choice = [1, 2, 3]
    value = variables(choice)
    total_score = 0
    if value == 1:
        print_pause("Your choice is right!!!")
        total_score += 2
        print_pause("Now, your score =" + str(total_score))
        storyline(total_score)

    elif value == 2:
        print_pause("Now, You are heading towards Talon")
        print_pause("Talon is kingdom, which built on water")
        print_pause(
            "you hear from kingdom people"
            + "that if the crystal is touched by human "
            + ", it will broken & The droons nest all over the world "
        )
        print_pause(
            "Therefore, you should discover the" + " place of the {last dragon}"
        )
        print_pause(
            "Now, you are heading towards Tial" + "where the last dragon exists"
        )
        print_pause("To go Tail kingdom , There are two ways ")
        print_pause("Which path will you take?")
        print_pause("1) sea route through Pacific ocean")
        print("2) Overland route through the Chang desert")
        list2 = [1, 2]
        value7 = variables(list2)
        if value7 == 1:
            print_pause("you board the ship")
            print_pause(
                "During the trip, you face" + "big scary craeture called 'Ting'"
            )
            print_pause("while facing this creature")
            print_pause("Unfortunately, you died")
            print_pause("you lose the game")
            print_pause("your score equal" + str(total_score))
            print_pause("\t\t\t\t\t\t\t\t\t\t The game is over")
            quit()
        else:
            print_pause("This is the right choise!!")
            print_pause("your score equal" + str(total_score))
            print_pause("Your trip went without risks")
            print_pause("you reach Tail kingdom")
            storyline(total_score)
    else:
        print_pause("Now, You are heading towards to Fang")
        print_pause(
            "you hear from kingdom people"
            + "that if the crystal is touched by human "
            + ", it will broken & The droons nest all over the world "
        )
        print_pause(
            "Therefore, you should discover the" + " place of the {last dragon}"
        )
        print_pause(
            "Now, you are heading towards to Tail" + " where the last dragon exists"
        )
        print_pause("To go Tail kingdom , There are two ways ")
        print_pause("Which path will you take?")
        print_pause("1) sea route through Dong sea")
        print("2) Overland route through the Wookie desert")
        list2 = [1, 2]
        value7 = variables(list2)
        if value7 == 1:
            print_pause("you board the ship")
            print_pause(
                "During the trip, you face" + "big scary craeture called 'Ting'"
            )
            print_pause("while facing this creature")
            print_pause("Unfortunately, you died")
            print_pause("you lose the game")
            print_pause("your score equal" + str(total_score))
            print_pause("\t\t\t\t\t\t\t\t\t\t The game is over")
            quit()
        else:
            print_pause("This is the right choise!!")
            print_pause("your score equal" + str(total_score))
            print_pause("Your trip went without risks")
            print_pause("you reach Tail kingdom")
            storyline(total_score)

prompt()