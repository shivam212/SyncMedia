#will contain code for the player
import sys
from PyQt5 import QtWidgets,QtGui

class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.k=1
        self.init_ui()

    def init_ui(self):
        self.play=QtWidgets.QPushButton(self)
        self.stop=QtWidgets.QPushButton(self)
        self.play.setText('Play')
        self.stop.setText('Stop')
        self.play.move(0,700)
        self.stop.move(80,700)
        self.setWindowTitle('SyncMedia')
        self.setGeometry(100,100,1024,768)
        self.play.clicked.connect(self.play_click)
        self.show()
    def play_click(self):
        if(self.k==1):
            self.play.setText('Pause')
            self.k=0
        elif(self.k==0):
            self.play.setText('Play')
            self.k=1

app=QtWidgets.QApplication(sys.argv)
window=Window()
sys.exit(app.exec_())
