from PySide2.QtWidgets import *

class ButtonsPanel(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.layout = QHBoxLayout()

        self.button1 = QPushButton("Configure")
        self.button2 = QPushButton("Connect")
        self.button3 = QPushButton("Disconnect")

        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)
        self.layout.addWidget(self.button3)

        self.setLayout(self.layout)

if __name__ == "__main__":
    app = QApplication([])
    win = ButtonsPanel()
    win.show()
    app.exec_()
