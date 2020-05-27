from PySide2.QtWidgets import *
from TP15Partie2Etape1 import*

class ConfigurationDialog(QDialog):
      def __init__(self):
        QDialog.__init__(self)

        self.setWindowTitle("Configuration")

        self.layout = QHBoxLayout()

        self.obj1 = LabeledTextField("IP address")
        self.obj2 = LabeledTextField("User")
        self.obj3 = LabeledTextField("Password")

        self.layout.addWidget(self.obj1)
        self.layout.addWidget(self.obj2)
        self.layout.addWidget(self.obj3)

        self.setLayout(self.layout)

if __name__ == "__main__":
    app = QApplication([])
    win = ConfigurationDialog()
    win.show()
    app.exec_()
