# import copy
from random import randint, random
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import main


class jeuGUI:


    def __init__(self, jeu):
        self._jeu = jeu
        self._pion = 0
        self.__root = Tk()
        self.__root.title('LE JEU QUI REND FOU')


        self.__frame1 = Frame(self.__root)
        self.__frame1.grid(row=0, column=0, rowspan=3)
        self.__frame1.config(height=self._jeu.getSize() * 10 + 1000, width=self._jeu.getSize() * 10 + 1000,
                             relief=RIDGE, bg='black', borderwidth=10)

        self.__frame2 = Frame(self.__root)
        self.__frame2.grid(row=0, column=1)
        self.__frame2.config(relief=RIDGE, borderwidth=3)


        # gérer la hauteur des cases
        self.__canvas = Canvas(self.__frame1)
        self.__canvas.config(height=65 * self._jeu.getSize()+1,
                             width=self._jeu.getSize() * 65 + 1, highlightthickness=0, bd=0)
        self.__canvas.place(x=100, y=80)
        self.__canvas.bind('<Button-1>', self.clickCell)


        self.__playerTurnText = StringVar()
        self.__playerTurn = Label(self.__frame2, textvariable=self.__playerTurnText)
        self.__playerTurn.pack()




    #Les joueurs
    def nextPlayer(self):
        self.__jeu.nextPlayer()




    #Pour demarer le jeu
    def start(self):
        self.drawGame()
        self.__root.mainloop()

    def mainLoop(self):
        self.__root.mainloop()

    def drawGame(self):
        self.__canvas.delete("all")
        self.__playerTurnText.set("Player " + str(self._jeu.getPlayer() + 1))
        self.drawCells()
        self.__canvas.update()


    #cellule et case du plateau
    def drawCells(self):
        circle_margin = 4
        print(self._jeu.getSize())
        for x in range(self._jeu.getSize()):
            for y in range(self._jeu.getSize()):
                self.__canvas.create_rectangle(x * 65, y * 65, (1 + x) * 65, (1 + y) * 65,
                                               fill='black', outline="blue")
                self.__canvas.create_oval(x * 30 + circle_margin, y * 30 + circle_margin, (x + 1) * 30 - circle_margin,
                                          (y + 1) * 30 - circle_margin, fill=self._pion.getColor(i))

    # configuration du click pour poser un pion
    def clickCell(self, event):
        x = event.x // 65
        if self._jeu.possible(x):
            self._jeu.put(x)
            self._jeu.nextPlayer()
            self.drawGame()


    #message fin de jeu
    def endOfGame(self):
        tkinter.messagebox.showinfo(message='Player ' + str(self._jeu.getPlayer() + 1) + ' a Gagné !')




size = 12
jeux = main.jeu(size, 2)
a = jeuGUI(jeux)
a.start()
