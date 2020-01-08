import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from UI import Ui_MainWindow
from random import randint


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.draw = False
        self.pushButton.clicked.connect(self.paint)
        self.show()

    def paintEvent(self, event):
        if self.draw:
            qp = QPainter()
            qp.begin(self)
            for i in range(30):
                radius = randint(0, 300)
                r = randint(0, 255)
                g = randint(0, 255)
                b = randint(0, 255)
                qp.setBrush(QColor(r, g, b))
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
