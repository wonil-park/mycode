#!/usr/bin/python3

def showInstructions():
    print('''
        RPG Game
        ========
        Commands:
          go/move [direction]
          get [item] / get all
        ''')


def showStatus():
    print('---------------------------')
    print('You are in the ' + currentRoom)
    print('Inventory : ' + str(inventory))
    if "item" in rooms[currentRoom] and len(rooms[currentRoom]['item']) > 0:
        for item in rooms[currentRoom]['item']:
            print('You see a ' + item)
    print("---------------------------")

commands = {
    'go': ['go', 'move', 'travel', 'walk'],
    'get': ['take', 'pick up', 'get'],
    'use': ['use', 'eat', 'drink']
}

inventory = []

rooms = {

    'Hall': {
        'south': 'Kitchen',
        'east': 'Dining Room',
        'item': ['key', 'leaflet'],
    },

    'Kitchen': {
        'north': 'Hall',
        'item': ['monster'],
    },
    'Dining Room': {
        'west': 'Hall',
        'south': 'Garden',
        'item': ['potion']
    },
    'Garden': {
        'north': 'Dining Room'
    }
}

currentRoom = 'Hall'

showInstructions()

# loop forever
while True:

    showStatus()

    move = ''
    while move == '':
        move = input('>')

    # split allows an items to have a space on them
    # get golden key is returned ["get", "golden key"]
    move = move.lower().split(" ", 1)

    # if they type 'go' first
    if commands['go'].__contains__(move[0]):
        # check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            # set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        # there is no door (link) to the new room
        else:
            print('You can\'t go that way!')

    # if they type 'get' first
    if commands['get'].__contains__(move[0]):
        # if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom]:
            if move[1] in rooms[currentRoom]['item']:
                inventory.append(move[1])
                # display a helpful message
                print(move[1] + ' got!')
                # delete the item from the room
                del rooms[currentRoom]['item']
            elif move[1] == 'all':
                for i, item in enumerate(rooms[currentRoom]['item']):
                    inventory.append(item)
                del rooms[currentRoom]['item']
        else:
            # tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('A monster has got you... GAME OVER!')
        break

    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        break
