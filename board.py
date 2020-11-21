import numpy as np

Size_Board = 10


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class boat:
    def __init__(self, size, orientation, row, column, state):
        self.size = size
        self.orientation = orientation
        self.pos = {row, column}
        self.state = state


class tabuleiro:

    def __init__(self, name):
        self.data = np.array([['Water' for i in range(Size_Board)] for j in range(Size_Board)])  # Water; Boat; Miss; Hit
        self.name = name
        self.boat_list = list()


    def print_tabuleiro(self):
        print(f"\n\tTabuleiro do {self.name}\n\t")
        string = "\t  A B C D E F G H I J"
        for i in range(Size_Board):
            string += f"\n\t{i} "
            for k in range(Size_Board):
                if(self.data[i, k] == 'Water'):
                    string += f"{bcolors.OKCYAN}W {bcolors.ENDC}"
                elif(self.data[i, k] == 'Boat'):
                    string += f"{bcolors.OKCYAN}W {bcolors.ENDC}"
                elif(self.data[i, k] == 'Hit'):
                    string += f"{bcolors.FAIL}H {bcolors.ENDC}"
                elif(self.data[i, k] == 'Miss'):
                    string += f"M "

        print(string)


    def check_water(self, row, column, size, orient):
        if orient == 'vertical':
            final_pose = row + size
            for i in range(row, final_pose):
                if(self.data[i, column] != 'Water'):
                    return False
        elif orient == 'horizontal':
            final_pose = column + size
            for i in range(column, final_pose):
                if(self.data[row, i] != 'Water'):
                    return False

        return True


    def check_hit(self, row, column):
        if(self.data[row, column] == 'Water' or self.data[row, column] == 'Boat'):
            return True
        else:
            return False


    def shoot(self, row, column):
        if self.check_hit(row, column):
            if self.data[row, column] == 'Water':
                self.data[row, column] = 'Miss'
                return 'Miss'
            elif self.data[row, column] == 'Boat':
                self.data[row, column] = 'Hit'
                return 'Hit'
            else:
                return 'error'
        else:
            return 'error'


    def insert_boat(self, row, column, size, orient):
        self.boat_list.append(boat(size, orient, row, column, True))
        if self.check_water(row, column, size, orient):
            if orient == 'vertical':
                final_pose = row + size
                for i in range(row, final_pose):
                    self.data[i, column] = 'Boat'
            elif orient == 'horizontal':
                final_pose = column + size
                for i in range(column, final_pose):
                    self.data[row, i] = 'Boat'
        else:
            return False

        return True