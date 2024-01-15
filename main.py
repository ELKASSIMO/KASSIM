
class Pion:

    def __init__(self, state = 0):

        self.__state = state


    def getState(self):
        return self.__state

    def setState(self, state):
        self.__state = state



    def getVisualIcon(self):
        if self.__state == 0:
            return 'O'
        elif self.__state == 1:
            return 'X'
        else:
            return '?'

    def getColor1(self, i):
        if self.__board[i] == 0:
            return 'black'
        elif self.__board[i] == 1:
            return 'red'
        elif self.__board[i] == 2:
            return 'yellow'

    def getColor2(self,i):
        if self.__board[i] == 0:
            return 'black'
        elif self.__board[i] == 1:
            return 'orange'
        elif self.__board[i] == 2:
            return 'blue'






class jeu :
    def __init__(self,n, player):
        self.__n = n
        self.__player = player
        "self.__nbLines = nbLines"
        "self.__nbColumns = nbColumns"
        self.__list = self.generate_plateau()


    def getSize(self):
        return self.__n

    def getPlayer(self):
        return self.__player
















    def generate_plateau(self):
        plateau = [[Pion(0) for _ in range(self.__n) ] for _ in range(self.__n)]
        return plateau

    def afficher_plateau(plateau):
        for line in plateau:
            print(" | ".join(ligne))
            print("_" * 35)

    def display(self):
        for line in range(self.__n):
            for column in range(self.__n):
                print(self.__list[line][column].getVisualIcon, end=' ')
            print("")






