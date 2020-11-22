from board import *
import random


###############################################################################################
# Estas funções são as funções correspondentes a cada modo de jogo
# Para já vamos fazer a função que corresponde à criação de um taboleiro por parte do computador e o utilizador fica a adivinhar quais as posições dos barcos

def TesteDrive():
    counter_jogadas = 0;

    check = True

    tab = tabuleiro("computador")
    generate_board(tab)
    tab.print_tabuleiro()

    print(f"{bcolors.OKBLUE}\tTabuleiro criado é a vez do jogador jogar.{bcolors.ENDC}\n")
    while(check):
        make_play(tab)
        tab.print_tabuleiro()
        counter_jogadas += 1
        check = False
        for i in tab.boat_list:
            if i.state == True:
                check = True
                continue


###############################################################################################
# Esta função corresponde a criação e inserção dos barcos no tabuleiro
# Para já esta função vai estar a criar um tabuleiro automaticamente. Mais para a frente pode vir a ser feito a parte de o utilizador fazer o seu taboleiro

def generate_board(table):

    if table.name == "computador":
        boat_sizes = (2, 2, 2, 2, 3, 3 ,3, 4, 4, 5)
        boat_orientations = ('vertical', 'horizontal')

        for i in boat_sizes:
            Flag = True
            while Flag:
                orientation = random.choice(boat_orientations)
                if orientation == 'vertical':
                    row = random.randint(0, Size_Board-i)
                    column = random.randint(0, Size_Board-1)
                    if table.insert_boat(row, column, i, 'vertical'):
                        Flag = False
                else:
                    row = random.randint(0, Size_Board-1)
                    column = random.randint(0, Size_Board-i)
                    if table.insert_boat(row, column, i, 'horizontal'):
                        Flag = False
    else:
        return 0 #para já, depois pode vir a ser feito uma cena para o utilizador



###############################################################################################
# Esta função verifica se a escolha das coordenada à qual se quer disparar é válida
#

def make_play(table_pc):
    shot = tuple()
    play = list(shot)
    letters = ('A','B','C','D','E','F','G','H','I','J','a','b','c','d','e','f','g','h','i','j')
    numbers = (1,2,3,4,5,6,7,8,9,10)
    turn = True
    valid = False
    while not valid:
        valid = True
        play =  input('Please choose the target coordinates: ')
        if (len(play) != 2 and len(play) != 3) or not play[0].isalpha() or not play[1].isdigit() or play[0] not in letters or int(play[1:]) not in numbers:
            valid = False
            print('Invalid input. Coordinates must be a letter (A-J) followed by a number (1-10).')
            continue
        if not table_pc.check_hit(int(play[1:])-1, letter_to_pose(play[0])):
            valid = False
            print('Invalid input. You already shot in those coordinates.')
            continue
    table_pc.shoot(int(play[1:])-1, letter_to_pose(play[0]))



def letter_to_pose(letter):
    let = np.array(['A','B','C','D','E','F','G','H','I','J','a','b','c','d','e','f','g','h','i','j'])

    column = int(np.where(let == letter)[0])

    if column > 9:
        column = column - 10

    return column
