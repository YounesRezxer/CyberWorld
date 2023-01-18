# start banner !
# libraries

import os
import sys
import time
from colorama import Fore
from webbrowser import open_new

#------------------------------------------------------------------------------------- !

def banner():
    os.system('clear')
    time.sleep(0.1)

    print(Fore.GREEN + """
    ▄████▄▓██   ██▓ ▄▄▄▄   ▓█████  ██▀███      █     █░ ▒█████   ██▀███   ██▓    ▓█████▄ 
   ▒██▀ ▀█ ▒██  ██▒▓█████▄ ▓█   ▀ ▓██ ▒ ██▒   ▓█░ █ ░█░▒██▒  ██▒▓██ ▒ ██▒▓██▒    ▒██▀ ██▌
   ▒▓█    ▄ ▒██ ██░▒██▒ ▄██▒███   ▓██ ░▄█ ▒   ▒█░ █ ░█ ▒██░  ██▒▓██ ░▄█ ▒▒██░    ░██   █▌
   ▒▓▓▄ ▄██▒░ ▐██▓░▒██░█▀  ▒▓█  ▄ ▒██▀▀█▄     ░█░ █ ░█ ▒██   ██░▒██▀▀█▄  ▒██░    ░▓█▄   ▌
   ▒ ▓███▀ ░░ ██▒▓░░▓█  ▀█▓░▒████▒░██▓ ▒██▒   ░░██▒██▓ ░ ████▓▒░░██▓ ▒██▒░██████▒░▒████▓ 
   ░ ░▒ ▒  ░ ██▒▒▒ ░▒▓███▀▒░░ ▒░ ░░ ▒▓ ░▒▓░   ░ ▓░▒ ▒  ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒░▓  ░ ▒▒▓  ▒ 
     ░  ▒  ▓██ ░▒░ ▒░▒   ░  ░ ░  ░  ░▒ ░ ▒░     ▒ ░ ░    ░ ▒ ▒░   ░▒ ░ ▒░░ ░ ▒  ░ ░ ▒  ▒ 
   ░       ▒ ▒ ░░   ░    ░    ░     ░░   ░      ░   ░  ░ ░ ░ ▒    ░░   ░   ░ ░    ░ ░  ░ 
   ░ ░     ░ ░      ░         ░  ░   ░            ░        ░ ░     ░         ░  ░   ░    
   ░       ░ ░           ░                                                        ░""")

#------------------------------------------------------------------------------------- !

def infoles_1():
    time.sleep(0.1)
    print(Fore.WHITE + "\n   [" + Fore.RED + "01" + Fore.WHITE + "]" + " CREATE A PASSWORD\n")
    time.sleep(0.1)
    print(Fore.WHITE + "   [" + Fore.RED + "02" + Fore.WHITE + "]" + " DEVELOPER\n")
    time.sleep(0.1)
    print(Fore.WHITE + "   [" + Fore.RED + "03" + Fore.WHITE + "]" + " EXIT\n")

#------------------------------------------------------------------------------------- !

def developer():
    time.sleep(0.1)
    url = "https://github.com/YounesRezxer"
    url2 = "https://www.youtube.com/@Blackamooz"
    open_new(url)
    open_new(url2)
    print(Fore.WHITE + "\n   [" + Fore.RED + "-" + Fore.WHITE + "]" + " YOUTUBE:@BLACKAMOOZ\n")
    time.sleep(0.1)
    print(Fore.WHITE + "   [" + Fore.RED + "-" + Fore.WHITE + "]" + " DEVELOPER:MR.YOUNES\n")
    time.sleep(0.1)
    print(Fore.WHITE + "   [" + Fore.RED + "-" + Fore.WHITE + "]" + " GITHUB:YounesRezxer\n")
