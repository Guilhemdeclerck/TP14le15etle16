from PySide2.QtWidgets import *
import random

class Window(QWidget):
      def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle("Cycle de l'ISEN Yncréa Ouest")
        self.setFixedSize(500,300)

        self.layout = QVBoxLayout()

        self.label = QLabel("CGSI")

        self.button = QPushButton("Changer le cycle")

        #self.text = QTextBlockFormat("CGSI")

        self.layout.addWidget(self.button)
        self.layout.addWidget(self.label)
        #self.layout.addWidget(self.text)

        self.button.clicked.connect(self.buttonclicked)

        self.setLayout(self.layout)

      def  buttonclicked(self):
          list = ["CSI", "CIR", "BIOST", "CENT", "BIAST", "EST"]
          cycle = random.choice(list)
          self.label.setText(cycle)


if __name__ == "__main__":
    app = QApplication([])
    win = Window()
    win.show()
    app.exec_()



