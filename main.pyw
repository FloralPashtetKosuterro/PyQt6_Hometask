from PyQt6 import QtWidgets, QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
import sys

from PyQt6.QtWidgets import QLabel


class MainTry(QtWidgets.QDialog):
    def secondprog(self):
        self.mylabel.setText("Вы купили 3 арбуза за 10 рублей. Инвестировав в пустоту, вы стали жертвой "
                             "кибершарлатана.")
        self.mybth.setText('Связаться с продавцом')
        self.mybth2.setText('Оставить отзыв')
        self.mybth.clicked.connect(self.answer)
        self.mybth2.clicked.connect(self.answer)

    def thirdprog(self):
        self.mylabel.setText('Вы купили один арбуз, но еврей был колдуном и в результате заставил купить два.'
                             '\t\n Неясным способом эти арбузы свалились на вас. Спасибо за покупку!')
        self.mybth.setText('Связаться с продавцом')
        self.mybth2.setText('Оставить отзыв')
        self.mybth.clicked.connect(self.answer)
        self.mybth2.clicked.connect(self.answer)

    def answer(self):
        self.mylabel.setText('Автоответчик: Добрый вечер, это контора Васи Пупкина')
        self.mybth.setText('Выключить программу')
        self.mybth2.setText('Выключить программу')
        self.mybth.clicked.connect(app.quit)
        self.mybth2.clicked.connect(app.quit)

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.mylabel = QtWidgets.QLabel("Приветствую! Это сетевая торговля арбузами.\n"
                                        "\tМеня зовут Изя Барабаш.\n "
                                        "1 арбуз = 3 рубля, 3 арбуза = 10 рублей")
        self.mybth = QtWidgets.QPushButton("Купить один арбуз")
        self.mybth2 = QtWidgets.QPushButton("Купить три арбуза")
        self.vbox = QtWidgets.QVBoxLayout()
        self.label = QLabel(self)
        self.pixmap = QPixmap('melon.jpg')
        self.label.setPixmap(self.pixmap)
        self.mylabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.vbox.addWidget(self.mylabel)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.mybth)
        self.vbox.addWidget(self.mybth2)
        self.mybth.clicked.connect(self.thirdprog)
        self.mybth2.clicked.connect(self.secondprog)
        self.setLayout(self.vbox)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainTry()
    window.setWindowTitle("Сделано по учебнику")
    window.resize(300, 300)
    window.show()
    sys.exit(app.exec())
