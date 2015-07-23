from sys import exit
import random

# classes
class bcolors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# variables
lives = 3
tip1 = "\nTIP: To check your inventory type 'inventory'\n"
tip2 = "\nTIP: To check your lives type 'lives'\n"
tip3 = "\nTIP: To return to your previous location type 'back'\n"
tip4 = "\nTIP: To exit the game type 'exit'\n"
tip5 = "\nTIP: To drink health potion type 'heal'\n"

welcome_messsage = (bcolors.HEADER + "\n>>> Welcome to the Quest of Hero! <<<" + bcolors.END)

# lists
tips = [tip1, tip2, tip3, tip4, tip5]
inventory = []

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

def heal():
    global lives
    global inventory

    if "health potion" not in inventory:
        print bcolors.YELLOW + '''
    >>> Sorry, you don't have health potion <<<<
    ''' + bcolors.END
    elif lives == 3 and "health potion" in inventory:
        print bcolors.YELLOW + '''
    >>> Sorry, your health is full <<<<
    ''' + bcolors.END
    else:
        lives += 1
        inventory.remove("health potion")

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

def info_cant_understand():
    print bcolors.RED + '''
    ---------------------------
    | I can't understand you! |
    ---------------------------
    ''' + bcolors.END

def info_cant_dothat():
    print bcolors.RED + '''
    ----------------------
    | You can't do that! |
    ----------------------
    ''' + bcolors.END

def info_choose_door():
    print bcolors.RED + '''
    -----------------------------
    | Please, choose your door! |
    -----------------------------
    ''' + bcolors.END

# I really don't like code here, it's not universal :\
def choose_room_gold(direction):
    print '''
    -----------------------------------------------------------------------------
    | The room became lighter, now you can see two doors, one in the center,    |
    | another in the ''' + direction + ''' from you. Which one you will choose? |
    -----------------------------------------------------------------------------
    '''
    another_choice = raw_input("> Make your choice: ")
    if direction in another_choice:
        lab_room()
    elif "center" in another_choice:
        puzzle_room()
    elif "back" in another_choice:
        info_cant_dothat()
        choose_room_gold(direction)
    elif "lives" in another_choice:
        check_lives()
        gold_room()
    elif "exit" in another_choice:
        exit(0)
    else:
        info_choose_door()
        choose_room_gold(direction)

def choose_room_puzzle(direction):
    print '''
    -----------------------------------------------------------------------------
    | The room became lighter, now you can see two doors, one in the center,    |
    | another in the ''' + direction + ''' from you. Which one you will choose? |
    -----------------------------------------------------------------------------
    '''
    another_choice = raw_input("> Make your choice: ")
    if direction in another_choice:
        monster_room()
    elif "center" in another_choice:
        boss_room()
    elif "back" in another_choice:
        info_cant_dothat()
        choose_room_puzzle(direction)
    elif "lives" in another_choice:
        check_lives()
        gold_room()
    elif "exit" in another_choice:
        exit(0)
    else:
        info_choose_door()
        choose_room_puzzle(direction)

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

        if "left" in choice and not inventory:
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
        elif "heal" in choice:
            heal()
            start()
        else:
            info_cant_dothat()
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
            choose_room_gold("right")
        elif "take" and "shield" in choice:
            inventory.append('shield')
            print bcolors.BLUE + '''
    --------------------------------------
    | Now you have the shield, good job! |
    --------------------------------------
            ''' + bcolors.END
            choose_room_gold("right")
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
            info_cant_understand()
            gold_room()

def lab_room():
    tip_rand()
    global lives
    global inventory

    if lives == 0:
        dead()
    else:
        print '''
    -------------------------------------------------------------------------
    | You're in the Great Sorcerer's labaratory.                            |
    | You see a lot of interesting stuff here.                              |
    | Bat wings, skulls, and old books with strange sparkly names on them.  |
    | On the big table you can see three potions:                           |
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
    | This was not a good idea to drink     |
    | a potion in sorcerer's room...        |
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
        elif "red" in choice:
            print bcolors.RED + '''
    ---------
    | BOOM! |
    ---------
            ''' + bcolors.END
            damage()
            start()
        elif "mix" and ("blue" and "green") in choice:
            print bcolors.BLUE + '''
    ---------------------------
    | Walls are dissapeared...|
    ---------------------------
    ''' + bcolors.END
            monster_room()
        elif "inventory" in choice:
            check_invent()
            lab_room()
        elif "lives" in choice:
            check_lives()
            lab_room()
        elif "back" in choice and not inventory:
            turn_back(start())
        elif "exit" in choice:
            exit(0)
        elif "back" in choice and 'shield' or 'sword' in inventory:
            info_cant_do_that()
            lab_room()
        else:
            info_cant_understand()
            lab_room()

def puzzle_room():
    tip_rand()
    global lives

    if lives == 0:
        dead()
    else:
        print '''
    -----------------------------------------------
    | You walked into a new room.                 |
    | Door is suddenly closed behind you.         |
    | You can hear strange voice, it whispers     |
    | "If EELS + MARK + BEST + WARY = EASY        |
    | What does HELP + BARK + WARD + LEAD equal?" |
    -----------------------------------------------
        '''
    choice = raw_input('> Your answer: ')

    # positive:
    if choice == "HARD":
        choice_new_room("right")
    elif "inventory" in choice:
        check_invent()
        lab_room()
    elif "lives" in choice:
        check_lives()
        lab_room()
    elif "back" in choice:
        info_cant_dothat()
        puzzle_room()
    elif "exit" in choice:
        exit(0)
    else:
        info_cant_understand()
        puzzle_room()

def monster_room():
    tip_rand()
    global lives

    if lives == 0:
        dead()
    else:
        print '''
    -----------------------------------------------
    | You walked into a new room.                 |
    | Door is suddenly closed behind you.         |
    | It's reaaaally stinks here                  |
    | You can see a huge green goblin in the room |
    | He's looks really sick and angry            |
    | What will you do?                           |
    -----------------------------------------------
        '''
        exit(0)

def boss_room():
    tip_rand()
    global lives

    if lives == 0:
        dead()
    else:
        print '''
        You're in the bosse's room
        '''

# start the game
print welcome_messsage
start()
