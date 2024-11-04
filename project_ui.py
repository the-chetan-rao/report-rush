from resources import resources_rc
from PyQt5 import QtCore, QtGui, QtWidgets


class Project(QtWidgets.QFrame):
    def __init__(self, url, parent=None):
        super(Project, self).__init__(parent)

        self.url = url
        self.setStyleSheet("#frame\n"
                           "{\n"
                           "background-color:#F3F4F6;\n"
                           "border-radius: 4px;\n"
                           "border: 1px solid #D1D5DB;\n"
                           "}")
        self.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.setFrameShadow(QtWidgets.QFrame.Raised)
        self.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setStyleSheet("#lineEdit\n"
                                    "{\n"
                                    "background-color:#F3F4F6;\n"
                                    "}")
        self.lineEdit.setFrame(False)
        self.lineEdit.setPlaceholderText("")
        self.lineEdit.setText(self.url)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setMaximumHeight(24)
        self.lineEdit.setMinimumHeight(24)
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.removeButton = QtWidgets.QPushButton(self)
        self.removeButton.setMinimumSize(QtCore.QSize(24, 24))
        self.removeButton.setMaximumSize(QtCore.QSize(24, 24))
        self.removeButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            ":/icons/icons8-cross-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.removeButton.setIcon(icon)
        self.removeButton.setIconSize(QtCore.QSize(24, 24))
        self.removeButton.setFlat(True)
        self.removeButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.removeButton)
