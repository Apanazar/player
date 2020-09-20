from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimediaWidgets import QVideoWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 700)

        self.centralWidget = QtWidgets.QWidget(MainWindow)
        
        self.videoWidget = QVideoWidget()
        self.videoWidget.setFullScreen(False)   

        self.playlistView = QtWidgets.QListView(self.centralWidget)
        self.playlistView.setStyleSheet("background-color: #000000;\ncolor: #ffffff;\nfont: 15px;")


        self.currentTimeLabel = QtWidgets.QLabel(self.centralWidget)
        self.currentTimeLabel.setText("-:--")
        self.currentTimeLabel.setStyleSheet("color: #ffffff;\nfont: 18px;")

       
        self.timeSlider = QtWidgets.QSlider(self.centralWidget)
        self.timeSlider.setStyleSheet(
                "QSlider::groove:horizontal {\n"
                                "border: 1px solid #ffffff;"
                                "height: 10px;"
                                "border-radius: 4px;"
                                "}\n"
                "QSlider::handle:horizontal {\n"
                                "width: 10px;}\n"
                "QSlider::add-page:qlineargradient {\n"
                                "background: white;"
                                "border-top-right-radius: 9px;"
                                "border-bottom-right-radius: 9px;"
                                "border-top-left-radius: 0px;"
                                "border-bottom-left-radius: 0px;"
                                "}\n"
                "QSlider::sub-page:qlineargradient {\n"
                                "background: black;"
                                "border-top-right-radius: 0px;"
                                "border-bottom-right-radius: 0px;"
                                "border-top-left-radius: 9px;"
                                "border-bottom-left-radius: 9px;"
                                "}")
        self.timeSlider.setOrientation(QtCore.Qt.Horizontal)

        self.totalTimeLabel = QtWidgets.QLabel(self.centralWidget)
        self.totalTimeLabel.setText("-:--")
        self.totalTimeLabel.setStyleSheet("color: #ffffff;font: 18px;")


        self.openButton = QtWidgets.QPushButton(self.centralWidget)
        self.openButton.setText("📁")
        self.openButton.setStyleSheet(
                "QPushButton{\n"
                                "background-color: #000000;\n"
                                "color: #ffffff;\n"
                                "border: 3px outset #1B1B1B;\n"
                                "border-radius: 10px;"
                                "width: 55px;\n"
                                "}\n"
                "QPushButton:hover{\n"
                                "background-color: #171717"
                                "}\n"
                "QPushButton:pressed{\n"
                                "background-color: #000000;\n"
                                "border: 3px inset #1B1B1B;\n"
                                "}")
        self.previousButton = QtWidgets.QPushButton(self.centralWidget)
        self.previousButton.setText("⇦")
        self.previousButton.setStyleSheet(
                "QPushButton{\n"
                                "background-color: #000000;\n"
                                "color: #ffffff;\n"
                                "border: 3px outset #1B1B1B;\n"
                                "border-radius: 10px;"
                                "width: 55px;\n"
                                "}\n"
                "QPushButton:hover{\n"
                                "background-color: #171717"
                                "}\n"
                "QPushButton:pressed{\n"
                                "background-color: #000000;\n"
                                "border: 3px inset #1B1B1B;\n"
                                "}")

        self.playButton = QtWidgets.QPushButton(self.centralWidget)
        self.playButton.setText("▶") #♬
        self.playButton.setStyleSheet(
                "QPushButton{\n"
                                "background-color: #000000;\n"
                                "color: #ffffff;\n"
                                "border: 3px outset #1B1B1B;\n"
                                "border-radius: 10px;"
                                "width: 55px;\n"
                                "}\n"
                "QPushButton:hover{\n"
                                "background-color: #171717"
                                "}\n"
                "QPushButton:pressed{\n"
                                "background-color: #000000;\n"
                                "border: 3px inset #1B1B1B;\n"
                                "}")

        self.pauseButton = QtWidgets.QPushButton(self.centralWidget)
        self.pauseButton.setText("❚❚️")
        self.pauseButton.setStyleSheet(
                "QPushButton{\n"
                                "background-color: #000000;\n"
                                "color: #ffffff;\n"
                                "border: 3px outset #1B1B1B;\n"
                                "border-radius: 10px;"
                                "width: 55px;\n"
                                "}\n"
                "QPushButton:hover{\n"
                                "background-color: #171717"
                                "}\n"
                "QPushButton:pressed{\n"
                                "background-color: #000000;\n"
                                "border: 3px inset #1B1B1B;\n"
                                "}")

        self.stopButton = QtWidgets.QPushButton(self.centralWidget)
        self.stopButton.setText("⬛")
        self.stopButton.setStyleSheet(
                "QPushButton{\n"
                                "background-color: #000000;\n"
                                "color: #ffffff;\n"
                                "border: 3px outset #1B1B1B;\n"
                                "border-radius: 10px;"
                                "width: 55px;\n"
                                "}\n"
                "QPushButton:hover{\n"
                                "background-color: #171717"
                                "}\n"
                "QPushButton:pressed{\n"
                                "background-color: #000000;\n"
                                "border: 3px inset #1B1B1B;\n"
                                "}")

        self.nextButton = QtWidgets.QPushButton(self.centralWidget)
        self.nextButton.setText("⇨")
        self.nextButton.setStyleSheet(
                "QPushButton{\n"
                                "background-color: #000000;\n"
                                "color: #ffffff;\n"
                                "border: 3px outset #1B1B1B;\n"
                                "border-radius: 10px;"
                                "width: 55px;\n"
                                "}\n"
                "QPushButton:hover{\n"
                                "background-color: #171717"
                                "}\n"
                "QPushButton:pressed{\n"
                                "background-color: #000000;\n"
                                "border: 3px inset #1B1B1B;\n"
                                "}")

        self.label = QtWidgets.QPushButton(self.centralWidget)
        self.label.setText("🔈")
        self.label.setStyleSheet(
                "QPushButton{\n"
                                "background-color: #000000;\n"
                                "color: #ffffff;\n"
                                "border: 3px outset #1B1B1B;\n"
                                "border-radius: 10px;"
                                "width: 25px;\n"
                                "}\n"
                "QPushButton:hover{\n"
                                "background-color: #171717"
                                "}\n")
        

        self.volumeSlider = QtWidgets.QSlider(self.centralWidget)
        self.volumeSlider.setMaximum(100)
        self.volumeSlider.setStyleSheet(
                "QSlider::groove:horizontal {\n"
                                "border: 1px solid #ffffff;"
                                "height: 10px;"
                                "border-radius: 4px;"
                                "}\n"
                "QSlider::handle:horizontal {\n"
                                "width: 10px;}\n"
                "QSlider::add-page:qlineargradient {\n"
                                "background: white;"
                                "border-top-right-radius: 9px;"
                                "border-bottom-right-radius: 9px;"
                                "border-top-left-radius: 0px;"
                                "border-bottom-left-radius: 0px;"
                                "}\n"
                 "QSlider::sub-page:qlineargradient {\n"
                                "background: black;"
                                "border-top-right-radius: 0px;"
                                "border-bottom-right-radius: 0px;"
                                "border-top-left-radius: 9px;"
                                "border-bottom-left-radius: 9px;"
                                "}")
        self.volumeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.volumeSlider.setProperty("value", 100)

        self.invButton = QtWidgets.QPushButton("☚")
        self.invButton.setStyleSheet(
                "QPushButton{\n"
                                    "background-color: #000000;\n"
                                    "color: #ffffff;\n"
                                    "border: 3px outset #1B1B1B;\n"
                                    "border-radius: 10px;"
                                    "width: 55px;\n"
                                    "}\n"
                "QPushButton:hover{\n"
                                    "background-color: #171717"
                                    "}\n"
                "QPushButton:pressed{\n"
                                    "background-color: #000000;\n"
                                    "border: 3px inset #1B1B1B;\n"
                                    "}")
        
        self.anButton = QtWidgets.QPushButton("☛")
        self.anButton.setStyleSheet(
                "QPushButton{\n"
                                "background-color: #000000;\n"
                                "color: #ffffff;\n"
                                "border: 3px outset #1B1B1B;\n"
                                "border-radius: 10px;"
                                "width: 55px;\n"
                                "}\n"
                "QPushButton:hover{\n"
                                "background-color: #171717"
                                "}\n"
                "QPushButton:pressed{\n"
                                "background-color: #000000;\n"
                                "border: 3px inset #1B1B1B;\n"
                                "}")
                                        
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralWidget)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.horizontalLayout_up = QtWidgets.QHBoxLayout()
        self.horizontalLayout_low = QtWidgets.QHBoxLayout()

        displayLayout = QtWidgets.QHBoxLayout()
        displayLayout.addWidget(self.videoWidget, 2)
        displayLayout.addWidget(self.playlistView)
       

        self.horizontalLayout_up.addWidget(self.currentTimeLabel)
        self.horizontalLayout_up.addWidget(self.timeSlider)
        self.horizontalLayout_up.addWidget(self.totalTimeLabel)

        self.horizontalLayout_low.addWidget(self.openButton)
        self.horizontalLayout_low.addStretch(1)
        self.horizontalLayout_low.addWidget(self.previousButton)
        self.horizontalLayout_low.addWidget(self.playButton)
        self.horizontalLayout_low.addWidget(self.pauseButton)
        self.horizontalLayout_low.addWidget(self.stopButton)
        self.horizontalLayout_low.addWidget(self.nextButton)
        self.horizontalLayout_low.addWidget(self.label)
        self.horizontalLayout_low.addWidget(self.volumeSlider)
        self.horizontalLayout_low.addStretch(1)
        self.horizontalLayout_low.addWidget(self.invButton)
        self.horizontalLayout_low.addWidget(self.anButton)

        self.verticalLayout.addLayout(displayLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_up)
        self.verticalLayout.addLayout(self.horizontalLayout_low)

        self.horizontalLayout.addLayout(self.verticalLayout)


        MainWindow.setCentralWidget(self.centralWidget)
        self.retranslateUi(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ABPlayer"))
