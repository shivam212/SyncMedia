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
        self.setWindowTitle('SyncMedia')

        self.play=QtWidgets.QPushButton(self)
        self.stop=QtWidgets.QPushButton(self)
        self.play.setText('Play')
        self.stop.setText('Stop')
        self.label=QtWidgets.QLabel("Volume",self)

        self.Slider = QtWidgets.QSlider(self)
        self.Slider.setRange(0, 100)
        self.Slider.sliderMoved.connect(self.setPosition)
        self.Slider.setOrientation(Qt.Horizontal)
        self.Slider.setFocusPolicy(Qt.NoFocus)

        self.VSlider = QtWidgets.QSlider(self)
        self.VSlider.sliderMoved.connect(self.setVPosition)
        self.VSlider.setRange(0, 10)

        self.VSlider.setOrientation(Qt.Horizontal)
        self.VSlider.setFocusPolicy(Qt.NoFocus)

        openAction = QtWidgets.QAction(QtGui.QIcon('open.png'), '&Open', self)
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('Open mp4 movie')
        openAction.triggered.connect(self.openFile)

        menu = self.menuBar()
        file = menu.addMenu(' &File ')
        file.addAction(openAction)

        self.play.clicked.connect(self.play_click)
        self.stop.clicked.connect(self.stop_click)
        self.mediaPlayer =QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.videoWidget = QVideoWidget()

        wid =QtWidgets.QWidget(self)
        self.setCentralWidget(wid)
        wid.resize(wid.sizeHint())

        wid.setAutoFillBackground(True)
        p = wid.palette()
        p.setColor(wid.backgroundRole(), Qt.black)
        wid.setPalette(p)

        self.Slider.setAutoFillBackground(True)
        p = self.Slider.palette()
        p.setColor(self.Slider.backgroundRole(), Qt.black)
        self.Slider.setPalette(p)

        controlLayout=QtWidgets.QHBoxLayout()
        controlLayout.addWidget(self.play)
        controlLayout.addWidget(self.stop)
        controlLayout.addStretch(1)
        controlLayout.addWidget(self.label)
        controlLayout.addWidget(self.VSlider)
        extralayout=QtWidgets.QHBoxLayout()
        
        extralayout.addWidget(self.videoWidget)


        layout =QtWidgets.QVBoxLayout()
        layout.addLayout(extralayout)
        self.videoWidget.update()
        layout.addWidget(self.Slider)
        layout.addLayout(controlLayout)
        wid.setLayout(layout)


        self.mediaPlayer.setVideoOutput(self.videoWidget)
        self.videoWidget.show()
        self.mediaPlayer.positionChanged.connect(self.positionChanged)
        self.mediaPlayer.durationChanged.connect(self.durationChanged)


        self.show()
    def play_click(self):
        if(self.k==0):
            self.mediaPlayer.play()
            self.play.setText('Pause')
            self.videoWidget.update()
            self.k=1
        elif(self.k==1):
            self.mediaPlayer.pause()
            self.play.setText('Play')
            self.k=0
    def stop_click(self):
    	self.mediaPlayer.stop()
    	self.play.setText('Play')
    	self.k=0
    def openFile(self):
        fileName,_=QtWidgets.QFileDialog.getOpenFileName(self, "Open Movie",
                QDir.homePath())

        self.setWindowTitle(f'SyncMedia - {fileName}')

        if fileName != '':
            print(fileName)
            self.mediaPlayer.setMedia(
                    QMediaContent(QUrl.fromLocalFile(fileName)))

    def positionChanged(self,position):
        self.Slider.setValue(position)

    def durationChanged(self,duration):
        self.Slider.setRange(0, duration)

    def setPosition(self, position):
        self.mediaPlayer.setPosition(position)

    def setVPosition(self, position):
        self.mediaPlayer.setVolume(position*10)


app=QtWidgets.QApplication(sys.argv)
window=Window()
sys.exit(app.exec_())