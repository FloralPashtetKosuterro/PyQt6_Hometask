from PyQt6 import QtWidgets
import sys

class MainTry(QtWidgets.QDialog):
    def secondprog(self):
        self.mylabel.setText("Вы купили 3 арбуза за 10 рублей. Инвестировав в пустоту, вы стали жертвой "
                             "кибершарлатана.")
    def thirdprog(self):
        self.mylabel.setText('Вы купили один арбуз, но еврей был колдуном и в результате заставил купить два.'
                             '\t\nПриходите ещё!')


    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.mylabel = QtWidgets.QLabel("Приветствую! Это сетевая торговля арбузами.\n"
                                        "\tМеня зовут Изя Барабаш.\n "
                                        "1 арбуз = 3 рубля, 3 арбуза = 10 рублей")
        self.mybth = QtWidgets.QPushButton("Купить один арбуз")
        self.mybth2 = QtWidgets.QPushButton("Купить три арбуза")
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.mylabel)
        self.vbox.addWidget(self.mybth)
        self.vbox.addWidget(self.mybth2)
        self.mybth.clicked.connect(self.thirdprog)
        self.mybth2.clicked.connect(self.secondprog)
        self.setLayout(self.vbox)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainTry()
    window.setWindowTitle("Сделано по учебнику")
    window.resize(250, 70)
    window.show()
    sys.exit(app.exec())
