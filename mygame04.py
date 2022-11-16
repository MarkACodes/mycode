#!/usr/bin/python3
"""Driving a simple game framework with
   a dictionary object | Alta3 Research"""


def showInstructions():
    """Show the game instructions when called"""
    # print a main menu and the commands
    print('''
    RPG Game
    ========
    Commands:
      go [direction]
      get [item]
    ''')


def showStatus():
    """determine the current status of the player"""
    # print the player's current location
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # print what the player is carrying
    print('Inventory:', inventory)
    # check if there's an item in the room, if so print it
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")


# an inventory, which is initially empty
inventory = []

## A dictionary linking a room to other rooms
rooms = {

    'Hall': {
        'south': 'Kitchen',
        'east': 'Dining Room',
        'item': 'key'
    },

    'Kitchen': {
        'north': 'Hall',
        'item': 'monster',
    },
    'Dining Room': {
        'west': 'Hall',
        'south': 'Garden',
        'item': 'potion'
    },
    'Garden': {
        'north': 'Dining Room'
    }
}

# start the player in the Hall
currentRoom = 'Hall'

# breaking this while loop means the game is over
while True:
    showStatus()
    """determine the current status of the player"""
    # print the player's current location
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # print what the player is carrying
    print('Inventory:', str(inventory))
    # check if there's an item in the room, if so print it
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")

    showInstructions()
    move = ''
    while move == '':
        move = input('>')

# the player MUST type something in
# otherwise input will keep asking
move = ''
while move == '':
    move = input('>')

# normalizing input:
# .lower() makes it lower case, .split() turns it to a list
# therefore, "get golden key" becomes ["get", "golden key"]
move = move.lower().split(" ", 1)

# if they type 'go' first
if move[0] == 'go':
    # check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
        # set the current room to the new room
        currentRoom = rooms[currentRoom][move[1]]
    # if they aren't allowed to go that way:
    else:
        print('You can\'t go that way!')

    # if they type 'get' first
    if move[0] == 'get':
        # make two checks:
        # 1. if the current room contains an item
        # 2. if the item in the room matches the item the player wishes to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            # add the item to their inventory
            inventory.append(move[1])
            # display a helpful message
            print(move[1] + ' got!')
            # delete the item key:value pair from the room's dictionary
            del rooms[currentRoom]['item']
        # if there's no item in the room or the item doesn't match
        else:
            # tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

    ## If a player enters a room with a monster
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('A monster has got you... GAME OVER!')
        # break
    sys.exit()

    ## Define how a player can win
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
    # break out of the while loop
    # break
    sys.exit()

    # todo: Class- build a Player class object that shows current location and health
    def __init__(self):
        self.health = 100
        self.location = 'Hall'
        self.inventory = []

    def showStatus(self):
        """determine the current status of the player"""
        # print the player's current location
        print('---------------------------')
        print('You are in the ' + self.location)
        # print what the player is carrying
        print('Inventory:', self.inventory)
        # check if there's an item in the room, if so print it
        if "item" in rooms[self.location]:
            print('You see a ' + rooms[self.location]['item'])
        print("---------------------------")


# Create a method that triggers a level-up message where users can allocate points to strength, intelligence, and speed.
    def level_up(self):
        print("You have leveled up! You can now allocate 5 points to your stats.")
    input("How many points would you like to allocate to strength? ")
    input("How many points would you like to allocate to intelligence? ")
    input("How many points would you like to allocate to speed? ")



# enter combat mode
    def combat(self, monster=None):
        print("You have encountered a monster! You must fight to the death!")
        # create random damage from hero and monster and loop until one is dead
        while self.health > 0 and monster.health > 0:
            self.health -= monster.damage
            monster.health -= self.damage
            print("You have", self.health, "health left.")
            print("The monster has", monster.health, "health left.")
        if self.health <= 0:
            print("You have died.")






