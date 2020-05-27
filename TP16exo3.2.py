from PySide2.QtWidgets import *

class Window(QWidget):
      def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle("Cycle de l'ISEN Yncréa Ouest")
        self.setFixedSize(500,300)

        self.i = 0

        self.layout = QVBoxLayout()

        self.button = QPushButton("Changer mon texte !")
        self.textedit = QTextEdit("LEnombre de clic va être afficher ici")

        self.layout.addWidget(self.button)
        self.layout.addWidget(self.textedit)

        self.button.clicked.connect(self.buttonclicked)

        self.setLayout(self.layout)

      def  buttonclicked(self):
          self.i += 1
          self.button.setText("Clic"+ str(self.i))
          self.textedit.setText("Clic"+ str(self.i))
          print("Clic"+str(self.i))

if __name__ == "__main__":
    app = QApplication([])
    win = Window()
    win.show()
    app.exec_()


#def  buttonclicked(self, i =0):
          #if i == 5:
              #print("ca fait bcp la non")
          #else: return self.button.set("Clic", i+1)
