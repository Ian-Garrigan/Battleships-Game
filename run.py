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