import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.uic.properties import QtGui
from random import randint

from UI import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.flag = False
        self.pushButton.clicked.connect(self.onClicked)

    def onClicked(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            self.drawFlag(qp)
            qp.end()

    def drawFlag(self, qp):
        pen = QPen(Qt.yellow, 4)
        qp.setPen(pen)
        x_coor = randint(50, 400)
        y_coor = randint(50, 400)
        diameter = randint(10, 400)
        qp.drawEllipse(x_coor, y_coor, diameter, diameter)


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
