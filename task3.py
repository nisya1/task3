import sys
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtGui import QPainter, QColor
from random import randrange
from UI import Ui_MainWindow as ui


class GoodMoodRising(ui, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.size = 100
        self.dopaint = False

        self.pushButton.clicked.connect(self.drawe)

    def drawe(self):
        self.dopaint = True
        self.update()

    def paintEvent(self, event):
        if self.dopaint:
            qp = QPainter()
            qp.begin(self)
            self.drawelipse(qp)
            qp.end()
        self.dopaint = False

    def drawelipse(self, qp):
        for _ in range(randrange(5, 20)):
            self.color = QColor(randrange(256), randrange(256), randrange(256))
            qp.setBrush(self.color)
            qp.setPen(self.color)
            d = randrange(10, 100)
            qp.drawEllipse(randrange(10, 700), randrange(10, 500), d, d)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GoodMoodRising()
    ex.show()
    sys.exit(app.exec())
