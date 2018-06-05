#will contain code for the player
import sys
from PyQt5 import QtWidgets,QtGui
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import QDir, Qt, QUrl

class Window(QtWidgets.QMainWindow):

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
        self.mediaPlayer =QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.videoWidget = QVideoWidget()
        self.videoWidget.setGeometry(100,100,500,500)
        wid =QtWidgets.QWidget(self)
        self.setCentralWidget(wid)
        controlLayout=QtWidgets.QHBoxLayout()
        controlLayout.addWidget(self.play)
        controlLayout.addWidget(self.stop)
        layout =QtWidgets.QVBoxLayout()

        layout.addWidget(self.videoWidget)
        layout.addLayout(controlLayout)
        wid.setLayout(layout)
        self.videoWidget.move(500,500)
        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile("/Users/shivam/Downloads/valerie amy.mp4")))
        self.mediaPlayer.setVideoOutput(self.videoWidget)
        self.videoWidget.show()
        self.mediaPlayer.play()
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
