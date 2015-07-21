from sys import exit
import random

# variables
lives = 3
tip1 = "\nTIP: To check your inventory type 'inventory'\n"
tip2 = "\nTIP: To check your lives type 'lives'\n"
tip3 = "\nTIP: To return to your previous location type 'back'\n"
tip4 = "\nTIP: To exit the game type 'exit'\n"

# lists
tips = [tip1, tip2, tip3, tip4]
inventory = []

# classes
# use this class like this: print bcolors.RED + "Warning: No active frommets remain. Continue?" + bcolors.END
class bcolors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# this function is for hero's inventory checking
def check_invent():
    if len(inventory) == 0:
        print bcolors.YELLOW + '''
    >>> Your inventory is empty <<<
    ''' + bcolors.END
    else:
        for i in inventory:
            print bcolors.YELLOW + '''
    >>> You have the %r in your inventory <<<
            ''' % i + bcolors.END

# this function is for hero's lives checking
def check_lives():
    global lives
    if lives == 1:
        print bcolors.RED + '''
    >>> You have only 1 live left, be careful! <<<
        ''' + bcolors.END
    else:
        print bcolors.YELLOW + '''
    >>> You have %d lives <<<
        ''' % lives + bcolors.END

def dead():
    print bcolors.RED + '''
    >>> You have no lives left, you're dead! <<<
    ''' + bcolors.END
    exit(0)

def tip_rand():
    global tips
    rand_tips = random.choice(tips)
    print rand_tips

def turn_back(function):
    function()

def damage():
    global lives
    lives = lives - 1
    return lives

# start the game
def start():
    tip_rand()
    global lives

    if lives == 0:
        dead()
    else:
        print '''
    ------------------------------------------------------
    | You're in the middle of the strange dark cave.     |
    | You can see two doors.                             |
    | One in the left and another in the right from you. |
    | Which one you will choose?                         |
    ------------------------------------------------------
    '''
        choice = raw_input('> Choose your door (left or right): ')

        if "left" in choice:
            gold_room()
        elif "right" in choice:
            lab_room()
        elif "inventory" in choice:
            check_invent()
            start()
        elif "lives" in choice:
            check_lives()
            start()
        elif "exit" in choice:
            exit(0)
        elif "back" in choice:
            turn_back(start())
        else:
            print '''
    == Please choose your door ==
    '''
            start()

def gold_room():
    tip_rand()
    global lives

    if lives == 0:
        dead()
    else:
        print '''
    -----------------------------------------------
    | You're in the gold room.                    |
    | It's full of gold coins,                    |
    | In front of you there are two big statues.  |
    | You can feel that they're watching you.     |
    | One of the statues has a sword.             |
    | Another one has a shield.                   |
    | What will you do?                           |
    -----------------------------------------------
        '''
        choice = raw_input("> Make your choice: ")

        if "coin" in choice:
            print bcolors.BLUE + '''
    --------------------------------------------------------------
    | You feel that floor is going down from over your feet.     |
    | You falling down into darkness...                          |
    --------------------------------------------------------------
            ''' + bcolors.END
            damage()
            start()
        elif "take" and "sword" in choice:
            inventory.append('sword')
            print bcolors.BLUE + '''
    -------------------------------------
    | Now you have the sword, good job! |
    -------------------------------------
            ''' + bcolors.END
            print '''
    '''
            gold_room()
        elif "take" and "shield" in choice:
            inventory.append('shield')
            print bcolors.BLUE + '''
    --------------------------------------
    | Now you have the shield, good job! |
    --------------------------------------
            ''' + bcolors.END
            gold_room()
        elif "inventory" in choice:
            check_invent()
            gold_room()
        elif "lives" in choice:
            check_lives()
            gold_room()
        elif "back" in choice:
            turn_back(start())
        elif "exit" in choice:
            exit(0)
        else:
            print bcolors.BLUE + '''
    ---------------------------
    | I can't understand you! |
    ---------------------------
            ''' + bcolors.END
            gold_room()

def lab_room():
    tip_rand()
    global lives

    if lives == 0:
        dead()
    else:
        print '''
    -------------------------------------------------------------------------
    | You're in the Great Sorcerer's labaratory.                            |
    | You see a lot of interesting stuff here.                              |
    | Bat wings, skulls, and old books with strange sparkly names on them.  |
    | On the big wood table you can see three poitions:                     |
    | o A blue one.                                                         |
    | o A green one.                                                        |
    | o And a red one.                                                      |
    | What will you do?                                                     |
    -------------------------------------------------------------------------
    '''
        choice = raw_input('> Make your choice: ')
        if "drink" in choice:
            print bcolors.BLUE + '''
    -----------------------------------------
    | You feel a fire inside you.           |
    | You last thought in this life was:    |
    | "This is was a not good idea to drink |
    | a potion in Sorcerer's room"          |
    -----------------------------------------
        ''' + bcolors.END
            damage()
            start()
        elif "take" in choice:
            print bcolors.BLUE + '''
    -----------------------------------------------------
    | You can hear the steps behind you.                |
    | You turned around immediatly and last thing       |
    | that you can see was the angry old mans' face.    |
    | He put a very powerful spell on you.              |
    -----------------------------------------------------
    ''' + bcolors.END
            damage()
            start()
#        elif ""
        elif "inventory" in choice:
            check_invent()
            lab_room()
        elif "lives" in choice:
            check_lives()
            lab_room()
        elif "back" in choice:
            turn_back(start())
        elif "exit" in choice:
            exit(0)
        else:
            print bcolors.BLUE + '''
            I can't understand you! ''' + bcolors.END
            gold_room()

start()
