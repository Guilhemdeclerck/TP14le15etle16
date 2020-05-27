from PySide2.QtWidgets import *

class Window(QWidget):
      def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle("IHM")
        self.setFixedSize(500,300)

        self.layout = QVBoxLayout()

        self.button = QPushButton("Changer mon texte !")

        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.buttonclicked)

        self.setLayout(self.layout)

      def  buttonclicked(self):
          self.button.close()


if __name__ == "__main__":
    app = QApplication([])
    win = Window()
    win.show()
    app.exec_()
