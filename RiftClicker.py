import win32api
import pyfiglet
from os import system, name
from random import random

from colorama import init
from colorama import Fore, Back, Style
from time import sleep
from pynput.mouse import Controller, Button

mouse = Controller()
init()


def clear():
    if name == "nt":
        _ = system('cls')
    else:
        _ = system('clear')


print(Fore.LIGHTBLUE_EX + pyfiglet.figlet_format("Rift Clicker"))
print(Fore.WHITE + "Thanks for downloading Rift Clicker!")
print("Input your base Left Click CPS")
lcps = int(input(": "))
clear()
print(Fore.LIGHTBLUE_EX + pyfiglet.figlet_format("Rift Clicker"))
print(Fore.WHITE + "Input your base Right Click CPS")
rcps = int(input(": "))
clear()

leftdelay = (1 / lcps)
rightdelay = (1 / rcps)

# Make Title Screen
print(Fore.LIGHTBLUE_EX + pyfiglet.figlet_format("Rift Clicker"))
print(Fore.WHITE + "Rift Clicker is now active!")
print("Mouse5 For Left Click, Mouse4 for Right Click.")
print("Left: " + str(lcps) + " CPS | Right: " + str(rcps) + " CPS")
print("Made by Recrucity#4040")


# Left Clicker
def lmb():
    if LKeyState < 0:
        mouse.click(Button.left, 1)
        sleep(leftdelay * random() + 1 / 2 * leftdelay)
    else:
        pass


# Right Clicker
def rmb():
    if RKeyState < 0:
        mouse.click(Button.right, 1)
        sleep(rightdelay * random() + 1 / 2 * rightdelay)
    else:
        pass


# Check for keypresses to enable clicker
while True:
    LKeyState = win32api.GetAsyncKeyState(0x06)
    lmb()

    RKeyState = win32api.GetAsyncKeyState(0x05)
    rmb()
