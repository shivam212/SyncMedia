#will contain code for the player
import sys
from PyQt5 import QtWidgets,QtGui

def window():
    app = QtWidgets.QApplication(sys.argv)
    w=QtWidgets.QWidget()
    play=QtWidgets.QPushButton(w)
    pause=QtWidgets.QPushButton(w)
    play.setText('Play')
    pause.setText('Pause')
    play.move(0,700)
    pause.move(50,700)
    w.setWindowTitle('SyncMedia')
    w.setGeometry(100,100,1024,768)
    w.show()
    sys.exit(app.exec_())

window()
