import random
import json
import os
import time

from pip import main

class format:
    clear = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
    underline = "\u001b[4m"
    italic = "\u001b[3m"
    dim = "\u001b[2m"
    bold = "\u001b[1m"
    end = "\u001b[0m"
    red = "\u001b[31m"
    blue = "\u001b[36m"
    green = "\u001b[32m"

directory = os.path.dirname(__file__)
filename = os.path.join(directory, ('json/dialogue.json'))
dialogue = json.load(open(filename, "r"))
filename = os.path.join(directory, ('json/maps.json'))
maps = json.load(open(filename, "r"))
filename = os.path.join(directory, ('json/items.json'))
items = json.load(open(filename, "r"))
filename = os.path.join(directory, ('json/lootpools.json'))
lootpool = json.load(open(filename, "r"))
filename = os.path.join(directory, ('json/democontent.json'))
demo = json.load(open(filename, "r"))



def defineVariables():
    global x
    global y
    global day
    global hours
    global minutes
    global period
    global headHealth
    global torsoHealth
    global leftArmHealth
    global rightArmHealth
    global leftLegHealth
    global rightLegHealth
    global sanity
    global inventory
    global inventoryIDs
    global inventoryDurability
    global equipped
    global equippedDurability
    global shadows
    global shadowhealth
    global side
    global looted
    global building
    global huntstart
    global level

    x = 1
    y = 1
    day = 0
    hours = 7
    minutes = random.randint(0, 4) * 10
    period = "PM"
    headHealth = 50
    torsoHealth = 100
    leftArmHealth = 75
    rightArmHealth = 75
    leftLegHealth = 75
    rightLegHealth = 75
    sanity = 100
    inventory = []
    inventoryIDs = []
    inventoryDurability = []
    equipped = "None"
    equippedDurability = 0
    shadows = []
    shadowhealth = []
    side = 1
    looted = []
    building = "house"
    huntstart = 0
    level = 1

def testVariables():
    global x
    global y
    global day
    global hours
    global minutes
    global period
    global inventory
    global inventoryIDs
    global inventoryDurability
    global equipped
    global equippedDurability
    global shadows
    global shadowhealth
    global difficulty

    x = 1
    y = 1
    day = 0
    hours = 1
    minutes = random.randint(0, 59)
    period = "AM"
    inventory = ["TEST_BAT", "TEST_SHOTGUN", "TEST_REVOLVER", "ROCKET_LAUNCHER"]
    inventoryIDs = ["baseballbat", "shotgun", "revolver", "rocketlauncher"]
    inventoryDurability = [3, 5, 6, 1]
    equipped = "None"
    equippedDurability = 0
    shadows = ["diningroom"]
    shadowhealth = [100]
    difficulty = 1

def updateTime(addminutes = 0):
    global minutes
    global minutesstr
    global hours
    global day
    global period

    minutes = minutes + addminutes

    while minutes >= 60:
        hours = hours + 1
        minutes = minutes - 60
    while hours > 12:
        if period == "AM":
            period = "PM"
        else:
            period == "AM"
        hours = hours - 12
    minutesstr = str(minutes)
    if minutes < 10:
        minutesstr = "0" + minutesstr

def ask(message, indent, options, delay):
    y = 0
    while y <= indent:
        print(" ", end = "")
        y = y + 1
    print(message)
    x = 0
    while x < len(options):
        y = 0
        while y <= indent:
            print(" ", end = "")
            y = y + 1
        print(str(x + 1) + ". " + options[x])
        time.sleep(delay)
        x = x + 1
    y = 0
    while y <= indent:
        print(" ", end = "")
        y = y + 1
    x = int(input("> "))
    if x > len(options) or x < 1:
        while x > len(options) or x < 1:
            y = 0
            while y <= indent:
                print(" ", end = "")
                y = y + 1
            x = int(input("Invalid input!\n   > "))
    return x

def askString(message, indent):
    y = 0
    while y <= indent:
        print(" ", end = "")
        y = y + 1
    print(message)
    while y <= indent:
        print(" ", end = "")
        y = y + 1
    x = input("> ")
    return x

def genShadows():
    global shadows
    global huntstart
    global huntbegin
    if (hours >= 8 and minutes >= 30 and period == "PM") or (hours <= 6 and period == "AM"):
        if huntstart == 0:
            huntstart = 1
            huntbegin = format.red + format.bold + "  " + fetchDialogue("menu", "huntstart") + format.end
        if len(shadows) < difficulty * 2:
            rand = random.randint(1, 5)
            if rand == 1:
                roomlist = maps[building]["roomlist"]
                rand = random.randint(0, len(roomlist) - 1)
                shadows.append(roomlist[rand])
                shadowhealth.append(100 * difficulty)
        rand = random.randint(0, 3)
        if rand == 1:
            run = 0
            layout = maps[building]["layout"]
            while run < len(shadows):
                vertical = 0
                while vertical <= len(layout) and shadows[run] not in layout[vertical]:
                    if shadows[run] in layout[vertical]:
                        horizontal = layout[vertical].index(shadows[run])
                        shadowdirections = []
                        if layout[vertical - 1][horizontal] == "open":
                            shadowdirections.append("up")
                        if layout[vertical + 1][horizontal] == "open":
                            shadowdirections.append("down")
                        if layout[vertical][horizontal - 1] == "open":
                            shadowdirections.append("left")
                        if layout[vertical][horizontal + 1] == "open":
                            shadowdirections.append("right")
                        if len(shadowdirections) > 0:
                            dir = random.randint(0, (len(shadowdirections) - 1))
                            print("dir: " + str(dir))
                            print(shadowdirections)
                            print(str(run) + "/" + str(len(shadows)))
                            time.sleep(1)
                            if shadowdirections[dir] == "up":
                                vertical = vertical - 2
                                shadows[run] = layout[vertical][horizontal]
                            if shadowdirections[dir] == "down":
                                vertical = vertical + 2
                                shadows[run] = layout[vertical][horizontal]
                            if shadowdirections[dir] == "left":
                                horizontal = horizontal - 2
                                shadows[run] = layout[vertical][horizontal]
                            if shadowdirections[dir] == "right":
                                horizontal = horizontal + 2
                                shadows[run] = layout[vertical][horizontal]
                    else:
                        vertical = vertical + 1
                run = run + 1

def checkHealth():
    global headHealth
    global torsoHealth
    global leftArmHealth
    global rightArmHealth
    global leftLegHealth
    global rightLegHealth
    global sanity

    actions = ""
    if headHealth <= 0:
        death("head")
    if torsoHealth <= 0:
        death("torso")
    if leftArmHealth <= 0:
        actions = actions + "\n  " + format.red + format.bold + "You wince in pain. Your left arm is crippled." + format.end
    if rightArmHealth <= 0:
        actions = actions + "\n  " + format.red + format.bold + "You wince in pain. Your right arm is crippled." + format.end
    if leftLegHealth <= 0:
        actions = actions + "\n  " + format.red + format.bold + "You wince in pain. Your left leg is crippled." + format.end
    if rightLegHealth <= 0:
        actions = actions + "\n  " + format.red + format.bold + "You wince in pain. Your right leg is crippled." + format.end
    if headHealth + 1 <= 50:
        headHealth = headHealth + 1
    if torsoHealth + 1 <= 100:
        torsoHealth = torsoHealth + 1
    if leftArmHealth + 1 <= 75:
        leftArmHealth = leftArmHealth + 1
    if rightArmHealth + 1 <= 75:
        rightArmHealth = rightArmHealth + 1
    if leftLegHealth + 1 <= 75:
        leftLegHealth = leftLegHealth + 1
    if rightLegHealth + 1 <= 75:
        rightLegHealth = rightLegHealth + 1
    if sanity + 1 <= 100:
        sanity = sanity + 1
    return actions

def fetchDialogue(speaker, prompt):
    return dialogue[speaker][prompt][str(random.randint(1, dialogue[speaker][prompt]["number"]))]

def cutsceneDialogue(message, indent, delay):
    y = 0
    while y < indent:
        print(" ", end = "")
        y = y + 1
    y = 0
    print("\"", end = "")
    while y < len(message):
        print(message[y : y + 1], end = "")
        if y < len(message) - 1:
            time.sleep(delay)
        y = y + 1
    print("\"")

def cutsceneOther(message, indent, delay):
    y = 0
    while y < indent:
        print(" ", end = "")
        y = y + 1
    y = 0
    while y < len(message):
        print(message[y : y + 1], end = "")
        time.sleep(delay)
        y = y + 1
    print("")

def death(target):
    print(format.clear)
    cutsceneOther(format.red + format.bold + "The shadow hits you in the " + target + "." + format.end, 2, 0.05)
    time.sleep(1)
    cutsceneDialogue(fetchDialogue("player", "attacked"), 2, 0.05)
    time.sleep(3)
    cutsceneOther(format.red + format.bold + "You die." + format.end, 2, 0.05)
    time.sleep(3)
    input("\n  Press " + format.bold + "enter" + format.end + " to continue.  ")
    print(format.clear)
    time.sleep(1)
    playerDecision = ask("Return to the menu, or watch the ending cutscenes?", 2, ["Watch cutscenes", "Return to menu"], 0.25)
    if playerDecision == 2:
        mainMenu()
    else:
        print(format.clear)
        time.sleep(3)
        cutsceneOther("March " + str(6 + day) + ", 2013", 2, 0.05)
        cutsceneOther("Bell ridge police department", 2, 0.05)
        cutsceneOther("-------------------------------", 2, 0.01)
        time.sleep(2)
        cutsceneOther("Police recovered a body from the Marshall residence at approximately", 2, 0.05)
        cutsceneOther("9:14 am. Victim had taken numerous blunt attacks throughout the", 2, 0.05)
        cutsceneOther("body, but postmortem examination has revealed that the immediate", 2, 0.05)
        cutsceneOther("cause of death was due to extensive damage to the " + target + " area.", 2, 0.05)
        cutsceneOther("-------------------------------", 2, 0.01)
        time.sleep(2)
        cutsceneOther("Current theories in the case include possible home invasion", 2, 0.05)
        cutsceneOther("with the intent of homicide.", 2, 0.05)
        time.sleep(3)
        input("\n  Press " + format.bold + "enter" + format.end + " to continue.  ")
        print(format.clear)
        time.sleep(2)
        cutsceneDialogue("It wasn't your fault, Lindsay.", 2, 0.05)
        time.sleep(3)
        print(format.clear)
        apartment = """
  ──────═══─────┐
         i      │
             ─┐ │
   ┌─┐    ║  u│ │
   │ │    ║  ▓│ │
   └─┘       ─┘ │"""
        print(apartment)
        print("\n  " + format.bold + "Vanessa" + format.end + ", friend\n  Apartment, 8:54am")
        print("")
        time.sleep(0.5)
        cutsceneDialogue("It really wasn't.", 2, 0.05)
        time.sleep(0.5)
        cutsceneDialogue("I don't know why you're blaming yourself for this.", 2, 0.05)
        input("\n  Press " + format.bold + "enter" + format.end + " to continue.  ")
        print(format.clear)
        print(apartment)
        print("\n  " + format.bold + "Lindsay" + format.end + ", caretaker\n  Apartment, 8:55am")
        print("")
        cutsceneDialogue("Oh god, I was the last one to see him though!", 2, 0.05)
        time.sleep(0.5)
        cutsceneDialogue("What if he knew something was wrong?", 2, 0.05)
        input("\n  Press " + format.bold + "enter" + format.end + " to continue.  ")
        print(format.clear)
        print(apartment)
        print("\n  " + format.bold + "Vanessa" + format.end + ", friend\n  Apartment, 8:55am")
        print("")
        cutsceneDialogue("My god. Stop blaming yourself.", 2, 0.05)
        time.sleep(0.5)
        cutsceneDialogue("If he knew something was wrong, he'd have gone and said it.", 2, 0.05)
        input("\n  Press " + format.bold + "enter" + format.end + " to continue.  ")
        print(format.clear)
        print(apartment)
        print("\n  " + format.bold + "Vanessa" + format.end + ", friend\n  Apartment, 8:55am")
        print("")
        cutsceneDialogue("We both knew him, you know.", 2, 0.05)
        input("\n  Press " + format.bold + "enter" + format.end + " to continue.  ")
        print(format.clear)
        print(apartment)
        print("\n  " + format.bold + "Vanessa" + format.end + ", friend\n  Apartment, 8:56am")
        print("")
        cutsceneDialogue("Look, even if he knew, it still wouldn't be your fault.", 2, 0.05)
        time.sleep(1)
        cutsceneDialogue("It'd still be the fault of the bastard that killed him.", 2, 0.05)
        input("\n  Press " + format.bold + "enter" + format.end + " to continue.  ")
        print(format.clear)
        print(apartment)
        print("\n  " + format.bold + "Lindsay" + format.end + ", caretaker\n  Apartment, 8:57am")
        print("")
        cutsceneDialogue("God...", 2, 0.05)
        input("\n  Press " + format.bold + "enter" + format.end + " to continue.  ")
        print(format.clear)
        print(apartment)
        print("\n  " + format.bold + "Vanessa" + format.end + ", friend\n  Apartment, 8:57am")
        print("")
        cutsceneDialogue("We gotta get to the meeting with the police on this though.", 2, 0.05)
        time.sleep(0.5)
        cutsceneDialogue("C'mon. We'll get through this. We'll find the bastard.", 2, 0.05)
        time.sleep(3)
        print(format.clear)
        time.sleep(3)
        cutsceneDialogue("We'll find em.", 2, 0.05)
        time.sleep(4)
        print(format.clear)
        time.sleep(0.5)
        input("\n  Press " + format.bold + "enter" + format.end + " to return to the menu.  ")
        mainMenu()
    
def mainMenu():
    print(format.clear)
    print(format.bold + format.red)
    print("          __      ______  ______  ______")
    print("         / /     / __  / / ____/ /_  __/")
    print("        / /     / /_/ / / /___    / /")
    print("       / /     / __  / /___  /   / /")
    print("      / /___  / / / / ____/ /   / /")
    print("     /_____/ /_/ /_/ /_____/   /_/")
    print("")
    print("         ___     __  ______  _____   __  __  ______")
    print("        /   |   / / /_  __/ / ___/  / / / / /_  __/")
    print("       / /| |  / /   / /   / /     / /_/ /   / /")
    print("      / / | | / /   / /   / / __  / __  /   / /")
    print("     / /  | |/ / __/ /_  / /_/ / / / / /   / /")
    print("    /_/   |___/ /_____/ /_____/ /_/ /_/   /_/")
    print("")
    print("        ______  ___     __")
    print("       / __  / /   |   / /")
    print("      / / / / / /| |  / /")
    print("     / / / / / / | | / /")
    print("    / /_/ / / /  | |/ /")
    print("   /_____/ /_/   |___/")
    print("")
    print("       ______  ______  ______  ______  __  __")
    print("      / ____/ / __  / / __  / /_  __/ / / / /")
    print("     / /___  / /_/ / / /_/ /   / /   / /_/ /")
    print("    / ____/ / __  / / __  /   / /   / __  /")
    print("   / /___  / / / / / / | |   / /   / / / /")
    print("  /_____/ /_/ /_/ /_/  |_|  /_/   /_/ /_/")
    print(format.end)
    playerDecision = ask("v0.0.1 PRE-RELEASE \n" + "   " + format.italic + format.dim + fetchDialogue("menu", "splashtext") + format.end + "\n", 2, ["Start new game", "Load Game (Nothing actually saves, sorry)", "Tutorial (Currently not functioning)", "Demo content (Not much here)", "Exit"], 0.25)
    if playerDecision == 1:
        startGame()
    if playerDecision == 2:
        loadGame()
    if playerDecision == 3:
        tutorial()
    if playerDecision == 4:
        demoContent()
    if playerDecision == 5:
        exit()

def startGame():
    global difficulty
    time.sleep(1)
    print(format.clear)
    time.sleep(2)
    cutsceneDialogue("So your appointment with the doctor is next week.", 2, 0.03)
    input("\n  Press " + format.bold + "enter" + format.end + " to continue.  ")
    print(format.clear)
    cutsceneDialogue("I actually need to go, it's getting late.", 2, 0.03)
    input("\n  Press " + format.bold + "enter" + format.end + " to continue.  ")
    print(format.clear)
    print("  ")
    print("       #   #     ")
    print("       #   #     ")
    print("       #   #     ")
    print("       # u #     ")
    print("  ──────   ─────┬")
    print("         o      │")
    print("  ")
    print("\n  " + format.bold + "Lindsay" + format.end + ", caretaker\n  Living room, 7:02pm\n  ")
    time.sleep(2)
    cutsceneDialogue("So uh, I'll see you soon.", 2, 0.03)
    time.sleep(1)
    print("")
    cutsceneOther(format.italic + format.dim + "For some reason this conversation starts to feel really important.\n" + format.end, 2, 0.03)
    time.sleep(1)
    playerDecision = ask("", 1, [
        "\"Have a good night.\"\n     [ Easy difficulty. ]\n     - Mild psychosis.\n     - Lindsay will return often, and her opinion will be improved. \n", 
        "\"Alright.\"\n     [ Normal difficulty. ]\n     - Average psychosis.\n     - Lindsay will return sometimes, and her opinion will be average. \n", 
        "\"...\"\n     [ Hard difficulty. ]\n     - Severe psychosis.\n     - Lindsay will only call, and her opinion will be worsened. \n"], 1)
    if playerDecision == 1:
        difficulty = 0.5
        said = "Have a good night."
        nextLine = "You too."
    if playerDecision == 2:
        difficulty = 1
        said = "Alright."
        nextLine = "Have a good night."
    if playerDecision == 3:
        difficulty = 2
        said = "..."
        nextLine = "Okay, jeez, fine. Don't talk. I'll be seein' ya."
    print(format.clear)
    print("  ", end = "")
    cutsceneDialogue(said, 0, 0.03)
    time.sleep(2)
    print("  ")
    print("       #   #     ")
    print("       # u #     ")
    print("       #   #     ")
    print("       #   #     ")
    print("  ──────   ─────┬")
    print("         o      │")
    print("  ")
    print("\n  " + format.bold + "Lindsay" + format.end + ", caretaker\n  Living room, 7:03pm\n  ")
    cutsceneDialogue(nextLine, 2, 0.03)
    input("\n  Press " + format.bold + "enter" + format.end + " to continue.  ")
    print(format.clear)
    print("       #   #     ")
    print("       #   #     ")
    print("       #   #     ")
    print("       #   #     ")
    print("  ──────   ─────┬")
    print("         o      │")
    print("  ")
    print("\n  Living room, 7:03pm")
    time.sleep(2)
    print(format.clear)
    print("       #   #     ")
    print("       #   #     ")
    print("       #   #     ")
    print("       #   #     ")
    print("  ──────═══─────┬")
    print("         o      │")
    print("  ")
    print("\n  Living room, 7:03pm")
    time.sleep(2.71828)
    print(format.clear)
    print("       #   #     ")
    print("       #   #     ")
    print("       #   #     ")
    print("  ──────═══─────┬")
    print("      *      *  │")
    print("     ─┐  o      │")
    print("  ")
    print("\n  Living room, 7:03pm")
    time.sleep(0.75)
    print(format.clear)
    print("       #   #     ")
    print("       #   #     ")
    print("  ──────═══─────┬")
    print("      * **   *  │")
    print("     ─┐         │")
    print("  ║  ▓│  o      │")
    print("  ")
    print("\n  Living room, 7:03pm")
    time.sleep(0.75)
    print(format.clear)
    print("       #   #     ")
    print("  ──────═══─────┬")
    print("      * *** **  │")
    print("     ─┐  * *    │")
    print("  ║  ▓│    *    │")
    print("  ║  ▓│  o      │")
    print("  ")
    print("\n  Living room, 7:03pm")
    time.sleep(0.75)
    print(format.clear)
    print("  ──────═══─────┬")
    print("      ********  │")
    print("     ─┐ *****   │")
    print("  ║  ▓│  **     │")
    print("  ║  ▓│         │")
    print("     ─┘  o      │")
    print("  ")
    print("\n  Living room, 7:03pm")
    time.sleep(3)
    print(format.clear)
    time.sleep(1)
    print("  ┌─────┐ ┌─┐ ┌─┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐     ┌─┐")
    print("  │ ┌───┘ │ │ │ │ │ ┌─┐ │ │ ┌─┐ │ └─┐ ┌─┘ │ ┌───┘ │ ┌─┐ │     │ │")
    print("  │ │     │ └─┘ │ │ └─┘ │ │ └─┘ │   │ │   │ └───┐ │ └─┘ │     │ │")
    print("  │ │     │ ┌─┐ │ │ ┌─┐ │ │ ┌───┘   │ │   │ ┌───┘ │ ┌┐ ┌┘     │ │")
    print("  │ └───┐ │ │ │ │ │ │ │ │ │ │       │ │   │ └───┐ │ ││ │      │ │")
    print("  └─────┘ └─┘ └─┘ └─┘ └─┘ └─┘       └─┘   └─────┘ └─┘└─┘      └─┘")
    time.sleep(1)
    cutsceneOther("WHISPERS", 2, 0.03)
    time.sleep(1)
    input("\n  Press " + format.bold + "enter" + format.end + " to continue.  ")
    print(format.clear)
    cutsceneOther("A game by " + format.dim + format.bold + "Those Who Wander studios" + format.end, 2, 0.05)
    time.sleep(0.5)
    print("")
    cutsceneOther("With design and story help from members of " + format.dim + format.bold + "SEXOOOOOO" + format.end + ", " + format.dim + format.bold + "KRINK" + format.end + ", and " + format.dim + format.bold + "Union" + format.end, 2, 0.05)
    time.sleep(0.5)
    print("")
    cutsceneOther(format.bold + "Thanks to all of those who have motivated me to work on this project." + format.end, 2, 0.05)
    print("")
    input("\n  Press " + format.bold + "enter" + format.end + " to continue.  ")
    print(format.clear)
    time.sleep(1)
    defineVariables()
    startNew()

def loadGame():
    global difficulty
    #Placeholder, planned to be implemented
    print(format.clear)
    print("   This is planned to be implemented. Progress is not saved,")
    print("   but I can jump you right to gameplay if you want.")
    playerDecision = ask("", 3, ["Yes", "No"], 0.05)
    if playerDecision == 1:
        defineVariables()
        playerDecision = ask("\nDifficulty selection:\n", 1, [
            "Wait for an eternity to have a shadow spawn simulator\n     [ Easy difficulty. ]\n     - Mild psychosis.\n     - Lindsay will return often, and her opinion will be improved. \n", 
            "Average night in florida simulator\n     [ Normal difficulty. ]\n     - Average psychosis.\n     - Lindsay will return sometimes, and her opinion will be average. \n", 
            "SCHIZOOOOOO\n     [ Hard difficulty. ]\n     - Severe psychosis.\n     - Lindsay will only call, and her opinion will be worsened. \n"], 0.25)
        if playerDecision == 1:
            difficulty = 0.5
        if playerDecision == 2:
            difficulty = 1
        if playerDecision == 3:
            difficulty = 2
        print(format.clear)
        startNew()
    if playerDecision == 2:
        mainMenu()

def startNew():
    global room
    global side
    room = "livingroom"
    side = 1
    updateTime()
    printMap(fetchDialogue("player", "wayblocked"))

def printMap(dialogue="", action=""):
    global huntstart
    genShadows()
    print(format.clear)
    shadowin = ""
    if room in shadows:
        shadowin = "s"
    if checkHealth() != "":
        action = action + checkHealth()
    print(maps[building][room]["side" + str(side)]["1" + shadowin])
    print(maps[building][room]["side" + str(side)]["2" + shadowin])
    print(maps[building][room]["side" + str(side)]["3" + shadowin])
    print(maps[building][room]["side" + str(side)]["4" + shadowin])
    print(maps[building][room]["side" + str(side)]["5" + shadowin])
    print(maps[building][room]["side" + str(side)]["6" + shadowin])
    print("\n  " + maps[building][room]["name"] + ", " + str(hours) + ":" + minutesstr + " " + period)
    if huntstart == 1:
        print(huntbegin)
        huntstart = 2
    if action != "":
        print("  " + format.italic + action + format.end)
    if dialogue != "":
        print("  \"" + dialogue + "\"")
    actions = ["Move", "Do", "Inventory", "Leave room"]
    if room in shadows:
        actions.append("Combat")
    playerDecision = ask("", 2, actions, 0)
    print("")
    if playerDecision == 1:
        move()
    if playerDecision == 2:
        do()
    if playerDecision == 3:
        inv()
    if playerDecision == 4:
        moveRoom()
    if actions[playerDecision - 1] == "Combat":
        combat()

def move():
    global side
    global sanity
    if side == 2:
        side = 1
    else:
        side = 2
    x = random.randint(1, 6)
    if x == 1:
        updateTime(10)
    said = ""
    action = ""
    if shadows != []:
        rand = random.randint(1, int(5 / difficulty))
        if rand == 1:
            heard = fetchDialogue("shadow", "sound")
            rand = random.randint(0, len(shadows) - 1)
            location = maps[building][shadows[rand]]["name"]
            said = fetchDialogue("player", "heard")
            action = "You hear " + heard + " coming from the " + location + "."
            sanity = sanity - random.randint(0, 5)
    printMap(said, action)

def do():
    playerDecision = ask("Action menu:", 2, ["Loot area", "Check self", "Exit menu"], 0.1)
    if playerDecision == 1:
        loot()
    if playerDecision == 2:
        checkSelf()
    if playerDecision == 3:
        printMap(fetchDialogue("player", "nevermind"))

def loot():
    global inventoryIDs
    interactable = maps[building][room]["side" + str(side)]["interactable"]
    if interactable != [] and len(inventory) <= 10:
        print(format.clear)
        playerDecision = ask("Loot menu:", 2, interactable, 0.1)
        if interactable[playerDecision - 1] + room in looted:
            printMap("", "You already looted this object!")
        else:
            pool = lootpool[interactable[playerDecision - 1]]["loot"]
            loot = pool[random.randint(0, len(pool) - 1)]
            inventoryIDs.append(loot)
            inventory.append(items[loot]["name"])
            inventoryDurability.append(items[loot]["durability"])
            if lootpool[interactable[playerDecision - 1]]["reloot"] == "no":
                looted.append(interactable[playerDecision - 1] + room)
            updateTime(random.randint(2, 5) * 10)
            printMap("", "You looted a " + items[loot]["name"] + " from the " + interactable[playerDecision - 1] + ".")
    else:
        if maps[building][room]["side" + str(side)]["interactable"] == []:
            printMap("", "No places to loot!")
        else:
            printMap("", "No space for loot!")

def checkSelf():
    print(format.clear)
    cutsceneOther("Self check:", 2, 0.05)
    print("")
    print("       Head: " + format.red + str(headHealth) + format.end + "/50")
    print("   Left arm: " + str(leftArmHealth) + "/75")
    print("  Right arm: " + str(rightArmHealth) + "/75")
    print("      Torso: " + format.red + str(torsoHealth) + format.end + "/100")
    print("   Left leg: " + str(leftLegHealth) + "/75")
    print("  Right leg: " + str(rightLegHealth) + "/75")
    print("     Sanity: " + str(sanity) + "/100")
    print("")
    print("  Items printed in " + format.red + "red" + format.end + " are vital parts.")
    input("\n  Press " + format.bold + "enter" + format.end + " to continue.  ")
    printMap()

def inv():
    global inventory
    global inventoryIDs
    global inventoryDurability
    global equipped
    global equippedDurability
    global sanity

    print(format.clear)
    if equipped != "None":
        print("   Equipped: " + items[equipped]["name"])
        print("   Damage: " + format.red + str(items[equipped]["damage"]) + format.end)
        print("   Durability: " + format.green + str(equippedDurability) + format.end + "/" + format.blue + str(items[equipped]["durability"]) + format.end)
    else:
        print("   Equipped: None")
    print("")
    if inventory == []:
        cutsceneOther("Nothing in pockets!", 2, 0.01)
        input("\n  Press " + format.bold + "enter" + format.end + " to exit menu.  ")
        printMap()
    else:
        displayInventory = inventory
        playerDecision = ask("Inventory:", 2, displayInventory, 0.1)
        if displayInventory[playerDecision - 1] == "Exit menu":
            printMap()
        else:
            item = items[inventoryIDs[playerDecision - 1]]
            temp = playerDecision - 1
            said = ""
            action = ""
            print("")
            cutsceneOther(format.bold + item["name"] + format.end, 2, 0.01)
            print("  Damage: " + format.red + str(item["damage"]) + format.end)
            print("  Durability: " + format.green + str(inventoryDurability[playerDecision - 1]) + format.end + "/" + format.blue + str(item["durability"]) + format.end)
            print("  " + item["1"])
            print("  " + item["2"])
            print("  " + item["3"])
            print("  " + item["4"])
            print("  " + item["5"])
            print("")
            playerDecision = ask("Item options:", 1, ["Equip item", "Drop item", "Exit menu"], 0.1)
            if playerDecision == 1:
                if equipped != "None":
                    inventory.append(items[equipped]["name"])
                    inventoryIDs.append(equipped)
                    inventoryDurability.append(equippedDurability)
                equipped = inventoryIDs[temp]
                equippedDurability = inventoryDurability[temp]
                action = items[equipped]["name"] + " equipped."
                if items[equipped]["type"] == "melee":
                    said = fetchDialogue("player", "meleeweapongained")
                if items[equipped]["type"] == "ranged":
                    said = fetchDialogue("player", "rangedweapongained")
                inventory.pop(temp)
                inventoryIDs.pop(temp)
                inventoryDurability.pop(temp)
            if playerDecision == 2:
                action = "You drop the " + inventory[temp]
                inventory.pop(temp)
                inventoryIDs.pop(temp)
                inventoryDurability.pop(temp)
            if playerDecision == 3:
                printMap(fetchDialogue("player", "nevermind"))
            if shadows != []:
                rand = random.randint(1, int(5 / difficulty))
                if rand == 1:
                    heard = fetchDialogue("shadow", "sound")
                    rand = random.randint(0, len(shadows) - 1)
                    location = maps[building][shadows[rand]]["name"]
                    said = fetchDialogue("player", "heard")
                    action = "You hear " + heard + " coming from the " + location + "."
                    sanity = sanity - random.randint(0, 5)
            printMap(said, action)

def moveRoom():
    global x
    global y
    global room
    global sanity

    layout = maps[building]["layout"]
    movement = []
    if layout[y][x + 1] == "open":
        movement.append("Right")
    if layout[y][x - 1] == "open":
        movement.append("Left")
    if layout[y + 1][x] == "open":
        movement.append("Down")
    if layout[y - 1][x] == "open":
        movement.append("Up")
    movement.append("Stay in room")
    playerDecision = ask("Movement menu:", 2, movement, 0.1)
    if movement[playerDecision - 1] == 'Right':
        x = x + 2
    if movement[playerDecision - 1] == 'Left':
        x = x - 2
    if movement[playerDecision - 1] == 'Down':
        y = y + 2
    if movement[playerDecision - 1] == 'Up':
        y = y - 2
    room = layout[y][x]
    run = random.randint(1, 6)
    if run == 1:
        updateTime(10)
    if movement[playerDecision - 1] == "Stay in room":
        printMap(fetchDialogue("player", "nevermind"))
    else:
        if room in shadows:
            print(format.clear)
            print(maps[building][room]["side" + str(side)]["1s"])
            print(maps[building][room]["side" + str(side)]["2s"])
            print(maps[building][room]["side" + str(side)]["3s"])
            print(maps[building][room]["side" + str(side)]["4s"])
            print(maps[building][room]["side" + str(side)]["5s"])
            print(maps[building][room]["side" + str(side)]["6s"])
            print("\n  " + maps[building][room]["name"] + ", " + str(hours) + ":" + minutesstr + " " + period)
            print("  \"" + fetchDialogue("player", "saw") + "\"")
            print("")
            combat()
        else:
            said = ""
            action = ""
            if shadows != []:
                rand = random.randint(1, int(5 / difficulty))
                if rand == 1:
                    heard = fetchDialogue("shadow", "sound")
                    rand = random.randint(0, len(shadows) - 1)
                    location = maps[building][shadows[rand]]["name"]
                    said = fetchDialogue("player", "heard")
                    action = "You hear " + heard + " coming from the " + location + "."
                    sanity = sanity - random.randint(0, 5)
            printMap(said, action)

def combat():
    global headHealth
    global torsoHealth
    global leftArmHealth
    global rightArmHealth
    global leftLegHealth
    global rightLegHealth

    global equipped
    global equippedDurability
    global shadows
    global shadowhealth

    playerDecision = ask("Combat menu:", 2, ["Attack", "Block", "Dodge", "Exit menu"], 0.1)
    print("")

    if playerDecision == 1:
        updateTime(random.randint(1, 4) * 10)
        said = ""
        roll = random.randint(1, 10)
        currentshadow = shadows.index(room)
        if roll != 10:
            rand = random.randint(1,3)
            if rand == 3:
                said = fetchDialogue("player", "attacking")
            if equipped != "None":
                shadowhealth[currentshadow] = shadowhealth[currentshadow] - items[equipped]["damage"]
                equippedDurability = equippedDurability - 1
                action = (format.blue + items[equipped]["attack"] + "shadow." + format.end)
                if equippedDurability == 0:
                    action = action + "\n  " + format.red + format.bold + items[equipped]["break"] + format.end
                    equipped = "None"
            else:
                shadowhealth[currentshadow] = shadowhealth[currentshadow] - 1
                rand = random.randint(1,3)
                if rand == 3:
                    said = fetchDialogue("player", "attacking")
                rand = random.randint(1,2)
                if rand == 1:
                    leftArmHealth = leftArmHealth - 1
                else:
                    rightArmHealth = rightArmHealth - 1
                action = "You punch the shadow."
            action = action + enemyHit()
            action = action + "\n  " + format.green + "Your hit connects." + format.end
        else:
            rand = random.randint(1,5)
            if rand == 3:
                said = fetchDialogue("player", "attackmissed")
            if equipped != "None":
                action = (format.blue + items[equipped]["attack"] + "shadow." + format.end)
            else:
                action = (format.blue + "You swing at the shadow with your fists." + format.end)
            action = action + enemyHit()
            action = action + format.red + format.bold + "\n  Attack missed!" + format.end
            if equipped != "None":
                if items[equipped]["faildamage"] == "yes":
                    equippedDurability = equippedDurability - 1
        if shadowhealth[currentshadow] <= 0:
            action = action + "\n  " + format.green + format.bold + "The shadow dies." + format.end
            shadows.pop(currentshadow)
            shadowhealth.pop(currentshadow)
        printMap(said, action)
    if playerDecision == 2:
        updateTime(random.randint(1, 4) * 10)
        rand = random.randint(1, 3)
        said = ""
        action = ""
        if rand != 1:
            if equipped != "None":
                action = format.blue + "You brace for the next hit with your " + items[equipped]["name"] + "." + format.end
                block = 25
            else:
                action = format.blue + "You brace for the next hit." + format.end
                block = 20
            said = fetchDialogue("player", "successfulblock")
        else:
            action = format.red + format.bold + "You fail to block the hit in time!" + format.end
            said = fetchDialogue("player", "failedblock")
            block = 0
        action = action + enemyHit(block)
        printMap(said, action)
    if playerDecision == 3:
        updateTime(random.randint(1, 4) * 10)
        rand = random.randint(1, 5)
        if rand <= 2:
            action = format.blue + "You jump out of the way." + format.end
        else:
            action = format.red + format.bold + "You attempt to jump out of the way, but fail." + format.end
            action = action + enemyHit(10)
        printMap("", action)
    if playerDecision == 4:
        printMap(fetchDialogue("player", "nevermind"))

def enemyHit(block = 0):
    global headHealth
    global torsoHealth
    global leftArmHealth
    global rightArmHealth
    global leftLegHealth
    global rightLegHealth
    global sanity
    
    target = random.randint(1, 6)
    damage = random.randint(0, 25)
    sanity = sanity - random.randint(0,5)
    if target == 1:
        headHealth = (headHealth + block) - damage
        target = "head"
    if target == 2:
        torsoHealth = (torsoHealth + block) - damage
        target = "torso"
    if target == 3:
        leftArmHealth = (leftArmHealth + block) - damage
        target = "left arm"
    if target == 4:
        rightArmHealth = (rightArmHealth + block) - damage
        target = "right arm"
    if target == 5:
        leftLegHealth = (leftLegHealth + block) - damage
        target = "left leg"
    if target == 6:
        rightLegHealth = (rightLegHealth + block) - damage
        target = "right leg"

    return format.red + format.bold + "\n  The shadow hits you in the " + target + "." + format.end

def tutorial():
    print(format.clear)
    time.sleep(1)
    cutsceneOther(format.bold + "Welcome to the Last Night On Earth tutorial!" + format.end, 2, 0.05)
    time.sleep(1)
    cutsceneOther("This tutorial will teach you how to play the game.", 2, 0.05)
    time.sleep(0.75)
    cutsceneOther("Because that's what a tutorial is " + format.italic + "supposed" + format.end + " to do.", 2, 0.05)
    input("\n  Press " + format.bold + "enter" + format.end + " to continue.  ")

    print(format.clear)
    time.sleep(2)
    print("  ──────═══─────┐")
    print("                │")
    print("      o      ─┐ │")
    print("   ┌─┐    ║  ▓│ │")
    print("   │ │    ║  ▓│ │")
    print("   └─┘       ─┘ │")
    print("  ")
    print("\n  Apartment, 2:00am")
    print("")
    print("  1. Move")
    print("  2. Do")
    print("  3. Loot")
    print("  4. Inventory")
    print("  5. Leave room\n")
    time.sleep(2)
    cutsceneOther("Welcome to the apartment.", 2, 0.05)
    time.sleep(1)
    cutsceneOther("This is a really simplified version of the", 2, 0.05)
    cutsceneOther("house you will see in the story.", 2, 0.05)
    input("\n  Press " + format.bold + "enter" + format.end + " to continue.  ")
    
    print(format.clear)
    print("  ──────═══─────┐")
    print("                │")
    print("      o      ─┐ │")
    print("   ┌─┐    ║  ▓│ │")
    print("   │ │    ║  ▓│ │")
    print("   └─┘       ─┘ │")
    print("  ")
    print("\n  Apartment, 2:00am")
    print("")
    print("  1. Move")
    print("  2. Do")
    print("  3. Loot")
    print("  4. Inventory")
    print("  5. Leave room\n")
    cutsceneOther("Here is the playing menu.", 2, 0.05)
    time.sleep(1)
    cutsceneOther("At the top you can see the room you are currently in.", 2, 0.05)
    time.sleep(1)
    cutsceneOther("Below that is name of the room, and the time.", 2, 0.05)
    input("\n  Press " + format.bold + "enter" + format.end + " to continue.  ")

    print(format.clear)
    print("  ──────═══─────┐")
    print("                │")
    print("      o      ─┐ │")
    print("   ┌─┐    ║  ▓│ │")
    print("   │ │    ║  ▓│ │")
    print("   └─┘       ─┘ │")
    print("  ")
    print("\n  Apartment, 2:00am")
    print("")
    print("  1. Move")
    print("  2. Do")
    print("  3. Loot")
    print("  4. Inventory")
    print("  5. Leave room\n")
    cutsceneOther("To start, try moving to the other side of the room by selecting option 1 in the menu.", 2, 0.05)
    time.sleep(0.75)
    cutsceneOther("To select an option, you just type the number corresponding to the option.", 2, 0.05)
    playerDecision = input("  > ")
    if playerDecision != 1:
        print("")
        cutsceneOther("Normally I'd let you fiddle around with all the controls even", 2, 0.05)
        cutsceneOther("though this is a tutorial, but to be honest, I'm lazy", 2, 0.05)
        print("")
        cutsceneOther("I'm just gonna make it as if you typed 1 like you were supposed to", 2, 0.05)
        input("\n  Press " + format.bold + "enter" + format.end + " to continue.  ")
    print(format.clear)
    print("  │          ┌─┐ ")
    print("  │          │ │ ")
    print("  │   o      └─┘ ")
    print("  │              ")
    print("  ├──┬────┬┬┬┐   ")
    print("  └──┴────┴──┴───")
    print("  ")
    print("\n  Apartment, 2:01am")
    print("")
    print("  1. Move")
    print("  2. Do")
    print("  3. Loot")
    print("  4. Inventory")
    print("  5. Leave room\n")
    cutsceneOther("So you're able to move. That's good.", 2, 0.05)
    cutsceneOther("There's some cabinets there, how about you loot those?", 2, 0.05)
    playerDecision = input("  > ")
    if playerDecision != 3:
        print("")
        cutsceneOther("I'm gonna pull a Stanley Parable", 2, 0.05)
        print("")
        cutsceneOther("I'm just gonna make it as if you typed 3 like you were supposed to", 2, 0.05)
        input("\n  Press " + format.bold + "enter" + format.end + " to continue.  ")   
    
def demoContent():
    print(format.clear)
    x = 1
    while x <= int(demo["itemascii"]["headerlength"]):
        print(demo["itemascii"][str(x)])
        x = x + 1
    input("\n  Press " + format.bold + "enter" + format.end + " to return to the menu.  ")
    mainMenu()

mainMenu()