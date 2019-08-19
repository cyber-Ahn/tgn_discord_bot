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

def log(msg, home_phat):
    if STATICS.LOG == "1":
        with open(home_phat + "SETTINGS/log.txt", "a") as f:
            f.write(msg+"\n")
            f.close()

if __name__ == "__main__":
    print("This is a library, it can not be started directly.")