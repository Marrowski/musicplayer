# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGraphicsView, QHeaderView, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSlider,
    QStatusBar, QTreeWidget, QTreeWidgetItem, QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1421, 1048)
        MainWindow.setStyleSheet(u"background-color: Gray;\n"
"font-family: Spotify Mix;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(520, 0, 341, 51))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Roboto"])
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: \"White\";\n"
"font-family: \"Roboto\";\n"
"font-size: 20px")
        self.horizontalSlider = QSlider(self.centralwidget)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setGeometry(QRect(280, 940, 1091, 22))
        sizePolicy.setHeightForWidth(self.horizontalSlider.sizePolicy().hasHeightForWidth())
        self.horizontalSlider.setSizePolicy(sizePolicy)
        self.horizontalSlider.setOrientation(Qt.Orientation.Horizontal)
        self.horizontalSlider_2 = QSlider(self.centralwidget)
        self.horizontalSlider_2.setObjectName(u"horizontalSlider_2")
        self.horizontalSlider_2.setGeometry(QRect(20, 940, 151, 22))
        sizePolicy.setHeightForWidth(self.horizontalSlider_2.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_2.setSizePolicy(sizePolicy)
        self.horizontalSlider_2.setOrientation(Qt.Orientation.Horizontal)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(170, 940, 81, 21))
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setStyleSheet(u"font-size: 10pt;\n"
"color: \"White\";\n"
"")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(710, 970, 51, 41))
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setStyleSheet(u"background-color: \"White\"")
        icon = QIcon()
        icon.addFile(u":/icons/icons/play_arrow_24dp_5F6368_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setCheckable(False)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(760, 970, 51, 41))
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setStyleSheet(u"background-color: \"White\"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/skip_next_24dp_5F6368_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(660, 970, 51, 41))
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setStyleSheet(u"background-color: \"White\"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/skip_previous_24dp_5F6368_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_3.setIcon(icon2)
        self.musicwidget = QWidget(self.centralwidget)
        self.musicwidget.setObjectName(u"musicwidget")
        self.musicwidget.setGeometry(QRect(360, 60, 501, 851))
        sizePolicy.setHeightForWidth(self.musicwidget.sizePolicy().hasHeightForWidth())
        self.musicwidget.setSizePolicy(sizePolicy)
        self.musicwidget.setStyleSheet(u"QWidget#musicwidget {\n"
"    border: 5px solid rgba(255, 255, 255, 40);\n"
"}\n"
"")
        self.graphicsView = QGraphicsView(self.musicwidget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(20, 50, 81, 61))
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.label_3 = QLabel(self.musicwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(110, 50, 361, 51))
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_5 = QLabel(self.musicwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(110, 140, 361, 51))
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.graphicsView_3 = QGraphicsView(self.musicwidget)
        self.graphicsView_3.setObjectName(u"graphicsView_3")
        self.graphicsView_3.setGeometry(QRect(20, 140, 81, 61))
        sizePolicy.setHeightForWidth(self.graphicsView_3.sizePolicy().hasHeightForWidth())
        self.graphicsView_3.setSizePolicy(sizePolicy)
        self.infowidget = QWidget(self.centralwidget)
        self.infowidget.setObjectName(u"infowidget")
        self.infowidget.setGeometry(QRect(870, 60, 501, 851))
        sizePolicy.setHeightForWidth(self.infowidget.sizePolicy().hasHeightForWidth())
        self.infowidget.setSizePolicy(sizePolicy)
        self.infowidget.setStyleSheet(u"QWidget#infowidget {\n"
"    border: 5px solid rgba(255, 255, 255, 40);\n"
"}\n"
"")
        self.graphicsView_6 = QGraphicsView(self.infowidget)
        self.graphicsView_6.setObjectName(u"graphicsView_6")
        self.graphicsView_6.setGeometry(QRect(20, 60, 451, 511))
        sizePolicy.setHeightForWidth(self.graphicsView_6.sizePolicy().hasHeightForWidth())
        self.graphicsView_6.setSizePolicy(sizePolicy)
        self.label_8 = QLabel(self.infowidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(50, 590, 381, 211))
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.musicwidget_2 = QWidget(self.centralwidget)
        self.musicwidget_2.setObjectName(u"musicwidget_2")
        self.musicwidget_2.setGeometry(QRect(20, 60, 321, 851))
        sizePolicy.setHeightForWidth(self.musicwidget_2.sizePolicy().hasHeightForWidth())
        self.musicwidget_2.setSizePolicy(sizePolicy)
        self.musicwidget_2.setStyleSheet(u"QWidget#musicwidget_2 {\n"
"    border: 5px solid rgba(255, 255, 255, 40);\n"
"}\n"
"")
        self.treeWidget = QTreeWidget(self.musicwidget_2)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.treeWidget.setHeaderItem(__qtreewidgetitem)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setGeometry(QRect(20, 30, 281, 192))
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
#if QT_CONFIG(shortcut)
        self.label.setBuddy(self.musicwidget)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Music Player", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Welcome to the music player", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"volume 0%", None))
        self.pushButton.setText("")
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

