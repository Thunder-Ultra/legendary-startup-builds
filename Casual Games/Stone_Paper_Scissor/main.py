#!/usr/bin/env python3

from random import randint
from typing import Container
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Enjoy ! Stone Paper Scissor')

        self.heading = QLabel('Click yours to Begin !')
        
        stone = QPushButton('Stone')
        paper = QPushButton('Paper')
        scissor = QPushButton('Scissor')

        stone.clicked.connect(self.S)
        paper.clicked.connect(self.P)
        scissor.clicked.connect(self.Sc)
        
        self.msg = QLabel()
        self.msg.setText('This is our Communication Portal')

        layout = QHBoxLayout()
        for W in stone,paper,scissor : layout.addWidget(W)
                
        container = QWidget()
        container.setLayout(layout)
        
        parent_layout = QVBoxLayout()
        for f in self.heading,container : parent_layout.addWidget(f)

        parent =  QWidget()
        parent.setLayout(parent_layout)

        self.setCentralWidget(parent)
        status = self.statusBar()
        status.addWidget(self.msg)


    def initiate(self,player):
        bot_turn = randint(1,3)
        D = player-bot_turn
        turns = 'Stone','Paper','Scissor'
        print('\n----------------\n {} vs {} \n----------------'.format(turns[player-1],turns[bot_turn-1]))
        if D==0:
            self.msg.setText("Perfect Tie")
            print('RESULT | There is no happiness nor sadness !')
        elif D in (1,-2):
            self.msg.setText('Congratulations ! You Won')
            print('RESULT | Player Won')
        else:
            self.msg.setText('I won !')
            print("RESULT | Player Lost")

    def S(self)     : self.initiate(1)
    def P(self)     : self.initiate(2)
    def Sc(self)    : self.initiate(3)

app = QApplication([])
main = MainWindow()
main.show()
app.exec_()
