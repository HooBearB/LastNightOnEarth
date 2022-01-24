## LNoE Documentation
## (Scuffed edition)

Not a final product, THIS DOCUMENT WILL BE UPDATED TO INCLUDE ALL PURPOSES OF FUNCTIONS EVENTUALLY!

## Introduction
Hi. If you, for one reason or another, have stumbled upon this repository, it might become immediately clear that I have no idea what I'm doing. The thing is, you would be completely right.

LNoE is pretty much held together with metaphorical popsticle sticks and glue. I am clueless, and bad at whatever I do.
I'm hoping I am able to write this document in enough detail that one can understand my botched logic without having to bang their head against a wall for a couple hours.
With that being said, I'm gonna actually start *writing* this document.

## Needed modules
- random is needed to have certain actions result in an unpredictable chance. Combat and looting relies on this.
- json is needed to load the json files that define the map, items, and dialogue.
- os is needed to find the json files in the program. It finds the directory the LNoE python file is in, and joins it with the suffix of the file needed.
- time is needed for me to tick everyone off by making intro sequences and cutscenes extremely long.

## Format class
The format class is a collection of ANSI escape prefixes that I attach before some text to give it fancy effects such as colour and italics.

## defineVariables()
Creates and globalizes needed variables with default values.

x and y are location variables. The system I use, however, is kind of screw-y. x positions work normally like a normal graph, but the y positions are completely flipped. For example, here's a sample map with x and y values as they would be read by LNoE's program.

["x,y"]
[
    ["0,0", "1,0", "2,0"]
    ["0,1", "1,1", "2,1"]
    ["0,2", "1,2", "2,2"]
]

day, hours, minutes, and period all are time variables. The period variable denotes AM/PM timing.
headHealth, torsoHealth, leftArmHealth, rightArmHealth, leftLegHealth, and rightLegHealth are used to manage body part damage.
sanity will eventually be used to trigger certain events, or story content.
inventory is a list of names for items in the player's current inventory.
inventoryIDs handles the item IDs in the inventory, as seen in items.json.
inventoryDurability handles the durability values for inventory items.
equipped and equippedDurability is handled as if it were an inventory item, but also applies changes to those items.
shadows handles the locations of all shadows currently spawned.
shadowhealth handles the health values of all shadows on the map.
side handles the side of the room the player is viewing from.
looted handles all loot pools that include the reloot json tag that have already been searched.
building handles which map should be accessed by the program.
huntstart manages when the shadows should start spawning.
level is currently unused, and is planned to be a way to track chapters.

## testVariables()
Defines special variables for testing. Still requires defineVariables() to be run to play normally.

## updateTime(addminutes)
- addminutes: int

Used to update time variables for display. [addminutes] is an integer that changes the amount of minutes before formatting.

## ask(message, indent, options, delay)
- message: string
- indent: int
- options: string table
- delay: float

Used to ask for input from the player. [message] defines the printed string put before the options, while [indent] specifies how many spaces to put before all contents printed during the calling of ask(). [options] is a table that displays options out in a list. [delay] is a number associated with the amount of time the program waits to print the next option in the list.

## askString(message, indent)
- message: string
- indent: int

Currently unused. Prints [message] with [indent] spaces and asks for a string response.

## genShadows()
Generates shadow objects on the map, and moves them at random each turn. Shadows can only move to adjacent tiles, but can phase through walls.

## checkHealth()
Determines what text to print for crippled limbs and whether or not an injury is terminal.

## fetchDialogue(speaker, prompt)
- speaker: string
- prompt: string 

Retrieves a random piece of dialogue based on [speaker] and [prompt].

## cutsceneDialogue(message, indent, delay)
- message: string
- indent: int
- delay: float

Prints [message] out in scrolling text along with quotation marks, with [indent] amount of spaces. [delay] is the amount of time in between printing of characters.

## cutsceneOther(message, indent, delay)
- message: string
- indent: int
- delay: float

Same as cutsceneDialogue() but doesn't print quotation marks.

## death(target)
- target: string

Prints the death message using [target]. Also contains ending cutscenes if the player chooses to watch them.

## mainMenu()
Prints the main menu and segways into different functions.

## startGame()
Plays opening cutscene, defines variables, and opens flow to normal gameplay.

## loadGame()
Placeholder. Currently allows player to jump straight into gameplay with set difficulty.

## startNew()
Defines location variables and opens dialogue, as well as transitioning to gameplay.

## printMap(dialogue, action)
- dialogue: string; "" by default
- action: string; "" by default

Prints out map using the given json data. Prints [dialogue] and [action] below the map, as well as time data. Prompts flow into other functions.

## move()
Moves the player to the other side of the room.

## do()
Segways into loot() and checkSelf(), prints a dialogue bit if the player chooses to not call one of those functions.

## loot()
Fetches a random item from the given lootpool and puts it in the player's inventory, also defining durability and display values.

## checkSelf()
Displays the player's health values for each limb, as well as current sanity.

## inv()
Allows the player to equip objects, or drop them.

## moveRoom()
Checks exits from the current room and allows the player to move around open areas.

## combat()
Allows the player to engage in combat with a shadow in the room, if there is one. Attacking uses the equipped object to deal damage to the current shadow in the room, while block allows the player to reduce damage. Dodge allows the player to negate damage entirely, albiet with a reduced chance.

## enemyhit(block)
block: int; 0 by default

Calculates how much damage a shadow deals to the player, subtracting [block]. This also applies the damage to a random body part.

## tutorial()
An unfinished tutorial. All elements are manual, and eventually when this finished will be running items like printMap() and loot() instead of manually printing statements.

## demoContent()
Prints out all the individual parts of the democontent.json file.