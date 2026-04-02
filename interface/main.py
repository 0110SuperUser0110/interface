import sys

from PyQt5 import QtCore, QtWidgets

from gui.gui import CircularAIGUI


def main() -> int:
    app = QtWidgets.QApplication(sys.argv)

    window = CircularAIGUI()
    window.setWindowFlags(
        QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint
    )
    window.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
    window.show()

    return app.exec_()


if __name__ == "__main__":
    raise SystemExit(main())
