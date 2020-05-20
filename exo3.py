from PySide2.QtWidgets import *
from PySide2.QtGui import *

class Window(QWidget):
      def __init__(self):
        QWidget.__init__(self)

        self.setFixedSize(400, 300)
        self.setWindowTitle("INTERFACE HOMME MACHINE")

        #self.icon = QIcon(C:\Users\user\Desktop\fr-flag)
        #self.setWindowIcon(self.icon)

        self.layout = QVBoxLayout

        self.label = QLabel
        self.label.setAlignement(Qt.AlignCenter)

        self.bar = QProgressBar
        self.bar.setValue(12)

        self.textedit = QLineEdit

        self.button = QPushButton
        self.button.setToolTip("QQ chose s'affiche normalement")


        #self.layout.addWidget(self.icon)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.bar)
        self.layout.addWidget(self.textedit)
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)


if __name__ == "__main__":
    app = QApplication([])
    win = Window()
    win.show()
    app.exec_()
