# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from resources import resources_rc
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 503)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("#centralwidget\n"
                                         "{\n"
                                         "background-color: #FFFFFF;\n"
                                         "}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setStyleSheet("#page\n"
                                "{\n"
                                "background-color: #FFFFFF;\n"
                                "}")
        self.page.setObjectName("page")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame = QtWidgets.QFrame(self.page)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 40, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setContentsMargins(150, 0, 150, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setSpacing(12)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEditURL = QtWidgets.QLineEdit(self.frame_5)
        self.lineEditURL.setMinimumSize(QtCore.QSize(0, 32))
        self.lineEditURL.setFrame(True)
        self.lineEditURL.setObjectName("lineEditURL")
        self.horizontalLayout_2.addWidget(self.lineEditURL)
        self.ButtonAdd = QtWidgets.QPushButton(self.frame_5)
        self.ButtonAdd.setMinimumSize(QtCore.QSize(32, 32))
        self.ButtonAdd.setMaximumSize(QtCore.QSize(35, 35))
        self.ButtonAdd.setStyleSheet("#ButtonAdd\n"
                                     "{\n"
                                     "background-color: #3B82F6;\n"
                                     "border-radius: 4px;\n"
                                     "}")
        self.ButtonAdd.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons8-add-96.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButtonAdd.setIcon(icon)
        self.ButtonAdd.setIconSize(QtCore.QSize(16, 16))
        self.ButtonAdd.setFlat(False)
        self.ButtonAdd.setObjectName("ButtonAdd")
        self.horizontalLayout_2.addWidget(self.ButtonAdd)
        self.verticalLayout_4.addWidget(self.frame_5)
        self.scrollArea = QtWidgets.QScrollArea(self.frame_4)
        self.scrollArea.setStyleSheet("#scrollAreaWidgetContents\n"
                                      "{\n"
                                      "background-color: #FFF;\n"
                                      "}")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 476, 69))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_4.addWidget(self.scrollArea)
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.frame_6 = QtWidgets.QFrame(self.frame_4)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEditLoc = QtWidgets.QLineEdit(self.frame_6)
        self.lineEditLoc.setMinimumSize(QtCore.QSize(0, 32))
        self.lineEditLoc.setFrame(True)
        self.lineEditLoc.setObjectName("lineEditLoc")
        self.horizontalLayout_3.addWidget(self.lineEditLoc)
        self.ButtonPath = QtWidgets.QPushButton(self.frame_6)
        self.ButtonPath.setMinimumSize(QtCore.QSize(32, 32))
        self.ButtonPath.setMaximumSize(QtCore.QSize(35, 35))
        self.ButtonPath.setStyleSheet("#ButtonPath\n"
                                      "{\n"
                                      "background-color: #E5E7EB;\n"
                                      "border-radius: 4px;\n"
                                      "}")
        self.ButtonPath.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/folder.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButtonPath.setIcon(icon1)
        self.ButtonPath.setIconSize(QtCore.QSize(16, 16))
        self.ButtonPath.setFlat(False)
        self.ButtonPath.setObjectName("ButtonPath")
        self.horizontalLayout_3.addWidget(self.ButtonPath)
        self.verticalLayout_4.addWidget(self.frame_6)
        self.ButtonStart = QtWidgets.QPushButton(self.frame_4)
        self.ButtonStart.setMinimumSize(QtCore.QSize(0, 25))
        self.ButtonStart.setStyleSheet("#ButtonStart\n"
                                       "{\n"
                                       "background-color: #22C55E;\n"
                                       "border-radius: 4px;\n"
                                       "color:#FFF;\n"
                                       "}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons8-play-96.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButtonStart.setIcon(icon2)
        self.ButtonStart.setObjectName("ButtonStart")
        self.verticalLayout_4.addWidget(self.ButtonStart)
        self.labelMinimize = QtWidgets.QLabel(self.frame_4)
        self.labelMinimize.setWordWrap(True)
        self.labelMinimize.setObjectName("labelMinimize")
        self.verticalLayout_4.addWidget(self.labelMinimize)
        self.frame_7 = QtWidgets.QFrame(self.frame_4)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_4.addWidget(self.frame_7)
        self.verticalLayout_3.addWidget(self.frame_4)
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setStyleSheet("#frame_3\n"
                                   "{\n"
                                   "background-color: #F3F4F6;\n"
                                   "}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setContentsMargins(20, 0, 10, 15)
        self.horizontalLayout.setSpacing(180)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ButtonX = QtWidgets.QPushButton(self.frame_3)
        self.ButtonX.setStyleSheet("color: #b18c96;")
        self.ButtonX.setFlat(True)
        self.ButtonX.setObjectName("ButtonX")
        self.horizontalLayout.addWidget(self.ButtonX)
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(
            self.label_3, 0, QtCore.Qt.AlignVCenter)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.verticalLayout_5.addWidget(self.frame)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.widget = QtWidgets.QWidget(self.page_2)
        self.widget.setStyleSheet("QPushButton#pushButton{\n"
                                  "    background-color:rgba(85, 98, 112, 255);\n"
                                  "    color:rgba(255, 255, 255, 200);\n"
                                  "    border-radius:5px;\n"
                                  "}\n"
                                  "QPushButton#pushButton:pressed{\n"
                                  "    padding-left:5px;\n"
                                  "    padding-top:5px;\n"
                                  "    background-color:rgba(255, 107, 107, 255);\n"
                                  "    background-position:calc(100% - 10px)center;\n"
                                  "}\n"
                                  "QPushButton#pushButton:hover{\n"
                                  "    background-color:rgba(255, 107, 107, 255);\n"
                                  "}")
        self.widget.setObjectName("widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_8 = QtWidgets.QFrame(self.widget)
        self.frame_8.setMinimumSize(QtCore.QSize(400, 0))
        self.frame_8.setStyleSheet("#frame_8 {\n"
                                   "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 98, 112, 255), stop:1 rgba(255, 107, 107, 255));\n"
                                   "    border-top-right-radius: 10px; /* Top-right corner */\n"
                                   "    border-bottom-right-radius: 10px; /* Bottom-right corner */\n"
                                   "}\n"
                                   "")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_6.setContentsMargins(50, 60, 50, 20)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:rgba(255, 255, 255, 220);")
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_6.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.frame_8)
        self.label_6.setMinimumSize(QtCore.QSize(0, 5))
        self.label_6.setMaximumSize(QtCore.QSize(200, 5))
        self.label_6.setStyleSheet("background-color:rgba(255, 107, 107, 255);\n"
                                   "border-radius: 2px;")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_6.addWidget(self.label_6)
        self.label_9 = QtWidgets.QLabel(self.frame_8)
        self.label_9.setStyleSheet("color:rgba(255, 255, 255, 220);")
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_6.addWidget(self.label_9)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem1)
        self.horizontalLayout_4.addWidget(self.frame_8)
        self.frame_9 = QtWidgets.QFrame(self.widget)
        self.frame_9.setMinimumSize(QtCore.QSize(400, 0))
        self.frame_9.setStyleSheet("#frame_9{\n"
                                   "background-color:rgba(255, 255, 255, 255);\n"
                                   "}")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_7.setContentsMargins(35, 40, 35, 20)
        self.verticalLayout_7.setSpacing(50)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_8 = QtWidgets.QLabel(self.frame_9)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:rgba(0, 0, 0, 200);")
        self.label_8.setObjectName("label_8")
        self.verticalLayout_7.addWidget(
            self.label_8, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.lineEditEmail = QtWidgets.QLineEdit(self.frame_9)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEditEmail.setFont(font)
        self.lineEditEmail.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
                                         "border:2px solid rgba(0, 0, 0, 0);\n"
                                         "border-bottom-color:rgba(46, 82, 101, 200);\n"
                                         "color:rgb(0, 0, 0);\n"
                                         "padding-bottom:7px;")
        self.lineEditEmail.setObjectName("lineEditEmail")
        self.verticalLayout_7.addWidget(self.lineEditEmail)
        self.lineEditPassword = QtWidgets.QLineEdit(self.frame_9)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEditPassword.setFont(font)
        self.lineEditPassword.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
                                            "border:2px solid rgba(0, 0, 0, 0);\n"
                                            "border-bottom-color:rgba(46, 82, 101, 200);\n"
                                            "color:rgb(0, 0, 0);\n"
                                            "padding-bottom:7px;")
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.verticalLayout_7.addWidget(self.lineEditPassword)
        self.ButtonLogin = QtWidgets.QPushButton(self.frame_9)
        self.ButtonLogin.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.ButtonLogin.setFont(font)
        self.ButtonLogin.setStyleSheet("QPushButton{\n"
                                       "    background-color:rgba(85, 98, 112, 255);\n"
                                       "    color:rgba(255, 255, 255, 200);\n"
                                       "    border-radius:5px;\n"
                                       "}\n"
                                       "QPushButton:pressed{\n"
                                       "    padding-left:5px;\n"
                                       "    padding-top:5px;\n"
                                       "    background-color:rgba(255, 107, 107, 255);\n"
                                       "    background-position:calc(100% - 10px)center;\n"
                                       "}\n"
                                       "QPushButton:hover{\n"
                                       "    background-color:rgba(255, 107, 107, 255);\n"
                                       "}")
        self.ButtonLogin.setObjectName("ButtonLogin")
        self.verticalLayout_7.addWidget(self.ButtonLogin)
        spacerItem2 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem2)
        self.label_11 = QtWidgets.QLabel(self.frame_9)
        self.label_11.setWordWrap(True)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_7.addWidget(self.label_11)
        self.horizontalLayout_4.addWidget(self.frame_9)
        self.verticalLayout_8.addWidget(self.widget)
        self.stackedWidget.addWidget(self.page_2)
        self.verticalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ReportRush"))
        self.label.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">ReportRush</span></p></body></html>"))
        self.label_2.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Project URLs:</span></p></body></html>"))
        self.lineEditURL.setPlaceholderText(_translate(
            "MainWindow", "Enter Semrush project URL"))
        self.label_4.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Output Folder:</span></p></body></html>"))
        self.lineEditLoc.setPlaceholderText(_translate(
            "MainWindow", "C:\\Users\\YourName\\Documents\\SemrushReports"))
        self.ButtonStart.setText(_translate("MainWindow", "Start Process"))
        self.labelMinimize.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">It\'s safe to minimise the app. ReportRush will notify you once the run is complete.</span></p></body></html>"))
        self.ButtonX.setText(_translate(
            "MainWindow", "Did I save you some time? Follow me on X / Twitter for SEO hacks that work."))
        self.label_3.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" color:#b18c96;\">Not affiliated with or endorsed by Semrush</span></p></body></html>"))
        self.label_5.setText(_translate(
            "MainWindow", "<html><head/><body><p>ReportRush</p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Automate the grunt work of exporting site audit issue reports from SEMrush. This open-source tool is not affiliated with or endorsed by SEMrush in any way.</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "Log In"))
        self.lineEditEmail.setPlaceholderText(
            _translate("MainWindow", "Email"))
        self.lineEditPassword.setPlaceholderText(
            _translate("MainWindow", "Password"))
        self.ButtonLogin.setText(_translate("MainWindow", "L o g  I n"))
        self.label_11.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">ReportRush does not store your password.</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())