from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import QPainter, QColor
from PyQt6 import uic, QtGui
from random import randint
import sys


class circleWidget(QWidget):
    def __init__(self):
        super().__init__()

    def paintEvent(self, event):
        painter = QPainter(self)

        painter.setBrush(
            QColor(255, 255, 0)
        )

        for i in range(randint(1, 50)):
            radius = randint(10, 200)
            painter.drawEllipse(
                randint(0, 600), randint(0, 600), radius, radius)


class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)

        self.button.clicked.connect(self.funcDrawCircles)

    def funcDrawCircles(self):
        self.circle = circleWidget()
        self.setCentralWidget(self.circle)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = mainWindow()
    ex.show()
    sys.exit(app.exec())
