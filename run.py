# Import libraries needed

from random import randint
import os
import sys


os.system("clear")
print("  ___  ___ ______________   ____  ______ _________  ____")
print(" / _ )/ _ /_  __/_  __/ /  / __/ / __/ // /  _/ _ \\/ __/")
print("/ _  / __ |/ /   / / / /__/ _/  _\\ \\/ _  // // ___/\\ \\ ")
print("/____/_/ |_/_/   /_/ /____/___/ /___/_//_/___/_/  /___/ ")
print("")
print("        Get ready for BATTLESHIP! Good luck soldier.")
print("   Typically this game is played on a 10 x 10 grid.")
print("      But you can opt for a smaller game board.")
print("   Please press Enter after each input.")
print("\u001b[31m---------------------------------------------------\033[0;0m")
while True:
    BATTLE_AREA = input(" Enter battle area size (range 1-10): ")
    if BATTLE_AREA.isdigit():
        BATTLE_AREA = int(BATTLE_AREA)
        if BATTLE_AREA > 1 and BATTLE_AREA <= 10:
            print(" ")
            print("Lets Rock n Roll kid, you know what to do.")
            print("-------------------------------------------------------")
            break
        else:
            print(" Please pick a number ranging from 1 to 10")
    else:
        print("No letters soldier and keep it less than 11!.")
        continue


def user_battle_size():
    """
    Creating the grid
    """
    for user_battle_size.x in range(ZONE):
        GRID.append(["-"] * ZONE)
    return ZONE

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def deploy_battle_area():
    """
    battle area construction
    """
    letters = ALPHABET[0: (ZONE)]
    print("      %s%s" % (" ", " ".join(letters)))
    each_row = 1
    for row in GRID:
        if each_row <= 9:
            print("     %d|%s|" % (each_row, "|".join(row)))
        else:
            print("    %d|%s|" % (each_row, "|".join(row)))
        each_row += 1

def ship_dropper():
    """
    Dropping the ships onto the grid.
    """
    ships_to_drop = 0
    global FLEET
    if ZONE <= 3:
        FLEET = 1
        while ships_to_drop != FLEET:
            row_placemarker = randint(1, (ZONE))
            column_placemarker = randint(1, (ZONE))
            ship_coordinates = [row_placemarker, column_placemarker]
            SHIP_LOCATION.append(ship_coordinates)
            ships_to_drop += 1
    elif ZONE < 8 and ZONE > 3:
        FLEET = 3
        while ships_to_drop != FLEET:
            row_placemarker = randint(1, (ZONE))
            column_placemarker = randint(1, (ZONE))
            ship_coordinates = [row_placemarker, column_placemarker]
            SHIP_LOCATION.append(ship_coordinates)
            ships_to_drop += 1
    else:
        FLEET = 10
        while ships_to_drop != FLEET:
            row_placemarker = randint(1, (ZONE))
            column_placemarker = randint(1, (ZONE))
            ship_coordinates = [row_placemarker, column_placemarker]
            SHIP_LOCATION.append(ship_coordinates)
            ships_to_drop += 1

def guesstimate():

    """
    Taking user input and storing it. Then adjusting the board accordingly.
    """
    global SHIPWRECK
    for attempts in range((ZONE*ZONE) // 2):
        strikes = int((ZONE*ZONE) // 2)
        print(" ")
        print(' Battle outpost: "Ahoy captain,'
              f'we have {strikes - attempts} strikes left and counting!."')
        print('  Captain: "Give me an update on the fleet, over."')
        print(f'Outpost: "{FLEET - SHIPWRECK} remain Captain, over and out"')
        col_chance = None
        while True:
            col_chance = input("Prepare to fire!Enter your LETTER: ")
            if col_chance.isalpha() and len(col_chance) == 1:
                col_chance = col_chance.lower()
                col_chance = ord(col_chance) - 96
                break
            else:
                deploy_battle_area()
                print(" Pick your letter captain, the grid will guide you.")
                continue
        row_chance = None
        while True:
            row_chance = input(" Letter confirmed, enter a NUMBER to target: ")
            if row_chance.isdigit():
                row_chance = int(row_chance)
                break
            else:
                deploy_battle_area()
                print("  Keep within the range supplied captain, over.")
                continue
        picked_row = row_chance
        picked_col = col_chance
        player_guess = [picked_row, picked_col]
        if player_guess in SHIP_LOCATION:
            print("-------------------------------------------------------")
            print("          Boo yaaa! Enemy down, great strike captain.")
            print("-------------------------------------------------------")
            GRID[picked_row - 1][picked_col - 1] = "\u001b[32mO\033[0;0m"
            SHIPWRECK += 1
        elif (attempts + 1) - strikes == 0:
            print("-------------------------------------------------------")
            print("                   Battleships destroyed, game over.")
            print("   Incoming heli to position, gather the troops Captain!")
            print("-------------------------------------------------------")
        elif (picked_row < 1 or picked_row > ZONE) \
                or (picked_col < 1 or picked_col > ZONE):
            print("-------------------------------------------------------")
            print("     We cant hit that target captain out of range!")
            print("              Choose wisely, victory is upon us!")
            print(f"          How about we try striking rows: 1-{ZONE}")
            print(f"          & columns: A-{ALPHABET[ZONE - 1]}")
            print("-------------------------------------------------------")
        elif (GRID[picked_row - 1][picked_col - 1]) == "\u001b[31mX\033[0;0m":
            print("-------------------------------------------------------")
            print("      Commander...You guessed that one already...")
            print("-------------------------------------------------------")
        elif (GRID[picked_row - 1][picked_col - 1]) == "\u001b[32mO\033[0;0m":
            print("-------------------------------------------------------")
            print("      Commander...You guessed that one already...")
            print("-------------------------------------------------------")
        else:
            print("-------------------------------------------------------")
            print(" Try agin, GO captain!")
            print("-------------------------------------------------------")
            GRID[picked_row - 1][picked_col - 1] = "\u001b[31mX\033[0;0m"
        if SHIPWRECK == FLEET:
            deploy_battle_area()
            print("-------------------------------------------------------")
            print(" hallelujah!")
            print("   Whats that smell Captain? ")
            print(" Thats the smell of victory boy. Now grab me a beer.")
            print(" Tell my wife and kids im coming home.")
            print("-------------------------------------------------------")
            break
        deploy_battle_area()
    attempts += 1

def begin_battleships():
    """
    Orderly queue when running the game
    """
    user_battle_size()
    print("               Fasten Up, its Battleship time!")
    print("-------------------------------------------------------")
    print(" ")
    deploy_battle_area()
    ship_dropper()
    guesstimate()


def restart():
    """
    Funct for restarting the game
    """
    play = input("Play again? Type: yes \
        Quit? Type: no ").lower()
    while True:
        if play == "no":
            exit()
        elif play == "yes":
            # Code brought from stackoverflow
            print("------------------------------------")
            print("argv was", sys.argv)
            print("sys.executable was", sys.executable)
            print("restart now")
            print("------------------------------------")
            os.execv(sys.executable, ['python'] + sys.argv)
        else:
            print("please type either yes or no")
            restart()


# Global variables
ZONE = BATTLE_AREA
GRID = []
SHIP_LOCATION = []
FLEET = 10
SHIPWRECK = 0

begin_battleships()
restart()
