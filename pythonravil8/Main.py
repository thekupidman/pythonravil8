from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys

class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(400, 320)

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack1 = QtWidgets.QWidget()
        self.stack2 = QtWidgets.QWidget()
        self.stack3 = QtWidgets.QWidget()
        self.stack4 = QtWidgets.QWidget()
        self.stack5 = QtWidgets.QWidget()

        self.Window1UI()
        self.Window2UI()
        self.Window3UI()
        self.Window4UI()
        self.Window5UI()

        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)
        self.QtStack.addWidget(self.stack5)

    def Window1UI(self):
        self.stack1.resize(400, 320)

        self.label1_1 = QtWidgets.QLabel(self.stack1)
        self.label1_1.setText("Вас приветствует система")
        self.label1_1.setGeometry(0, 10, 400, 50)
        self.label1_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label1_1.setFont(QtGui.QFont("Times", 16, QtGui.QFont.Bold))

        self.label1_2 = QtWidgets.QLabel(self.stack1)
        self.label1_2.setText("быстрого анкетирования!")
        self.label1_2.setGeometry(0, 45, 400, 50)
        self.label1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label1_2.setFont(QtGui.QFont("Times", 14, QtGui.QFont.Bold))

        self.label1_3 = QtWidgets.QLabel(self.stack1)
        self.label1_3.setText("Тема - Периоды жизни!")
        self.label1_3.setGeometry(0, 150, 400, 50)
        self.label1_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label1_3.setFont(QtGui.QFont("Times", 18, QtGui.QFont.Bold))

        self.btn1_1 = QtWidgets.QPushButton(self.stack1)
        self.btn1_1.setText("Выход")
        self.btn1_1.setGeometry(QtCore.QRect(60, 250, 120, 40))

        self.btn1_2 = QtWidgets.QPushButton(self.stack1)
        self.btn1_2.setText("Начать")
        self.btn1_2.setGeometry(QtCore.QRect(220, 250, 120, 40))

    def Window2UI(self):
        self.stack2.resize(400, 320)

        self.label2_1 = QtWidgets.QLabel(self.stack2)
        self.label2_1.setText("Выберите любимую кашу")
        self.label2_1.setGeometry(0, 10, 400, 50)
        self.label2_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label2_1.setFont(QtGui.QFont("Times", 16, QtGui.QFont.Bold))

        self.list2 = QtWidgets.QListWidget(self.stack2)
        self.list2.setGeometry(40, 70, 250, 170)
        self.list2.addItem(QtWidgets.QListWidgetItem("Манная"))
        self.list2.addItem(QtWidgets.QListWidgetItem("Рисовая"))
        self.list2.addItem(QtWidgets.QListWidgetItem("Гороховая"))
        self.list2.addItem(QtWidgets.QListWidgetItem("Гречневая"))

        self.btn2_1 = QtWidgets.QPushButton(self.stack2)
        self.btn2_1.setText("Назад")
        self.btn2_1.setGeometry(QtCore.QRect(60, 250, 120, 40))

        self.btn2_2 = QtWidgets.QPushButton(self.stack2)
        self.btn2_2.setText("Вперед")
        self.btn2_2.setGeometry(QtCore.QRect(220, 250, 120, 40))

    def Window3UI(self):
        self.stack3.resize(400, 320)

        self.label3_1 = QtWidgets.QLabel(self.stack3)
        self.label3_1.setText("Как вы учились в 5 классе:")
        self.label3_1.setGeometry(0, 10, 400, 50)
        self.label3_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label3_1.setFont(QtGui.QFont("Times", 16, QtGui.QFont.Bold))

        self.combo3 = QtWidgets.QComboBox(self.stack3)
        self.combo3.setGeometry(40, 70, 250, 40)

        self.combo3.addItem("Отлично")
        self.combo3.addItem("Хорошо")
        self.combo3.addItem("Удовлетворительно")
        self.combo3.addItem("Неудовлетворительно")

        self.btn3_1 = QtWidgets.QPushButton(self.stack3)
        self.btn3_1.setText("Назад")
        self.btn3_1.setGeometry(QtCore.QRect(60, 250, 120, 40))

        self.btn3_2 = QtWidgets.QPushButton(self.stack3)
        self.btn3_2.setText("Вперед")
        self.btn3_2.setGeometry(QtCore.QRect(220, 250, 120, 40))

    def Window4UI(self):
        self.stack4.resize(400, 320)

        self.label4_1 = QtWidgets.QLabel(self.stack4)
        self.label4_1.setText("Какое у вас образование:")
        self.label4_1.setGeometry(0, 10, 400, 50)
        self.label4_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label4_1.setFont(QtGui.QFont("Times", 16, QtGui.QFont.Bold))

        self.radio4_1 = QtWidgets.QRadioButton(self.stack4)
        self.radio4_1.setText("Начальное")
        self.radio4_1.setGeometry(40, 70, 200, 50)

        self.radio4_2 = QtWidgets.QRadioButton(self.stack4)
        self.radio4_2.setText("Среднее общее")
        self.radio4_2.setGeometry(40, 100, 200, 50)

        self.radio4_3 = QtWidgets.QRadioButton(self.stack4)
        self.radio4_3.setText("Среднее специальное")
        self.radio4_3.setGeometry(40, 130, 200, 50)

        self.radio4_4 = QtWidgets.QRadioButton(self.stack4)
        self.radio4_4.setText("Высшее")
        self.radio4_4.setGeometry(40, 160, 200, 50)

        self.btn4_1 = QtWidgets.QPushButton(self.stack4)
        self.btn4_1.setText("Назад")
        self.btn4_1.setGeometry(QtCore.QRect(60, 250, 120, 40))

        self.btn4_2 = QtWidgets.QPushButton(self.stack4)
        self.btn4_2.setText("Вперед")
        self.btn4_2.setGeometry(QtCore.QRect(220, 250, 120, 40))

    def Window5UI(self):
        self.stack5.resize(400, 320)

        self.label5_1 = QtWidgets.QLabel(self.stack5)
        self.label5_1.setText("Спасибо что воспользовались\nнашей системой!")
        self.label5_1.setGeometry(0, 10, 400, 50)
        self.label5_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label5_1.setFont(QtGui.QFont("Times", 16, QtGui.QFont.Bold))

        self.table5 = QtWidgets.QTableWidget(self.stack5)
        self.table5.setColumnCount(2)
        self.table5.setRowCount(3)

        self.table5.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("Вопросы"))
        self.table5.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem("Ваши ответы"))

        self.table5.setGeometry(10, 70, 380, 170)

        self.table5.setItem(0, 0, QtWidgets.QTableWidgetItem("Выберите любимую кашу"))
        self.table5.setItem(1, 0, QtWidgets.QTableWidgetItem("Как вы учились в 5 классе"))
        self.table5.setItem(2, 0, QtWidgets.QTableWidgetItem("Какое у вас образование"))
        self.table5.setColumnWidth(0, 180)
        self.table5.setColumnWidth(1, 180)

        self.btn5_1 = QtWidgets.QPushButton(self.stack5)
        self.btn5_1.setText("Назад")
        self.btn5_1.setGeometry(QtCore.QRect(60, 250, 120, 40))

        self.btn5_2 = QtWidgets.QPushButton(self.stack5)
        self.btn5_2.setText("Выход")
        self.btn5_2.setGeometry(QtCore.QRect(220, 250, 120, 40))



class Main(QMainWindow, Ui_Main):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        self.btn1_1.clicked.connect(self.ExitApp)
        self.btn1_2.clicked.connect(self.OpenWindow2)

        self.btn2_1.clicked.connect(self.OpenWindow1)
        self.btn2_2.clicked.connect(self.OpenWindow3)

        self.btn3_1.clicked.connect(self.OpenWindow2)
        self.btn3_2.clicked.connect(self.OpenWindow4)

        self.btn4_1.clicked.connect(self.OpenWindow3)
        self.btn4_2.clicked.connect(self.OpenWindow5)

        self.btn5_1.clicked.connect(self.OpenWindow4)
        self.btn5_2.clicked.connect(self.ExitApp)

    def OpenWindow1(self):
        self.QtStack.setCurrentIndex(0)

    def OpenWindow2(self):
        self.QtStack.setCurrentIndex(1)

    def OpenWindow3(self):
        self.QtStack.setCurrentIndex(2)

    def OpenWindow4(self):
        self.QtStack.setCurrentIndex(3)

    def OpenWindow5(self):
        a2 = ""
        for tt in self.list2.selectedItems():
            a2 = tt.text()

        a3 = self.combo3.currentText()

        a4 = ""
        if self.radio4_1.isChecked(): a4 = self.radio4_1.text()
        if self.radio4_2.isChecked(): a4 = self.radio4_2.text()
        if self.radio4_3.isChecked(): a4 = self.radio4_3.text()
        if self.radio4_4.isChecked(): a4 = self.radio4_4.text()

        self.table5.setItem(0, 1, QtWidgets.QTableWidgetItem(a2))
        self.table5.setItem(1, 1, QtWidgets.QTableWidgetItem(a3))
        self.table5.setItem(2, 1, QtWidgets.QTableWidgetItem(a4))

        self.QtStack.setCurrentIndex(4)

    def ExitApp(self):
        QApplication.exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    showMain = Main()
    sys.exit(app.exec_())
