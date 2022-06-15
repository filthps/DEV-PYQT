"""
Санчала сконвертировать форму созданную через pyside2-designer
 pyside2-uic my_form.ui -o my_form.py
"""
import sys
from PySide2 import QtWidgets, QtCore
from ui.my_form import Ui_MainWindow


class MyApp(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.app_width = None
        self.app_height = None

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_2.clicked.connect(self.move_top_left)
        self.ui.pushButton.clicked.connect(self.move_top_right)

    def get_width(self):
        if self.app_width is None:
            width = QtWidgets.QApplication.screenAt( self.width())

    def move_top_left(self):
        self.move(0, 0)

    def move_top_right(self):
        w = QtWidgets.QApplication.screenAt(self.pos())
        self.move(w, 0)


if __name__ == "__main__":
    root = QtWidgets.QApplication(sys.argv)
    my_app = MyApp()
    my_app.show()
    root.exec_()
