#will contain code for the player
import sys
from PyQt5 import QtWidgets,QtGui
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import QDir, Qt, QUrl, QSize

class Window(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.k=0
        self.init_ui()

    def init_ui(self):
        self.play=QtWidgets.QPushButton(self)
        self.stop=QtWidgets.QPushButton(self)
        self.play.setText('Play')
        self.stop.setText('Stop')
        self.setWindowTitle('SyncMedia')
        menu = self.menuBar()
        file = menu.addMenu(' &File ')
        openAction = QtWidgets.QAction(QtGui.QIcon('open.png'), '&Open', self)
        openAction.setShortcut('Cmd+O')
        openAction.setStatusTip('Open mp4 movie')
        openAction.triggered.connect(self.openFile)
        open =QtWidgets.QAction(QtGui.QIcon('open.png'), '&Open', self)
        file.addAction(openAction)
        #file.addAction(close)

        self.play.clicked.connect(self.play_click)
        self.mediaPlayer =QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.videoWidget = QVideoWidget()

        wid =QtWidgets.QWidget(self)
        self.setCentralWidget(wid)
        wid.resize(wid.sizeHint())
        controlLayout=QtWidgets.QHBoxLayout()
        controlLayout.addWidget(self.play)
        controlLayout.addWidget(self.stop)
        extralayout=QtWidgets.QHBoxLayout()
        self.videoWidget.resize(self.videoWidget.sizeHint())
        extralayout.addWidget(self.videoWidget)

        layout =QtWidgets.QVBoxLayout()

        layout.addLayout(extralayout)
        self.videoWidget.update()
        layout.addLayout(controlLayout)
        wid.setLayout(layout)

        #self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile("/Users/shivam/Downloads/valerie amy.mp4")))
        self.mediaPlayer.setVideoOutput(self.videoWidget)
        self.videoWidget.show()


        self.show()
    def play_click(self):
        if(self.k==0):
            self.mediaPlayer.play()
            self.play.setText('Pause')
            self.k=1
        elif(self.k==1):
            self.mediaPlayer.pause()
            self.play.setText('Play')
            self.k=0

    def openFile(self):
        fileName, _ =QtWidgets.QFileDialog.getOpenFileName(self, "Open Movie",
                QDir.homePath())

        if fileName != '':
            print(fileName)
            self.mediaPlayer.setMedia(
                    QMediaContent(QUrl.fromLocalFile(fileName)))

app=QtWidgets.QApplication(sys.argv)
window=Window()

sys.exit(app.exec_())
