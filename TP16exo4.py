from PySide2.QtWidgets import *

class Window(QWidget):
      def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle("Calculatrice")
        self.layoutprincipale = QVBoxLayout()

        self.text = QTextBrowser()
        self.text.setFixedSize(500,20)

        self.button1 = QPushButton("C")
        self.button1.setFixedSize(250,50)

        self.button2 = QPushButton("CE")
        self.button2.setFixedSize(250,50)

        self.layouth0 = QHBoxLayout()
        self.layouth1 = QHBoxLayout()
        self.layouth2 = QHBoxLayout()
        self.layouth3 = QHBoxLayout()
        self.layouth4 = QHBoxLayout()


        self.button3 = QPushButton("7")
        self.button4 = QPushButton("8")
        self.button5 = QPushButton("9")
        self.button6 = QPushButton("/")
        self.button7 = QPushButton("4")
        self.button8 = QPushButton("5")
        self.button9 = QPushButton("6")
        self.button10 = QPushButton("*")
        self.button11 = QPushButton("1")
        self.button12 = QPushButton("2")
        self.button13 = QPushButton("3")
        self.button14 = QPushButton("-")
        self.button15 = QPushButton("0")
        self.button16 = QPushButton()
        self.button17 = QPushButton("=")
        self.button18 = QPushButton("+")

        self.layoutprincipale.addWidget(self.text)
        self.layouth0.addWidget(self.button1)
        self.layouth0.addWidget(self.button2)
        self.layouth1.addWidget(self.button3)
        self.layouth1.addWidget(self.button4)
        self.layouth1.addWidget(self.button5)
        self.layouth1.addWidget(self.button6)
        self.layouth2.addWidget(self.button7)
        self.layouth2.addWidget(self.button8)
        self.layouth2.addWidget(self.button9)
        self.layouth2.addWidget(self.button10)
        self.layouth3.addWidget(self.button11)
        self.layouth3.addWidget(self.button12)
        self.layouth3.addWidget(self.button13)
        self.layouth3.addWidget(self.button14)
        self.layouth4.addWidget(self.button15)
        self.layouth4.addWidget(self.button16)
        self.layouth4.addWidget(self.button17)
        self.layouth4.addWidget(self.button18)

        self.layoutprincipale.addLayout(self.layouth0)
        self.layoutprincipale.addLayout(self.layouth1)
        self.layoutprincipale.addLayout(self.layouth2)
        self.layoutprincipale.addLayout(self.layouth3)
        self.layoutprincipale.addLayout(self.layouth4)

        self.button3.clicked.connect(self.sept)
        self.button4.clicked.connect(self.huit)
        self.button5.clicked.connect(self.neuf)
        self.button11.clicked.connect(self.un)
        self.button12.clicked.connect(self.deux)
        self.button13.clicked.connect(self.trois)
        self.button7.clicked.connect(self.quatre)
        self.button8.clicked.connect(self.cinq)
        self.button9.clicked.connect(self.six)
        self.button15.clicked.connect(self.zero)

        self.button18.clicked.connect(self.plus)
        self.button17.clicked.connect(self.egal)
        self.button1.clicked.connect(self.clear)
        self.button2.clicked.connect(self.cleare)
        self.button6.clicked.connect(self.division)
        self.button14.clicked.connect(self.moins)
        self.button10.clicked.connect(self.fois)

        self.setLayout(self.layoutprincipale)

      def clear(self):
        self.text.setText("")

      def cleare(self):
        self.text.setText("ah")

      def sept(self):
        self.text.setText("7")

      def huit(self):
        self.text.setText("8")

      def neuf(self):
        self.text.setText("9")

      def un(self):
        self.text.setText("1")

      def deux(self):
        self.text.setText("2")

      def trois(self):
        self.text.setText("3")

      def quatre(self):
        self.text.setText("4")

      def cinq(self):
        self.text.setText("5")

      def six(self):
        self.text.setText("6")

      def zero(self):
        self.text.setText("0")

      def plus(self):
        self.text.setText("")

      def egal(self):
        self.text.setText("49")

      def division(self):
        self.text.setText("")

      def moins(self):
        self.text.setText("")

      def fois(self):
        self.text.setText("")



if __name__ == "__main__":
    app = QApplication([])
    win = Window()
    win.show()
    app.exec_()
