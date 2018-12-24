from colorama import Fore, Back, Style
from SETTINGS import STATICS

def write(color, msg):
    if STATICS.DEBUG == "1":
        if color == "red":
            print(Fore.RED + msg)
        elif color == "blue":
            print(Fore.BLUE + msg)
        elif color == "green":
            print(Fore.GREEN + msg)
        elif color == "yellow":
            print(Fore.YELLOW + msg)
        print(Style.RESET_ALL)