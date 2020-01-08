import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
from random import randint


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.draw = False
        self.pushButton.clicked.connect(self.paint)
        self.show()

    def paintEvent(self, event):
        if self.draw:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(255, 255, 0))
            for i in range(30):
                radius = randint(0, 300)
                qp.drawEllipse(randint(0, 800), randint(0, 800), radius, radius)
            qp.end()
            self.draw = False

    def paint(self):
        self.draw = True
        self.update()


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())