class pion:
    def __init__(self, state=0):
        self.__state = state

    def getState(self):
        return self.__state
    def setState(self, state):
        self.__state = state



class jeu:
    def __init__(self, n, player):
        self.__n = n
        self.__player = player
        self.__list = self.generate_plateau()
        self.__pions_placed = [[-1] * n for _ in range(n)]  # Example: -1 for empty, 0 for player 1, 1 for player 2
    def getColor(self, x, y):
        return self.__list[x][y]


    #Obtenir la taille du plateu
    def getSize(self):
        return self.__n

    #Tous ce qui concerne les joueurs
    def getPlayer(self):
        return self.__player
    def nextPlayer(self):
        self.__player = (self.__player + 1) % 2

    #Fonction pour que le clic marche
    def possible(self, column):
        # Vérifiez si la colonne est valide (dans les limites du plateau)
        if 0 <= column < self.__n:
            # Vérifiez si la colonne n'est pas déjà pleine
            return self.__list[0][column].getState() == 0
        else:
            return False
    def put(self, column):
        row = self.find_empty_row(column)
        if row != -1:
            print("ligne", row, "colonne:", column)
            self.__list[row][column].setState(self.__player+1)
            self.__pions_placed[row][column] = self.__player+1
        else:
            print("colonne est pleine")
    def find_empty_row(self, column):
        # Parcourez les lignes de bas en haut pour trouver la première ligne vide
        for row in range(self.__n - 1, -1, -1):
            if self.__pions_placed[row][column] == -1:
                return row
        # La colonne est pleine
        return -1

    def again(self):
        for i in range(self.__n):
            if self.__list[i] == 0:
                return True
        return False

    #generer le plateau
    def generate_plateau(self):
        plateau = [[pion(0) for _ in range(self.__n)] for _ in range(self.__n)]
        return plateau
    def afficher_plateau(self, plateau):
        for line in plateau:
            print(" | ".join(line))
            print("_" * 35)
    def display(self):
        for line in range(self.__n):
            for column in range(self.__n):
                print(self.__list[line][column].getVisualIcon(), end=' ')
            print("")
