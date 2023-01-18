from colorama import Fore
import random
import os
def password():

    print(Fore.WHITE + "\n   [" + Fore.RED + "-" + Fore.WHITE + "]" + "ENTER THE PASSWORD NUMBER, TRY TO BE ABOVE 8 !\n")

    passrange = int(input(Fore.WHITE + "\n   [" + Fore.RED + "~" + Fore.WHITE + "]" + 'PLEASE ENTER THE PASSWORD RANGE : ' + Fore.RED + ""))
    alefba = ('&//abcdefglomnp123456789_*#$@!%ASDFGHJKLMNBVCXZQWERTYUIOP')


    if passrange >= 8:

        for i in range(passrange):
            i = random.choice(alefba)
            print(i, end= '')
            

    else:
        print('You Can Not Choice >8 Number !')