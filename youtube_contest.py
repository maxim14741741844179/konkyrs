#подключение библиотек
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox, QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton
#создание приложения и главного окна
qpp = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('викторина по хрен знает чему')
main_win.move(100, 10)
main_win.resize(1500, 900)
#создание виджетов главного окна
gg = QLabel('Когда появился YouTube?')
r_btn1 = QRadioButton('2005')
r_btn2 = QRadioButton('2010')
r_btn3 = QRadioButton('2015')
r_btn4 = QRadioButton('2020')
#расположение виджетов по лэйаутам
y = QVBoxLayout()
x = QHBoxLayout()
x1 = QHBoxLayout()
x2 = QHBoxLayout()
y.addLayout(x)
y.addLayout(x1)
y.addLayout(x2)
x.addWidget(gg, alignment = Qt.AlignCenter)
x1.addWidget(r_btn1, alignment = Qt.AlignCenter)
x1.addWidget(r_btn2, alignment = Qt.AlignCenter)
x2.addWidget(r_btn3, alignment = Qt.AlignCenter)
x2.addWidget(r_btn4, alignment = Qt.AlignCenter)
main_win.setLayout(y)
#обработка нажатий на переключатели
def victor():
    victor1 = QMessageBox()
    victor1.setText('типа победа')
    victor1.exec_()
    main_win.close()
def victor2():
    victor1 = QMessageBox()
    victor1.setText('типа проигрышь')
    victor1.exec_()
    main_win.close()
r_btn1.clicked.connect(victor)
r_btn2.clicked.connect(victor2)
r_btn3.clicked.connect(victor2)
r_btn4.clicked.connect(victor2)
#отображение окна приложения 
main_win.show()
qpp.exec()