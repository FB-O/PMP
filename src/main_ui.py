# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

from custom_widgets.slider import JumpSlider

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 467)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_media = QFrame(self.centralwidget)
        self.frame_media.setObjectName(u"frame_media")
        self.frame_media.setStyleSheet(u"")
        self.frame_media.setFrameShape(QFrame.StyledPanel)
        self.frame_media.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_media)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.videoWidget = QVideoWidget(self.frame_media)
        self.videoWidget.setObjectName(u"videoWidget")

        self.horizontalLayout_4.addWidget(self.videoWidget)


        self.verticalLayout.addWidget(self.frame_media)

        self.frame_bar = QFrame(self.centralwidget)
        self.frame_bar.setObjectName(u"frame_bar")
        self.frame_bar.setMaximumSize(QSize(16777215, 24))
        self.frame_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_bar)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(6, 0, 6, 0)
        self.lbl_position = QLabel(self.frame_bar)
        self.lbl_position.setObjectName(u"lbl_position")

        self.horizontalLayout_3.addWidget(self.lbl_position)

        self.slider_progressBar = JumpSlider(self.frame_bar)
        self.slider_progressBar.setObjectName(u"slider_progressBar")
        self.slider_progressBar.setMaximum(1000)
        self.slider_progressBar.setSingleStep(0)
        self.slider_progressBar.setOrientation(Qt.Horizontal)

        self.horizontalLayout_3.addWidget(self.slider_progressBar)

        self.lbl_duration = QLabel(self.frame_bar)
        self.lbl_duration.setObjectName(u"lbl_duration")

        self.horizontalLayout_3.addWidget(self.lbl_duration)


        self.verticalLayout.addWidget(self.frame_bar)

        self.frame_controls = QFrame(self.centralwidget)
        self.frame_controls.setObjectName(u"frame_controls")
        self.frame_controls.setMaximumSize(QSize(16777215, 25))
        self.frame_controls.setFrameShape(QFrame.StyledPanel)
        self.frame_controls.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_controls)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(6, 0, 6, 0)
        self.pb_play = QPushButton(self.frame_controls)
        self.pb_play.setObjectName(u"pb_play")
        self.pb_play.setEnabled(False)
        self.pb_play.setMaximumSize(QSize(30, 24))

        self.horizontalLayout_2.addWidget(self.pb_play)


        self.verticalLayout.addWidget(self.frame_controls, 0, Qt.AlignLeft)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionOpen)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.lbl_position.setText(QCoreApplication.translate("MainWindow", u"-- : -- : --", None))
        self.lbl_duration.setText(QCoreApplication.translate("MainWindow", u"-- : -- : --", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

