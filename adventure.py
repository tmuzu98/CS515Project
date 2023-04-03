import json
import sys
import inspect
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("map_file", help="Path to the map file")
args = parser.parse_args()

with open(args.map_file) as f:
    game_map = json.load(f)


global current_room
current_room = 0
inventory = []
verbs = {}
global count
count = 0


def register(func):
    verbs[func.__name__] = func
    return func


def print_room():
    room = game_map[current_room]
    print(f"> {room['name']}\n\n{room['desc']}\n")
    if 'items' in room:
        items_str = ', '.join([f"{item} " for item in room['items']])
        print(f"Items: {items_str}")
        print()
    exits_str = ''.join([f"{exit} " for exit in room['exits']])
    print("Exits:", exits_str)
    print()


@register
def go(direction):
    global count
    count += 1
    if count > 20:
        print(
            f"No of attempts used {count}.\n You have used all of your attempts. Better Luck next time!!")
        sys.exit()
    global current_room
    room = game_map[current_room]
    if direction in room['exits']:
        next_room = room['exits'][direction]
        if next_room is not None:
            if next_room == 5:
                if 'key' in inventory and 'love potion' in inventory:
                    print(
                        "Congratulations! You have unlocked the Chamber of Secrets and won the game!")
                    print(
                        "Huray you have Romilda with the love potion to infatuate Harry! You completed all the objectives")
                    sys.exit()
                elif 'key' in inventory:
                    print(
                        "Congratulations! You have unlocked the Chamber of Secrets and won the game!")
                    print(
                        "You broke Romilda's heart, you couldn't find the love potion for")
                    sys.exit()
                else:
                    print("You do not have the key yet go and find the keys first!!")
                    print_room()

            else:
                current_room = next_room
                print(f"You go {direction}.\n")
                print_room()
        else:
            print("You can't go that way.")
    else:
        print(f"There's no way to go {direction}")


@register
def look():
    print_room()


@register
def get(item):
    room = game_map[current_room]
    if 'items' in room and item in room['items']:
        inventory.append(item)
        room['items'].remove(item)
        print(f"You pick up the {item}.")
    else:
        print(f"There's no {item} anywhere.")


@register
def drop(item):
    if item in inventory:
        room = game_map[current_room]
        room['items'].append(item)
        inventory.remove(item)
        print(f"You drop the {item}.")
    else:
        print(f"You don't have {item} in your inventory.")


@register
def show_inventory():
    if len(inventory) == 0:
        print("You're not carrying anything.")
    else:
        print("Inventory:")
    for i in inventory:
        print(" ", i)


@register
def show_help():
    valid_verbs = []
    for verb, func in verbs.items():
        argspec = inspect.getfullargspec(func)
        if argspec.args:
            argstring = ' ...'
        else:
            argstring = ''
        valid_verbs.append(f"{verb}{argstring}")
    print("You can run the following commands:")
    for verb in valid_verbs:
        if verb == "show_inventory":
            verb = 'inventory'
        elif verb == "show_help":
            verb = 'help'
        print(f"  {verb}")


try:
    print(""" Welcome to The marauders' a magical map that reveals the whole
    of Hogwarts School of Witchcraft and Wizardry, the map includes:
    1. Gryffindor Common Room,
    2. The Hogwarts Library,
    3. Professor Severus Snape's Office,
    4. The Great Hall,
    5. The Headmaster's office,
    6. The Chamber of Secrets
        Your object is to somehow reach the Chamber of Secrets with the help of the map.
        Also there is a  little help Romilda aslks of you to get love potion from
        Prof. Snape's office. Help a girl out to get to her love.
        Beware!!! you have limited number of attempts to move around the School.
        Have Fun!!
        And currently you are here ||>
    # """)
    print_room()
    while True:
        try:
            action = input(
                "What would you like to do? ").strip().lower().split()
        except EOFError:
            print("Use 'quit' to exit.")
            continue

        verb = action[0]
        if verb == "go":
            if len(action) > 1:
                direction = action[1]
                go(direction)
            else:
                print("Sorry, you need to 'go' somewhere.")
        elif verb == "look":
            look()
        elif verb == "get":
            if len(action) > 1:
                item = " ".join(action[1:])
                get(item)
            else:
                print("Sorry, you need to 'get' something.")
        elif verb == "drop":
            if len(action) > 1:
                item = " ".join(action[1:])
                drop(item)
            else:
                print("Sorry, you need to 'drop' something.")
        elif verb == "inventory":
            show_inventory()
        elif verb == "quit":
            print("Goodbye!")
            sys.exit()
        elif verb == "help":
            show_help()
        else:
            print("I don't know how to  do that.")
except KeyboardInterrupt:
    print("\nGoodbye!")
