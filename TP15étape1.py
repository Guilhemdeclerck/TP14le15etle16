from PySide2.QtWidgets import *
from TP15étape2 import*
from TP15Partie2Etape1 import*
from TP15Partie2Etape2 import*

class SQLClientWindow(QWidget):
      def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle("SQLT Client")
        self.setFixedSize(600,400)

        self.layout = QVBoxLayout()

        self.buttonspanel = ButtonsPanel()
        self.notificationPanel = QTextEdit("oui")
        self.resulttable = QTableWidget(5,3)
        self.resulttable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.layout.addWidget(self.buttonspanel)
        self.layout.addWidget(self.notificationPanel)
        self.layout.addWidget(self.resulttable)

        self.setLayout(self.layout)

if __name__ == "__main__":
    app = QApplication([])
    dial = ConfigurationDialog()
    win = SQLClientWindow()
    win.show()
    dial.show()
    app.exec_()

