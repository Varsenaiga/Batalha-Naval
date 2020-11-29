from board import *
import random

MAX_rondas = 50

###############################################################################################
# Estas funções são as funções correspondentes a cada modo de jogo
# Para já vamos fazer a função que corresponde à criação de um taboleiro por parte do computador e o utilizador fica a adivinhar quais as posições dos barcos

def TesteDrive():
    counter_jogadas = 1

    check = True

    tab = tabuleiro("computador")
    generate_board(tab)
    tab.print_tabuleiro("enemy")

    print(f"{bcolors.OKBLUE}\tTabuleiro criado, é a vez do jogador jogar.{bcolors.ENDC}\n")
    while(check):
        make_play(tab)
        print(f"\n\t{bcolors.HEADER}Balas restantes: {MAX_rondas-counter_jogadas}{bcolors.ENDC}")
        tab.print_tabuleiro("enemy")
        counter_jogadas += 1
        check = False
        for i in tab.boat_list:
            if i.state == True:
                check = True
                continue
        if counter_jogadas > MAX_rondas and check == True:
            print(f"{bcolors.FAIL}\n\tPerdeste o jogo. Não conseguiste acertar em todos os barcos antes das balas acabarem.{bcolors.ENDC}\n")
            return 0

    print(f"{bcolors.OKGREEN}\n\tParabéns venceste o jogo ainda com {MAX_rondas-counter_jogadas} rondas por jogar.{bcolors.ENDC}\n")
    return 1


def PvC():
    counter_jogadas = 1

    Win = False
    Lose = False

    tab_pc = tabuleiro("computador")
    generate_board(tab_pc)
    tab_player = tabuleiro("Player")
    generate_board(tab_player)

    while(not Lose and not Win):
        print(f"\n\t{bcolors.HEADER}Balas restantes: {MAX_rondas-counter_jogadas}{bcolors.ENDC}")
        print(f"{bcolors.OKGREEN}\n\tRonda do Bot:{bcolors.ENDC}\n")
        bot_play(tab_player)
        tab_player.print_tabuleiro("friend")
        print(f"{bcolors.OKGREEN}\n\tRonda do player:{bcolors.ENDC}\n")
        make_play(tab_pc)
        tab_pc.print_tabuleiro("enemy")
        counter_jogadas += 1
        Win = True
        for i in tab_pc.boat_list:
            if i.state == True:
                Win = False
                continue
        Lose = True
        for i in tab_player.boat_list:
            if i.state == True:
                Lose = False
                continue
        if counter_jogadas > MAX_rondas and check == True:
            print(f"{bcolors.FAIL}\n\tPerdeste o jogo. Não conseguiste acertar em todos os barcos antes das balas acabarem.{bcolors.ENDC}\n")
            return 0

    if Win and Lose:
        print(f"{bcolors.WARNING}\n\tEmpantas-te com um pc... uheuheuhe{bcolors.ENDC}\n")
        return 2
    elif Win:
        print(f"{bcolors.OKGREEN}\n\tParabéns venceste o jogo ainda com {MAX_rondas-counter_jogadas} rondas por jogar.{bcolors.ENDC}\n")
        return 1
    else:
        print(f"{bcolors.FAIL}\n\tPerdeste o jogo. Todos os teus barcos foram afundados.{bcolors.ENDC}\n")
        return 0

def PvP():
    print(f"{bcolors.FAIL}\tNão implementado.{bcolors.ENDC}\n")

def Online():
    print(f"{bcolors.FAIL}\tNão implementado.{bcolors.ENDC}\n")


###############################################################################################
# Esta função corresponde a criação e inserção dos barcos no tabuleiro
# Para já esta função vai estar a criar um tabuleiro automaticamente. Mais para a frente pode vir a ser feito a parte de o utilizador fazer o seu taboleiro

def generate_board(table):
    letters = ('A','B','C','D','E','F','G','H','I','J','a','b','c','d','e','f','g','h','i','j')
    numbers = (1,2,3,4,5,6,7,8,9,10)

    boat_sizes = (2, 2, 2, 2, 3, 3 ,3, 4, 4, 5)
    boat_orientations = ('vertical', 'horizontal')

    valid = False

    if table.name == "computador":
        for i in boat_sizes:
            valid = False
            while not valid:
                orientation = random.choice(boat_orientations)
                if orientation == 'vertical':
                    row = random.randint(0, Size_Board-i)
                    column = random.randint(0, Size_Board-1)
                    if table.insert_boat(row, column, i, 'vertical'):
                        valid = True
                else:
                    row = random.randint(0, Size_Board-1)
                    column = random.randint(0, Size_Board-i)
                    if table.insert_boat(row, column, i, 'horizontal'):
                        valid = True
    else:
        for i in boat_sizes:
            valid = False
            while not valid:
                play =  input(f"\n\tEscolhe a posição inicial do barco de tamanho {i}:")
                if (len(play) != 2 and len(play) != 3) or not play[0].isalpha() or not play[1:].isdigit() or play[0] not in letters or int(play[1:]) not in numbers:
                    print("\n\tInput invalido. As cordenadas devem ser uma letra (A-J) seguidas de um número (1-10).")
                else:
                    orientation = input("\n\tEscolhe a horientação do barco (H ou V):")
                    if orientation not in ['H','V','h','v']:
                        print("\n\tA orientação deve ser H se horizontal ou V se vertical")
                    else:
                        play=play.upper()
                        column = letters.index(play[0])
                        row = numbers.index(int(play[1:]))
                        print(f"{row} e {column}")
                        if orientation == 'V' or orientation == 'v':
                            if row+i > Size_Board: row=row-i
                            if table.insert_boat(row, column, i, "vertical"):
                                valid = True
                            else: print("\n\tJá existe um barco por baixo daquele que queres meter")
                        elif orientation == 'H' or orientation == 'h':
                            while column+i > Size_Board: column=column-i
                            if table.insert_boat(row, column, i, "horizontal"):
                                valid = True
                            else: print("\n\tJá existe um barco por baixo daquele que queres meter")
            table.print_tabuleiro("friend")



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
        play =  input('\n\tPlease choose the target coordinates: ')
        if (len(play) != 2 and len(play) != 3) or not play[0].isalpha() or not play[1:].isdigit() or play[0] not in letters or int(play[1:]) not in numbers:
            valid = False
            print('\n\tInvalid input. Coordinates must be a letter (A-J) followed by a number (1-10).')
            continue
        if not table_pc.check_hit(int(play[1:])-1, letter_to_pose(play[0])):
            valid = False
            print('\n\tInvalid input. You already shot in those coordinates.')
            continue
    table_pc.shoot(int(play[1:])-1, letter_to_pose(play[0]))



def letter_to_pose(letter):
    let = np.array(['A','B','C','D','E','F','G','H','I','J','a','b','c','d','e','f','g','h','i','j'])

    column = int(np.where(let == letter)[0])

    if column > 9:
        column = column - 10

    return column


def bot_play(table_pc):
    shot = tuple()
    play = list(shot)
    letters = ('A','B','C','D','E','F','G','H','I','J','a','b','c','d','e','f','g','h','i','j')
    numbers = (1,2,3,4,5,6,7,8,9,10)
    turn = True
    valid = False
    while not valid:
        valid = True
        play =  f"{random.choice(letters)}{random.choice(numbers)}"
        if not table_pc.check_hit(int(play[1:])-1, letter_to_pose(play[0])):
            valid = False
            #print('Invalid input. You already shot in those coordinates.')
            continue
    table_pc.shoot(int(play[1:])-1, letter_to_pose(play[0]))
