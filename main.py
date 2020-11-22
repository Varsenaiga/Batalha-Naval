import numpy as np
#from board import *
from functions import *

class bcolors:
    WARNING = '\033[93m'
    ENDC = '\033[0m'

def main():
    i = start_game()
    i = 1 #definido pois para já não há outro gamemode
    if i == 1:
        TesteDrive()
    elif i==2:
        PvC()
    elif i==2:
        PvP()
    elif i==2:
        online()
    else:
        print("ERROR: não conhecido")
        quit()


def start_game():
    print("\t\u272E----------------------------------\u272E\n\t\u272EBem vindo ao Batalha Naval do NEEC\u272E\n\t\u272E----------------------------------\u272E\n")
    while 1:
        try:
            user_input = input("\tEscolha do modo de jogo:\n\t1.TesteDrive\t2.P vs C\t3.P vs P\t4.Online\n\tOu escolhe \"exit\".\n\t")
            i = int(user_input)
            if i > 4 or i < 1:
              raise Exception()
        except:
            if(user_input=='exit'): quit()
            print(f"{bcolors.WARNING}\tEscolha de gamemode não valida.{bcolors.ENDC}\n")
        else:
            return user_input

main()
