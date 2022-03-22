import sys, random
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen, QFont, QFontMetrics
from PyQt5.QtCore import Qt

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 1800, 700)
        self.setWindowTitle('Points')
        self.show()

    def paintEvent(self, e):
        painter = QPainter()
        painter.setRenderHints(QPainter.Antialiasing)
        str = "GangHui"

        font = QFont()
        font.setPixelSize(400)
        fm = QFontMetrics(font)
        w = fm.horizontalAdvance(str)
        h = fm.height()
        ascent = fm.ascent()
        descent = fm.descent()
        leading = fm.leading()
        lineSpacing = fm.lineSpacing()
        print("fm.horizontalAdvance(str):", w)
        print("fm.height():", h)
        print("fm.ascent():", ascent)
        print("fm.descent():", descent)
        print("fm.leading():", leading)
        print("fm.lineSpacing():", lineSpacing)
        base = 500
        painter.begin(self)
        painter.setFont(font)
        painter.drawText(150, base, str)

        # 基线 红色
        painter.setPen(Qt.red)
        painter.drawLine(150, base, w, base)

        # 高度线 绿色 height = ascent + descent
        painter.setPen(Qt.green)
        painter.drawLine(150, base - h, w, base - h)

        # 上升线 青色
        painter.setPen(Qt.cyan)
        painter.drawLine(150, base - ascent, w, base - ascent)

        # 下沉线 蓝色
        painter.setPen(Qt.blue)
        painter.drawLine(150, base + descent, w, base + descent)

        rect = fm.boundingRect(str)
        rect.moveTo(150, base - ascent)
        painter.fillRect(rect, QColor(123, 123, 123, 123))
        painter.end()

    def drawPoints(self, qp):
        qp.setPen(Qt.red)
        size = self.size()

        for i in range(1000):
            x = random.randint(1, size.width() - 1)
            y = random.randint(1, size.height() - 1)
            qp.drawPoint(x, y)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())