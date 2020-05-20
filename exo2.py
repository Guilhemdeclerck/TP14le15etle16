from PySide2.QtWidgets import *

class Window(QWidget):
      def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle("lol")

        self.layout = QGridLayout()

        self.label = QLabel("Ceci est un QLabel")
        self.button1 = QPushButton("Ceci est un QPushButton1")
        self.button2 = QPushButton("Ceci est un QPushButton2")
        self.textedit = QTextEdit("Ceci est un TextEdit")

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)
        self.layout.addWidget(self.textedit)

        self.setLayout(self.layout)


if __name__ == "__main__":
    app = QApplication([])
    win = Window()
    win.show()
    app.exec_()
