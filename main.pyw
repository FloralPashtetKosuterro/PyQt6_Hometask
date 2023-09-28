from PyQt6 import QtWidgets
import sys

class MainTry(QtWidgets.QDialog):
    def secondprog(self):
        self.secondlabel = QtWidgets.QLabel("Вы купили 3 арбуза за 10 рублей. Инвестировав в пустоту, вы стали жертвой "
                                            "кибершарлатана.")
        self.vvbox = QtWidgets.QVBoxLayout()
        self.vvbox.addWidget(self.secondlabel)
        self.setLayout(self.vvbox)

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.mylabel = QtWidgets.QLabel("Приветствую! Это сетевая торговля арбузами.\n"
                                        "\tМеня зовут Изя Барабаш.\n "
                                        "1 арбуз = 3 рубля, 3 арбуза = 10 рублей")
        self.mybth = QtWidgets.QPushButton("Купить")
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.mylabel)
        self.vbox.addWidget(self.mybth)
        self.mybth.clicked.connect(self.secondprog)
        self.setLayout(self.vbox)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainTry()
    window.setWindowTitle("Сделано по учебнику")
    window.resize(250, 70)
    window.show()
    sys.exit(app.exec())
