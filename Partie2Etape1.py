from PySide2.QtWidgets import *
from TP15étape2 import*

class LabeledTextField(QWidget):
      def __init__(self, text):
        QWidget.__init__(self)

        self.layout = QHBoxLayout()

        self.label = QLabel(text)

        self.textedit = QTextEdit("")
        self.textedit.setMaximumHeight(20)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.textedit)

        self.setLayout(self.layout)

if __name__ == "__main__":
    app = QApplication([])
    win = LabeledTextField()
    win.show()
    app.exec_()


