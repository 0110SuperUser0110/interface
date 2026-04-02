from pathlib import Path
import sys

from PyQt5 import QtCore, QtGui, QtWidgets


class CircularAIGUI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set window size and remove title bar
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setFixedSize(500, 500)

        # Set window to be transparent
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Load the ring image
        image_path = Path(__file__).resolve().parent.parent / "assets" / "metallic_ring.png"
        self.ring_image = QtGui.QPixmap(str(image_path))
        if self.ring_image.isNull():
            raise FileNotFoundError(f"Unable to load GUI asset: {image_path}")

    def resizeEvent(self, event):
        # Keep the widget mask aligned with the actual widget size.
        self.setMask(QtGui.QRegion(self.rect(), QtGui.QRegion.Ellipse))
        super().resizeEvent(event)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)

        # Draw the ring image centered in the window
        painter.drawPixmap(0, 0, self.width(), self.height(), self.ring_image)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = CircularAIGUI()
    gui.show()
    sys.exit(app.exec_())
