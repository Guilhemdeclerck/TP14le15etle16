from PySide2.QtWidgets import *

class Window(QWidget):
      def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle("IHM")

        self.layout = QHBoxLayout()
        self.bar = QProgressBar()
        self.slider = QSlider()

        self.layout.addWidget(self.bar)
        self.layout.addWidget(self.slider)

        self.slider.valueChanged.connect(self.signal)

        self.setLayout(self.layout)

      def signal(self):
          slot = self.slider.value()
          self.bar.setValue(slot)

      #def slot(self):
          #self.bar.setValue()

if __name__ == "__main__":
    app = QApplication([])
    win = Window()
    win.show()
    app.exec_()
