# The tool of the cyber world for creating passwords and passwordlists is available for you !!!

import sys
from modules import banner
from colorama import Fore
from modules import Create_password

while True:
    try:

        banner.banner()
        banner.infoles_1()
        input1 = input(Fore.LIGHTWHITE_EX + "   CyberWorld ~# " + Fore.RED + "")


    except KeyboardInterrupt:
        print("")
        sys.exit()


    if input1 == "1":
        try:

            banner.banner()
            Create_password.password()
            input(Fore.WHITE + "\n   [" + Fore.RED+ "-" + Fore.WHITE + "]" +"BACK TO THE TOOLS MENU . . . ")

        except KeyboardInterrupt:
            print("")
            sys.exit()

    elif input1 == "2":
        try:

            banner.banner()
            banner.developer()
            input(Fore.WHITE + "\n   [" + Fore.RED+ "-" + Fore.WHITE + "]" +"BACK TO THE TOOLS MENU . . . ")

        except KeyboardInterrupt:
            print("")
            sys.exit()


    elif input1 == "3":
        print("")
        sys.exit() 