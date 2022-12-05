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

# Global variables
ZONE = BATTLE_AREA
GRID = []
SHIP_LOCATION = []
FLEET = 10
SHIPWRECK = 0

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